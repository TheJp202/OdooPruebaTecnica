# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleChannel(models.Model):
    _name = "sale.channel"
    _description = "Canal de ventas"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(required=True)

class AccountMove(models.Model):
    _inherit = "account.move"

    sale_channel_id = fields.Many2one(
        "sale.channel",
        string="Canal de ventas",
        ondelete="set null",
    )