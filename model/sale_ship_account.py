from odoo import models, fields, api


class SalAccountInvoice(models.Model):
    _inherit = 'account.invoice.line'

    ship_id = fields.Many2one('sale.ship', ondelete='cascade', string="Ship")

# class SaleOrderLineInvoice(models.TransientModel):
#     _inherit = 'sale.order.line'

    # @api.multi
    # def prepare_invoice_line(self):
    #     super(SaleOrderLineInvoice, self).prepare_invoice_line()
    #
    #     res={'sale_ship_id':}











