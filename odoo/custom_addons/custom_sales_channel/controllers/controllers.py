# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSalesChannel(http.Controller):
#     @http.route('/custom_sales_channel/custom_sales_channel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sales_channel/custom_sales_channel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sales_channel.listing', {
#             'root': '/custom_sales_channel/custom_sales_channel',
#             'objects': http.request.env['custom_sales_channel.custom_sales_channel'].search([]),
#         })

#     @http.route('/custom_sales_channel/custom_sales_channel/objects/<model("custom_sales_channel.custom_sales_channel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sales_channel.object', {
#             'object': obj
#         })

