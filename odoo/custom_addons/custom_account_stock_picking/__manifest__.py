# -*- coding: utf-8 -*-
{
    "name": "Personalización Factura Transferencias",
    "summary": "Añade un campo para ver transferencias",
    "description": """
Este modulo implementar un campo para poder visualizar las transferencias relacionadas con el pedido de venta.
""",
    "author": "Jean Pierre Llamoca Corpus",
    "website": "https://github.com/TheJp202/OdooPruebaTecnica/",
    "category": "Accounting",
    "version": "1.0",

    "depends": ["account", "sale_management", "stock"],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'application': False,
    'demo': [],
}


