# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': "mail_multi_domain",
    'summary': "Multi-domain management in Odoo",
    'description': """
        Long description of module's purpose
    """,
    'author': "Subteno IT",
    'website': "https://www.subteno-it.com",
    'category': 'Discuss',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ir_mail_server.xml',
        'views/res_company.xml',
        'views/mail_user_alias.xml',
        'views/res_users.xml',
        'data/base.xml',
    ],
}