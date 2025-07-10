# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAccountNumber(http.Controller):
#     @http.route('/custom_account_number/custom_account_number', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_account_number/custom_account_number/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_account_number.listing', {
#             'root': '/custom_account_number/custom_account_number',
#             'objects': http.request.env['custom_account_number.custom_account_number'].search([]),
#         })

#     @http.route('/custom_account_number/custom_account_number/objects/<model("custom_account_number.custom_account_number"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_account_number.object', {
#             'object': obj
#         })

