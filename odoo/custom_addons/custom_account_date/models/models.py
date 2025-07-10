from odoo import api, fields, models
from datetime import datetime as dt

class AccountMove(models.Model):
    _inherit = "account.move"

    x_emission_datetime = fields.Datetime(
        string="Fecha de emisión",
        copy=False,
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("invoice_date") and not vals.get("x_emission_datetime"):
                vals["x_emission_datetime"] = vals["invoice_date"] + " 00:00:00"
            elif vals.get("x_emission_datetime") and not vals.get("invoice_date"):
                vals["invoice_date"] = vals["x_emission_datetime"].split(" ")[0]
        return super().create(vals_list)

    def write(self, vals):
        if "x_emission_datetime" in vals:
            vals["invoice_date"] = vals["x_emission_datetime"].split(" ")[0]
        return super().write(vals)