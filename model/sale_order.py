from odoo import models, fields, api


class SalOrdI(models.Model):
    _inherit = 'sale.order'

    ship_id = fields.Many2one('sale.ship', ondelete='cascade', string="Ship", states={'sale': [('readonly', True)]})

    purchase_ids = fields.One2many(
        'purchase.order', 'sale_order_id', string="Purchase")

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ('ship', 'Ship confirm'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    @api.multi
    def confirm_ship(self):
        self.write({'state': 'ship'})

        ship_details_obj = self.env['sale.ship.detail']

        ship_detail_line_obj = self.env['sale.ship.detail.line']

        for order in self:
            dicti = {}
            for line in order.order_line:
                #
                # if    in dicti.keys()

                print(line.ship_id.imo_no)
                print(dicti)
                # print(dicti[line.ship_id.imo_no])

                if line.ship_id.imo_no in dicti.keys():
                    ship_detail_line_obj.create({
                        'product_id': line.product_id.id,
                        'ship_id': line.ship_id.id,
                        'product_qty': line.product_uom_qty,
                        'ship_detail_id': dicti[line.ship_id.imo_no]})


                else:
                    ship_det = ship_details_obj.create({'ship_id': line.ship_id.id,
                                                        'partner_id': order.partner_id.id,
                                                        'sale_id': order.id})
                    res = ship_detail_line_obj.create({
                        'product_id': line.product_id.id,
                        'product_qty': line.product_uom_qty,
                        'ship_id': line.ship_id.id,
                        'ship_detail_id': ship_det.id})

                dicti[line.ship_id.imo_no] = ship_det.id


        # self.state='ship'

    # order_line is a one2many field in sale.order model to the sale.order.line model

    # order_line = fields.One2many('sale.order.line')

    # so if you add an item in sale.order.line model  a change in order_line occurs , hence we can use it in onchange

    @api.onchange('ship_id', 'order_line')
    def _onchange_shipid(self):
        if self.ship_id:
            for line in self.order_line:
                line.ship_id = self.ship_id.id

    @api.multi
    def action_confirm(self):
        super(SalOrdI, self).action_confirm()

        for line in self.order_line:
            for lines in line.move_ids:
                lines.ship_id = line.ship_id

        for record in self.picking_ids:
            record.ship_id = self.ship_id


class SaleOrdLine(models.Model):
    _inherit = 'sale.order.line'

    ship_id = fields.Many2one('sale.ship', ondelete='cascade',
                              string="SaleOrLine", states={'sale': [('readonly', True)]})

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrdLine, self)._prepare_invoice_line(qty)
        print("abc")
        res['ship_id'] = self.ship_id.id

        return res
