from odoo import models, fields, api

class student_report(models.Model):
    _name = 'student.report'
    _description="Student Report card"
    _sql_constraints = [('report_code','unique(report_code)', 'Report code must be unique')]

    report_code=fields.Char("Report Id",required=True,copy=False,default='New')
    report_card_terms=fields.Char("Semester No")
    result=fields.Char("Result")
    grade=fields.Char("Grade")

    student_report_id = fields.Many2one('student.details',string="Name Student",delegate=True,required=True)
    faculty_report_id=fields.Many2one('student.faculty', string="Faculty Name")

    @api.model
    def create(self, vals):
        if vals.get('report_code','New')=='New':
            vals['report_code']=self.env['ir.sequence'].next_by_code('student.report') or '/'
        return super(student_report,self).create(vals)
