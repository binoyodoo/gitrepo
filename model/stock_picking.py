from odoo import models, fields, api


class StockPickMove(models.Model):
    _inherit = 'stock.move'

    ship_id = fields.Many2one('sale.ship', string="Ship")

class StockPick(models.Model):
    _inherit = 'stock.picking'

    ship_id = fields.Many2one('sale.ship', string="Ship")

