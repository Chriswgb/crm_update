from odoo import api, models, modules, fields

class References(models.Model):
    _name = "references"
    _order = "sequence, id"

    name = fields.Char("Referencia")
    sequence = fields.Integer('Sequence', default=1)