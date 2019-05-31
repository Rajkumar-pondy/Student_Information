from odoo import models, fields, api
class student_fee(models.Model):
    _name='student.fee'
    _description="Student Fee Structure"
    _rec_name="fee_code"
    _sql_constraints = [('fee_code','unique(fee_code)', 'Student Fee code must be unique')]
    
    fee_code=fields.Char("Fee Receipt Id")
    semester_no=fields.Char("Semester No")
    tution_fee=fields.Float("Tuition Fee")
    
    #Relational Fields
    fee_stu_id=fields.Many2one('student.details',string="Student name",ondelete='restrict',delegate=True,required=True)
    course_fee_id=fields.Many2one('student.course')
    
   