from odoo import models, fields, api

class student_report(models.Model):
    _name = 'student.report'
    _description="Student Report card"
    _inherit='student.details'
    _sql_constraints = [('report_code','unique(report_code)', 'Report code must be unique')]
    
    student_name=fields.Char("Student Name")
    report_code=fields.Char("Report Id")
    report_card_terms=fields.Char("Semester No")
    result=fields.Char("Result")
    grade=fields.Char("Grade")
    
    report_student_id = fields.Many2one('student.details', string="Student Id")
    
    faculty_report_id=fields.Many2one('student.faculty', string="Faculty Id", required=True, ondelete='restrict')
