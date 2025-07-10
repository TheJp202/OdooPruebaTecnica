{
    "name": "Personalización Factura QR",
    "summary": "Añade un código QR al PDF de la factura",
    "description": """
Este modulo inserta un código QR en el PDF de la factura generada.
El QR se forma con: Número|Cliente|Fecha|TotalCantidades|TotalAPagar
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


