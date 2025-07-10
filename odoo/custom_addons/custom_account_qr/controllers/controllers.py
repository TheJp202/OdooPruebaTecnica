# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAccountQr(http.Controller):
#     @http.route('/custom_account_qr/custom_account_qr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_account_qr/custom_account_qr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_account_qr.listing', {
#             'root': '/custom_account_qr/custom_account_qr',
#             'objects': http.request.env['custom_account_qr.custom_account_qr'].search([]),
#         })

#     @http.route('/custom_account_qr/custom_account_qr/objects/<model("custom_account_qr.custom_account_qr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_account_qr.object', {
#             'object': obj
#         })

