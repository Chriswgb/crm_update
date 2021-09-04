# -*- coding: utf-8 -*-
{
    'name': "CRM update",
    "author": "Feacteam",
    'summary': '', 
    'description': """
        
    """,          
    'version': '1.1',
    'depends': ['base','contacts','mail','crm'],
    'data': [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/res_partner.xml",
        "views/departments.xml",
        'views/references.xml',
        "views/crm_lead.xml",
        "views/activities.xml",
        "views/menus.xml",
        "views/res_company.xml"
    ],
    'application': True,
}

