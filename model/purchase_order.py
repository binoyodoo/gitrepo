from odoo import models, fields, api



class PurchaseOrd(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order")

    # print(purchase_order_id)