# -*- coding: utf-8 -*-
{
    'name': "custom_pos_alert",
    'summary': "Muestra una alerta cuando se selecciona un producto con precio S/ 0.00 en el Punto de Venta",
    'description': """
Este módulo agrega una validación al Punto de Venta (POS) de Odoo.
Cuando un usuario selecciona un producto cuyo precio es S/ 0.00, se muestra una alerta en pantalla notificando al cajero o vendedor sobre el precio cero.
Útil para evitar ventas accidentales de productos sin precio.
    """,
    'author': "Jean Pierre Llamoca Corpus",
    'website': "https://github.com/TheJp202/OdooPruebaTecnica/",
    'category': 'Sales',
    'version': '1.0',

    'depends': ['point_of_sale'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'custom_pos_alert/static/src/js/pos_zero_price_alert.js',
        ],
    },
    'installable': True,
    'application': False,
    'demo': [],
}