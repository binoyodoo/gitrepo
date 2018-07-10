from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'ship.wizard'

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date_to")
    print_button = fields.Char(string="Title")

    imo_number = fields.Many2one('sale.ship', string="Imo Number")

    # @api.onchange('date_to')
    # def _date_check(self):
    #     if self.date_from > self.date_to:
    #         dat = self.date_from
    #         self.date_from = self.date_to
    #         self.date_to= dat

    @api.onchange('date_to')
    def _date_check(self):
         if self.date_from > self.date_to:
              self.date_from = self.date_to

    @api.onchange('date_from')
    def _date_checkk(self):
        if self.date_to:

          if self.date_from > self.date_to:
            self.date_to = self.date_from

    # def print_confirm(self):
    #     self.print_button ='Wizard'
