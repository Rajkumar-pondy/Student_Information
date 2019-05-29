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
    fee_stu_id=fields.Many2one('student.details',string="Student Id ",ondelete='restrict')
    
#     student_name = fields.Char('Student Name')
#     student_code=fields.Integer("Student Id")
#     lab_fee=fields.Float("Lab Fee")
#     library_fee=fields.Float("Lib Fee")
#     development_fee=fields.Float("Develop. Fee")
#     hostel_fee=fields.Float("Hostel Fee")
#     mess_fee=fields.Float("Mess Fee")
#     total_amount=fields.Float("Total Amount",compute="cal_total",store=True)
#     
#     @api.one
#     def cal_total(self):
#         self.total_amount=self.tution_fee + self.lab_fee + self.library_fee + self.development_fee + self.hostel_fee + self.mess_fee
#         print(self.total_amount)
