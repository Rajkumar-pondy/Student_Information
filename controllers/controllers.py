# -*- coding: utf-8 -*-
from odoo import http

# class StudentInformation(http.Controller):
#     @http.route('/student_information/student_information/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/student_information/student_information/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('student_information.listing', {
#             'root': '/student_information/student_information',
#             'objects': http.request.env['student_information.student_information'].search([]),
#         })

#     @http.route('/student_information/student_information/objects/<model("student_information.student_information"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student_information.object', {
#             'object': obj
#         })