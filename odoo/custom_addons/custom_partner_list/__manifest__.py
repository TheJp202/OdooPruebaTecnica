# -*- coding: utf-8 -*-
{
    'name': "custom_partner_list",
    'summary': "Muestra el idioma configurado en la lista de contactos",
    'description': """
Este módulo agrega la visualización de la columna "Idioma" configurado para cada contacto en la vista de lista del modelo res.partner.
Permite al usuario ver rápidamente qué idioma está definido en los contactos desde la vista de lista.
    """,
    'author': "Jean Pierre Llamoca Corpus",
    'website': "https://github.com/TheJp202/OdooPruebaTecnica/",
    'category': 'Contacts',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': False,
    'demo': [],
}

