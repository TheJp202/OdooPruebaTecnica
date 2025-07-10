# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAccountDate(http.Controller):
#     @http.route('/custom_account_date/custom_account_date', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_account_date/custom_account_date/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_account_date.listing', {
#             'root': '/custom_account_date/custom_account_date',
#             'objects': http.request.env['custom_account_date.custom_account_date'].search([]),
#         })

#     @http.route('/custom_account_date/custom_account_date/objects/<model("custom_account_date.custom_account_date"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_account_date.object', {
#             'object': obj
#         })

