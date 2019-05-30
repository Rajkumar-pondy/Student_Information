from odoo import models, fields, api

class student_report(models.Model):
    _name = 'student.report'
    _description="Student Report card"
    _sql_constraints = [('report_code','unique(report_code)', 'Report code must be unique')]
    
    report_code=fields.Char("Report Id")
    report_card_terms=fields.Char("Semester No")
    result=fields.Char("Result")
    grade=fields.Char("Grade")
    
    student_id_report = fields.Many2one('student.details', string="Student Id",delegate=True,required=True)
    
    faculty_report_id=fields.Many2one('student.faculty', string="Faculty Name",ondelete='restrict')
    
#     @api.multi
#     def name_get(self):
#         result= []
#         for record in self:
#             rec_name="%s %s" % (record.student_name, record.department)
#             result.append((record.id, rec_name))
#         return result
#     
#    
