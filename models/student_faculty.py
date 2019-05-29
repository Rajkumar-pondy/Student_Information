from odoo import models, fields, api
import datetime

class student_faculty(models.Model):
    _name = 'student.faculty'
    _description="Faculty Information"
    _sql_constraints = [('faculty_code','unique(faculty_code)', 'Faculty code must be unique')]
    _rec_name='faculty_name'
    
    faculty_code= fields.Char("Faculty Id",required=True)
    faculty_name= fields.Char("Faculty Name")
    email = fields.Char('Email')
    contact = fields.Char('Contact Number')
    dob = fields.Date('Date of Birth')
    image = fields.Binary('Image',store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    age = fields.Integer('Age', compute='_staff_age_calculate',store=True)
    department = fields.Char("Department Name")
    salary= fields.Float("Salary")
    
    student_count=fields.Integer(string='Student count',compute='compute_student_counts')
    course_count=fields.Integer(string='Course count',compute='compute_course_count')
    
    faculty_student_ids=fields.Many2many('student.details','student_name',string="Students Handling")
    
    faculty_course_ids=fields.Many2many('student.course',string='Courses Taken')
    
    report_faculty_ids= fields.One2many('student.report','faculty_report_id')

    

    @api.multi
    def compute_student_counts(self):
        for rec in self:
            rec.student_code = self.env['student.details'].search([])
            rec.student_count = len(rec.student_code)
            print(rec.student_count)
            action = {
             'name': 'Student Details',
             'type': 'ir.actions.act_window',
             'res_model': 'student.details',
             'target': 'current',
             }
            if rec.student_count == 1:
                #student_code = student_code[0]
#                 action['res_id'] = student_count
                action['view_mode'] = 'form'
                action['views'] = [(self.env.ref('student_information.student_form_view').id, 'form')]
            else:
                action['view_mode'] = 'tree,form'
#                 action['domain'] = [('id', 'in', student_tree_view)]
                return action
    @api.multi
    def compute_course_count(self):
        for rec in self:
            rec.course_code = self.env['student.course'].search([])
            rec.course_count=len(rec.course_code)
            action = {
             'name': 'Student Course Details',
             'type': 'ir.actions.act_window',
             'res_model': 'student.course',
             'target': 'current',
             }
            if rec.course_count == 1:
                action['view_mode'] = 'form'
                action['views'] = [(self.env.ref('student_information.course_form_view').id, 'form')]
            else:
                action['view_mode'] = 'tree,form'
                return action
     
    @api.depends('dob')
    def _staff_age_calculate(self):
        if self.dob:
            current_year=datetime.datetime.now().year
            birth_year=self.dob.year
            self.age=current_year-birth_year