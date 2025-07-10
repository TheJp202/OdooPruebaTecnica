# -*- coding: utf-8 -*-
{
    "name": "Personalización Factura Número",
    "summary": "Genera número de serie y correlativo en la factura.",
    "description": """
Este módulo concatena las dos primeras secciones del nombre sin separadores y los guarda en un campo como la serie.
También guarda la tercera sección en un campo como el correlativo.
""",
    "author": "Jean Pierre Llamoca Corpus",
    "website": "https://github.com/TheJp202/OdooPruebaTecnica/",
    "category": "Accounting",
    "version": "1.0",

    "depends": ["account", "base"],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'application': False,
    'demo': [],
}

