# -*- coding: utf-8 -*-
{
    'name': "Canales de Ventas",
    "summary": "Agrega el modelo Canales de Ventas",
    "description": """
Este múdlo crea el modelo de Canales de Ventas con la lista de canales.
Además, añade el campo «Canal de Ventas» en la factura.
""",
    "author": "Jean Pierre Llamoca Corpus",
    "website": "https://github.com/TheJp202/OdooPruebaTecnica/",
    "category": "Accounting",
    "version": "1.0",

    "depends": ["account", "base"],

    'data': [
        'security/ir.model.access.csv',
        'data/sales_channel_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'application': False,
    'demo': [],
}


