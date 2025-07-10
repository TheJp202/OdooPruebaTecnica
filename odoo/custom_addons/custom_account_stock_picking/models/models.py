# -*- coding: utf-8 -*-

from odoo import fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    picking_ids = fields.Many2many(
        comodel_name="stock.picking",
        string="Transferencias relacionadas",
        compute="_compute_picking_ids",
        store=False,
    )

    def _compute_picking_ids(self):
        for move in self:
            sale_orders = move.invoice_line_ids.mapped(
                "sale_line_ids.order_id"
            )
            move.picking_ids = sale_orders.mapped("picking_ids")