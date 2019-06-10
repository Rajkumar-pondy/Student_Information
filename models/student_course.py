from odoo import models, fields, api

class student_course(models.Model):
    _name='student.course'
    _inherit='mail.thread'
    _description="Student Course Details"
#     _inherits={'student.details':'student_code','student.fee':'fee_receipt_no'}
#     _sql_constraints = [('course_code','unique(course_code)', 'Course code must be unique')]
    _rec_name="course_code"
    
    
    course_code=fields.Char("Course Id",required=True,track_visibility='onchange')
#     course_name=fields.Char("Course Name")
    
    #Relation Fields
    course_stu_id=fields.Many2one('student.details',string="Student name",delegate=True,required=True)

    fee_course_ids=fields.One2many('student.fee','course_fee_id',string="Fee course ids")

    
