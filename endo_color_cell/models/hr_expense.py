from odoo import api, fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    color_integer = fields.Integer(default=0, compute='_compute_color', store=True)

    @api.depends('active')
    def _compute_color(self):
        for record in self:
            if record.active:
                record.color_integer = 0
            else:
                record.color_integer = -1
