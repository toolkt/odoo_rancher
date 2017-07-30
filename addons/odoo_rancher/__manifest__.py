# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Odoo Rancher',
    'version' : '1.0',
    'summary': 'Integrating Odoo with Rancher',
    'description': """

    """,
    'category': 'Custom',
    'sequence': 20,
    'website' : 'http://toolkt.com',
    'depends' : ['base'],
    'demo' : [],
    'data' : [
        'views/rancher_view.xml',
    ],
    'test' : [],
    'auto_install': False,
    'installable': True,
}
