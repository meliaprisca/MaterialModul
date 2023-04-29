# -*- coding: utf-8 -*-
{
    'name': "Keda Material",

    'summary': """
        keda_material""",

    'description': """
        keda_material
    """,

    'author': "Melia",
    'website': "https://github.com/meliaprisca",

    'category': 'Uncategory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
            'base',
            'website'
            ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/keda_material_data.xml',
        'views/keda_material.xml',
        'views/keda_template.xml',
    ],
}
