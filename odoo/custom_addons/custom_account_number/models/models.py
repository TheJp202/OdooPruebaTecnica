# -*- coding: utf-8 -*-

import re
from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    x_invoice_serie = fields.Char(
        string="Número de serie",
        compute="_compute_invoice_serie_correlative",
        store=True,
    )
    x_invoice_correlative = fields.Char(
        string="Número correlativo",
        compute="_compute_invoice_serie_correlative",
        store=True,
    )

    @api.depends("name")
    def _compute_invoice_serie_correlative(self):
        for move in self:
            serie = correlativo = False
            if move.name:
                # Split por / ó - (por si la secuencia usa guiones)
                parts = re.split(r"[/-]", move.name)
                if len(parts) >= 3:
                    serie = f"{parts[0]}{parts[1]}"
                    correlativo = parts[2].zfill(8)
            move.x_invoice_serie = serie
            move.x_invoice_correlative = correlativo
