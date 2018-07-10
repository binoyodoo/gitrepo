from odoo import models, fields, api, _
from datetime import datetime
from datetime import date


class SaleShipDetails(models.Model):
    _name = 'sale.ship.detail'
    # _rec_name =

    name = fields.Char(string="Ship Name", default=lambda self: _('New'))
    sale_id = fields.Many2one('sale.order', string='Order Reference', ondelete='cascade', index=True,
                              copy=False)
    ship_id = fields.Many2one('sale.ship', string='Ship Reference')

    partner_id = fields.Many2one('res.partner', string='Customer')

    ship_detail_line_ids = fields.One2many('sale.ship.detail.line', 'ship_detail_id', string='Ship Detail Lines')

    product_quantity = fields.Float(compute='_compute_quantity', string="Total Quantity")

    def _compute_quantity(self):
        self.product_quantity=0.0

        for line in self.ship_detail_line_ids:
            self.product_quantity += line.product_qty



    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sale.ship.detail') or _('New')

        return super(SaleShipDetails, self).create(vals)


class SaleShipDetailsLine(models.Model):
    _name = 'sale.ship.detail.line'

    ship_detail_id = fields.Many2one('sale.ship.details', string='Detail Reference')

    product_id = fields.Many2one('product.product', string='Product')

    product_qty = fields.Float(string="Product Quantity")

    ship_id = fields.Many2one('sale.ship', string='Ship')
