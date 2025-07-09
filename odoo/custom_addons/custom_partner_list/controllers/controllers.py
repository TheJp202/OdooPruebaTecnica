# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPartnerList(http.Controller):
#     @http.route('/custom_partner_list/custom_partner_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_partner_list/custom_partner_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_partner_list.listing', {
#             'root': '/custom_partner_list/custom_partner_list',
#             'objects': http.request.env['custom_partner_list.custom_partner_list'].search([]),
#         })

#     @http.route('/custom_partner_list/custom_partner_list/objects/<model("custom_partner_list.custom_partner_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_partner_list.object', {
#             'object': obj
#         })

