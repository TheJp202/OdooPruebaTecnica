# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAccountStockPicking(http.Controller):
#     @http.route('/custom_account_stock_picking/custom_account_stock_picking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_account_stock_picking/custom_account_stock_picking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_account_stock_picking.listing', {
#             'root': '/custom_account_stock_picking/custom_account_stock_picking',
#             'objects': http.request.env['custom_account_stock_picking.custom_account_stock_picking'].search([]),
#         })

#     @http.route('/custom_account_stock_picking/custom_account_stock_picking/objects/<model("custom_account_stock_picking.custom_account_stock_picking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_account_stock_picking.object', {
#             'object': obj
#         })

