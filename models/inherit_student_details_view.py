# -*- coding: utf-8 -*-
from odoo import models, fields, api

class student_details(models.Model):
    _inherit='student.details'
    
    
    father_name=fields.Char('Father Name')