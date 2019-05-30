# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import re

class student_details(models.Model):
    _name = 'student.details'
    _inherit='mail.thread'
    _description="Student Information"
    _rec_name='student_code'
    _sql_constraints = [('student_code','unique(student_code)', 'Student code must be unique')]

    #Basic fields
    student_code=fields.Char('Student id')
    student_name = fields.Char('Student Name')
    email = fields.Char('Email', track_visibility='onchange')
    contact = fields.Char('Contact Number',track_visibility='always')
    dob = fields.Date('Date of Birth')
    registration_date = fields.Datetime('Registration Date')
    image = fields.Binary('Image',store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    age = fields.Integer("Age",compute='calculate_age',store=True)
    department = fields.Char("Department Name")
    

    #Relational_fields
    report_student_ids= fields.One2many('student.report','student_id_report')
    
    student_receipt_ids=fields.One2many('student.fee','fee_stu_id')
    
    student_course_ids=fields.One2many('student.course','course_stu_id')
    


    #Compute fields    
    @api.depends('dob')
    def calculate_age(self):
        for rec in self:
            if rec.dob:
                current_year=datetime.datetime.now().year
                birth_year=self.dob.year
                rec.age=current_year- birth_year
    @api.onchange('email')
    def Email(self):
        for rec in self:
            if rec.email:
                match=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', rec.email)
                if match==None:
                    raise ValidationError('Not a valid Email ID')
                
    @api.multi
    def name_get(self,cr,uid,ids,context={}):
        if not len(ids):
            return []
        res=[]
        for student in self.browse(cr,uid,ids,context=context):
            res.append((student.student_code,student.student_name+','+student.student_code))
            return res
                
