from odoo import models, fields, api
class student_fee(models.Model):
    _name='student.fee'
    _description="Student Fee Structure"
    _rec_name="fee_code"
#     _sql_constraints = [('fee_code','unique(fee_code)', 'Student Fee code must be unique')]
    
    fee_code=fields.Char("Fee Receipt Id",required=True,copy=False,default='New')
    semester_no=fields.Char("Semester No")
    tution_fee=fields.Float(string="Tuition Fee",group_operator="sum")
    exam_fee=fields.Float(string="Exam Fee")
    total_fee=fields.Float(string="Total Fee")
    currency_id =fields.Many2one('res.currency',help="Currency for tution fee",required=True)
    
    #Relational Fields
    fee_stu_id=fields.Many2one('student.details',string="Name Student",delegate=True,required=True)
    course_fee_id=fields.Many2one('student.course',string="Course code")
    
    @api.multi
    def name_get(self):
        context={}
        res=[]
        for record in self:
            if context.get('fee_display_name',False):
                res.append((record.id,record.fee_code))
            else:
                res.append((record.id, '%s,%s' %(record.fee_code,record.semester_no)))
        return res 
    
    @api.model
    def create(self,vals):
        if vals.get('fee_code','New')=='New':
             vals['fee_code'] = self.env['ir.sequence'].next_by_code('student.fee') or '/'
        return super(student_fee, self).create(vals)
    
    @api.onchange('tution_fee','exam_fee')
    def on_change_fee(self):
        if self.tution_fee and self.exam_fee:
                self.total_fee= self.tution_fee + self.exam_fee