# -*- coding: utf-8 -*-

from odoo import api, fields, models
import qrcode, io, base64

class AccountMove(models.Model):
    _inherit = "account.move"

    x_total_qty_lines = fields.Float(
        string="Total Cantidades de línea",
        compute="_compute_total_qty_lines",
        store=True,
    )
    x_qr_invoice = fields.Binary(
        string="QR de Factura",
        compute="_compute_qr_invoice",
        store=True,
    )

    @api.depends("invoice_line_ids.quantity")
    def _compute_total_qty_lines(self):
        for move in self:
            move.x_total_qty_lines = sum(move.invoice_line_ids.mapped("quantity"))

    @api.depends(
        "name",
        "invoice_date",
        "partner_id.name",
        "x_total_qty_lines",
        "amount_total",
    )
    def _compute_qr_invoice(self):
        for move in self:
            if move.move_type not in ("out_invoice", "out_refund"):
                move.x_qr_invoice = False
                continue
            qr_string = (
                f"{move.name or ''}|"
                f"{move.partner_id.name or ''}|"
                f"{move.invoice_date or ''}|"
                f"{move.x_total_qty_lines:.2f}|"
                f"{move.amount_total:.2f}"
            )
            move.x_qr_invoice = self._generate_qr_code(qr_string)

    @staticmethod
    def _generate_qr_code(qr_string):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(qr_string)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue())
