# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import re
import random

class student_details(models.Model):
    _name = 'student.details'
    _inherit='mail.thread'
    _description="Student Information"
    _rec_name='name'

    #Basic fields
    student_code=fields.Char(required=True,copy=False,index=True,default='New')
    name = fields.Char('Name')
    email = fields.Char('Email')
    active=fields.Boolean()
    contact = fields.Char('Contact Number')
    dob = fields.Date('Date of Birth')
    registration_date = fields.Datetime('Registration Date')
    image = fields.Binary('Image',store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    age = fields.Integer("Age",compute='calculate_age',store=True,readonly=False)
    department = fields.Char("Department Name")
    states=fields.Selection([
                            ('started','Set to started'),
                            ('progress','In progress'),
                            ('finished','Done'),
                            ], default='started',track_visibility='onchange')
    #Relational_fields
    report_student_ids= fields.One2many('student.report','student_report_id')
    
    student_receipt_ids=fields.One2many('student.fee','fee_stu_id')
    
    student_course_ids=fields.One2many('student.course','course_stu_id')

    #Compute fields
    @api.depends('dob')
    def calculate_age(self):
            if self.dob:
                current_year=datetime.datetime.now().year
                birth_year=self.dob.year
                self.age=current_year- birth_year
    
    @api.onchange('email')
    def email_validation(self):
            if self.email:
                match=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
                if match==None:
                    raise ValidationError('Not a valid Email ID')
    @api.one
    def progress_started(self):
        self.write({
                    'states': 'started',
                  })
   
    @api.one
    def progress_progressbar(self):
        self.write({
                    'states': 'progress'
        })
 
#This function is triggered when the user clicks on the button 'Done'
    @api.one
    def done_progressbar(self):
        self.write({
                    'states': 'finished',
                    })
    @api.multi
    def name_get(self):
        context={}
        res=[]
        for record in self:
            if context.get('student_special_name',False):
                res.append((record.id,record.name))
            else:
                res.append((record.id,'%s,%s' %(record.name,record.department)))
        return res
    @api.model
    def create(self,vals):
        if vals.get('student_code','New')=='New':
             vals['student_code'] = self.env['ir.sequence'].next_by_code('student.details') or '/'
        return super(student_details, self).create(vals)
    
    def toggle_active(self):
        res=super(student_details,self).toggle_active()
        return res