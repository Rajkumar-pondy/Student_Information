from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit='product.template'
#     _description="Student Course Details"
#     _inherits={'student.details':'student_code','student.fee':'fee_receipt_no'}
#     _sql_constraints = [('course_code','unique(course_code)', 'Course code must be unique')]
#     _rec_name="course_code"
    
    
    register_date=fields.Date("register Date",required=True)
    a = fields.Integer("Enter field A")