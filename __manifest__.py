# -*- coding: utf-8 -*-
{
    'name': "College Management",

    'summary': """
       College Management contains student, faculty and college activities""",

    'description': """
        This module is used to maintain college activities
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/faculty_views.xml',
        'views/report_views.xml',
        'views/templates.xml',
        'views/fee_view.xml',
        'views/course_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}