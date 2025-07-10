# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPosButton(http.Controller):
#     @http.route('/custom_pos_button/custom_pos_button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_pos_button/custom_pos_button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_pos_button.listing', {
#             'root': '/custom_pos_button/custom_pos_button',
#             'objects': http.request.env['custom_pos_button.custom_pos_button'].search([]),
#         })

#     @http.route('/custom_pos_button/custom_pos_button/objects/<model("custom_pos_button.custom_pos_button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_pos_button.object', {
#             'object': obj
#         })

