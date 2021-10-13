# _*_ coding: utf-8 _*_

{
    'name': 'Odoo Academy',
    
    'sumary': """Academy app to manage Training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'autor': 'Odoo',
    
    'website':'http://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['sale','website'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
    ],
    
    'demo':[
       'demo/academy_demo.xml',
    ],
}