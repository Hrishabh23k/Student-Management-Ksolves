{
    'name': 'School Management',

    'summary': """ School Management Software""",

    'author': "Hrishabh Nagar",

    'category': 'Human Resources',

    'version': '16.0.1.0.0',
    'depends': ['base'],

    'data':[
        'security/ir.model.access.csv',
        'views/school.xml',
        'views/teacher.xml',
    ],

    'installable':True,
    'application':True,
    'auto_install':False
}