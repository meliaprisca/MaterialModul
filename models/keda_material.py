from odoo import models, fields, api, _
from odoo.exceptions import UserError

class KedaMaterial(models.Model):
    _name = 'keda.material'

    name = fields.Char(string='Name', required=True, )
    code = fields.Char(string='Code', required=True, )
    type = fields.Selection([
        ('fabric','Fabric'),
        ('cotton','Cotton'),
        ('jeans','Jeans'),
        ], string='Type', required=True, )
    buy_price = fields.Float(string='Buy Price', required=True)
    supplier = fields.Many2one('res.company','Supplier', required=True, default=lambda self: self.env.company)

    _sql_constraints = [
        ('code_material_uniq', 'unique (code)', 'The code of the material must be unique !')
    ]

    @api.constrains('buy_price')
    def _constrains_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise UserError(_('Buy price cannot less than 100'))
