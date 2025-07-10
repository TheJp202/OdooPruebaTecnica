{
    "name": "Personalización POS Botón",
    "summary": "Añade un botón «Boleta» al PaymentScreen del Punto de Venta y muestra un popup con el total a pagar.",
    "description": """
Este módulo inserta un nuevo botón «Boleta» en la parte derecha del PaymentScreen. Al hacer clic, aparece una ventana emergente que informa el monto total de la orden. 
El botón sólo existe en esa pantalla; no afecta otros flujos.
""",
    "author": "Jean Pierre Llamoca Corpus",
    "website": "https://github.com/TheJp202/OdooPruebaTecnica/",
    "category": "Sales",
    "version": "1.0",

    "depends": ["point_of_sale"],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    "assets": {
        "point_of_sale._assets_pos": [
            "custom_pos_button/static/src/js/payment_boleta_button.js",
            "custom_pos_button/static/src/xml/payment_boleta_button.xml",
        ],
    },

    'installable': True,
    'application': False,
    'demo': [],
}

