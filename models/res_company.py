from odoo import models, api, fields

class ResCompanyInherit(models.Model):
    _inherit = "res.company"

    rtn = fields.Char("RTN")