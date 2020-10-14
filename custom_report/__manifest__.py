# -*- coding: utf-8 -*-
{
    'name': "custom_report",

    'summary': """
        custom airway bill""",

    'description': """
        custom airway bill
    """,

    'depends': ['sale_stock', 'account', 'point_of_sale'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    "qweb" : [
        'static/src/xml/pos.xml',
    ],
}
