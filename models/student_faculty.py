from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError

class student_faculty(models.Model):
    _name = 'student.faculty'
    _description="Faculty Information"
    _sql_constraints = [('faculty_code','unique(faculty_code)', 'Faculty code must be unique')]
    _rec_name='faculty_name'
    
    faculty_code= fields.Char("Faculty Id",required=True,copy=False,default='New')
    faculty_name= fields.Char("Faculty Name",separator=",")
    email = fields.Char('Email')
    contact = fields.Char('Contact Number')
    dob = fields.Date('Date of Birth')
    image = fields.Binary('Image',store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    age = fields.Integer('Age', compute='_staff_age_calculate',store=True)
    department = fields.Char("Department Name")
    salary= fields.Float("Salary",digits=(9, 2)) 
    edit_ok=fields.Boolean("Can be edit",default=True)
    resource_calendar_id=fields.Many2one('resource.calendar',string="Working Hours",help="Faculty working hours")
    color_field=fields.Char()
    
    student_count=fields.Integer(string='Student count',compute='compute_student_counts')

    faculty_student_ids=fields.Many2many('student.details',string="Students Handling")
    faculty_course_ids=fields.Many2many('student.course',string='Courses Taken')
    report_faculty_ids= fields.One2many('student.report','faculty_report_id')
    
    @api.depends('dob')
    def _staff_age_calculate(self):
        if self.dob:
            current_year=datetime.datetime.now().year
            birth_year=self.dob.year
            self.age=current_year-birth_year
    
    def compute_student_counts(self):
            action = {
                      'name': 'Student Details',
                      'type': 'ir.actions.act_window',
                      'res_model': 'student.details',
                      'target': 'current',
                     }
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
    @api.model
    def create(self,vals):
         if vals.get('faculty_code','New')=='New':
             vals['faculty_code'] = self.env['ir.sequence'].next_by_code('student.faculty') or '/'
         return super(student_faculty, self).create(vals)