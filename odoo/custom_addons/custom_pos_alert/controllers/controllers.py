# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPosAlert(http.Controller):
#     @http.route('/custom_pos_alert/custom_pos_alert', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_pos_alert/custom_pos_alert/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_pos_alert.listing', {
#             'root': '/custom_pos_alert/custom_pos_alert',
#             'objects': http.request.env['custom_pos_alert.custom_pos_alert'].search([]),
#         })

#     @http.route('/custom_pos_alert/custom_pos_alert/objects/<model("custom_pos_alert.custom_pos_alert"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_pos_alert.object', {
#             'object': obj
#         })

