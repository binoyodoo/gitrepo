from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = 'sale.report'

    ship_id = fields.Many2one('sale.ship', ondelete='cascade', string="Ship")

    def _select(self):
        return super(SaleReport, self)._select()+",l.ship_id as ship_id"


    def _group_by(self):
        return super(SaleReport, self)._group_by()+",l.ship_id"
                            

