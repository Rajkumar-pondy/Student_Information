from odoo import models, fields, api
import datetime

class student_faculty(models.Model):
    _name = 'student.faculty'
    _description="Faculty Information"
    _sql_constraints = [('faculty_code','unique(faculty_code)', 'Faculty code must be unique')]
    _rec_name='faculty_name'
    
    faculty_code= fields.Char("Faculty Id",required=True)
    faculty_name= fields.Char("Faculty Name",separator=",")
    email = fields.Char('Email')
    contact = fields.Char('Contact Number')
    dob = fields.Date('Date of Birth')
    image = fields.Binary('Image',store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    age = fields.Integer('Age', compute='_staff_age_calculate',store=True)
    department = fields.Char("Department Name")
    salary= fields.Float("Salary")
    
    student_count=fields.Integer(string='Student count',compute='compute_student_counts')
#     course_count=fields.Integer(string='Course count',compute='compute_course_count')
    
    faculty_student_ids=fields.Many2many('student.details',string="Students Handling")
    
    faculty_course_ids=fields.Many2many('student.course',string='Courses Taken')
    
    report_faculty_ids= fields.One2many('student.report','faculty_report_id')

    

    @api.multi
    def compute_student_counts(self):
            action = {
                      'name': 'Student Details',
                      'type': 'ir.actions.act_window',
                      'res_model': 'student.details',
                      'target': 'current',
                     }
            self.ensure_one()
#             students=self.mapped('faculty_student_ids')
            students=self.faculty_student_ids
            self.student_count=len(students)
            if self.student_count>1:
                action['domain'] = [('id', 'in', students.ids)]
                action['view_mode'] = 'tree,form'
                return action
            else:
                action['views'] = [(self.env.ref('student_information.student_form_view').id, 'form')]
                action['res_id'] = students.id
                return action
           
          
#     @api.multi
#     def compute_course_count(self):
#         for rec in self:
#             rec.course_code = self.env['student.course'].search_count([])
#             rec.course_count=rec.course_code
#             action = {
#              'name': 'Student Course Details',
#              'type': 'ir.actions.act_window',
#              'res_model': 'student.course',
#              'target': 'current',
#              }
#             rec.ensure_one()
#             courses=self.mapped('faculty_course_ids')
#             if len(courses)>1:
#                 action['domain']=[('id','in','courses.ids')]
#                 action['view-mode']='tree'
#                 return action
#             elif courses:
#                 action['views']=[(self.env.ref('student_information.course_form_view').id,'form')]
#                 action['res_id']=courses.id
#                 return action
     
    @api.depends('dob')
    def _staff_age_calculate(self):
        if self.dob:
            current_year=datetime.datetime.now().year
            birth_year=self.dob.year
            self.age=current_year-birth_year
            

        
        
        
        
        
        
        
        