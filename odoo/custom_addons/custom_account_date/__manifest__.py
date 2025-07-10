# -*- coding: utf-8 -*-
{
    "name": "Personalización Factura Fecha",
    "summary": "Agrega fecha y hora de emisión.",
    "description": """
Este módulo implementa un campo que maneja fecha y hora de la emisión de la factura, reemplazando al campo nativo de fecha de la factura.
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
