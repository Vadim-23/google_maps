# -*- coding: utf-8 -*-
{
    'name': 'ENDO color cell',
    'category': 'Hidden/Tools',
    'description': """""",
    'author': 'iLLya Vayner',
    'maintainer': 'Collabor Digital',
    'depends': [
        # 'base_endo',
        'web',
    ],
    'data': [
        'views/hr_expense.xml'

    ],
    'assets': {
        'web.assets_backend': [
            'endo_color_cell/static/src/js/tree_button.js',
        ],
        'web.assets_qweb': [
            'endo_color_cell/static/src/xml/tree_button.xml',
        ]
    },


    'license': 'LGPL-3',
}
