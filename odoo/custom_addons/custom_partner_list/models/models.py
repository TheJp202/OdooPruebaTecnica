# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_partner_list(models.Model):
#     _name = 'custom_partner_list.custom_partner_list'
#     _description = 'custom_partner_list.custom_partner_list'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

