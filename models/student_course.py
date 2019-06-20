from odoo import models, fields, api

class student_course(models.Model):
    _name='student.course'
    _inherit='mail.thread'
    _description="Student Course Details"
    
    
    course_code=fields.Char("Course Id",required=True,track_visibility='onchange')
    #Relation Fields
    course_stu_id=fields.Many2one('student.details',string="Student name",delegate=True,required=True)

    fee_course_ids=fields.One2many('student.fee','course_fee_id',string="Fee course ids")

    @api.multi
    def name_get(self):
        context={}
        res=[]
        for record in self:
            if context.get('course_special_name',False):
                res.append((record.id,record.course_code))
            else:
                res.append((record.id, "%s" % (record.course_code)))
        return res
