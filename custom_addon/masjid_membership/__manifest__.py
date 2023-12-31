# -*- coding: utf-8 -*-
{
    'name': "Masjid Membership",
    'icon': '/masjid_membership/static/description/icon.png',
    'application': True,
    'sequence': 1,
    'summary': """
        A module to add masjid's membership details.
    """,

    'description': """
        A module to add masjid's membership details.
    """,

    'author': "Akbar Ali",
    'website': "https://www.codequbes.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'member',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/detailedView.xml',
        'views/listView.xml',
        'views/actions.xml',
        'views/menus.xml',
    ],
}
