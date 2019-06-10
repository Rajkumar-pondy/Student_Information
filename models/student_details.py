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
    _rec_name='student_name'
#     _sql_constraints = [('student_code','unique(student_code)', 'Student code must be unique')]

    #Basic fields
    student_code=fields.Char('Student id')
    student_name = fields.Char('Student Name')
    email = fields.Char('Email', track_visibility='onchange')
    contact = fields.Char('Contact Number')
    dob = fields.Date('Date of Birth')
    registration_date = fields.Datetime('Registration Date')
    image = fields.Binary('Image',store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    age = fields.Integer("Age",compute='calculate_age',store=True)
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
       
#     @api.depends('student_code')
#     def random_student(self):
#         chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
#         self.write({ ''.join(random.SystemRandom().choice(chars) for _ in range(6))})


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
    
        
        
   
   