from odoo import models, fields, api
from datetime import datetime
from datetime import date


class Saleship(models.Model):
    _name = 'sale.ship'
    _rec_name = 'imo_no'

    name = fields.Char(string="Title", required=True, states={'sale': [('readonly', True)]})
    imo_no = fields.Integer(string="imo.no", states={'sale': [('readonly', True)]})
    man_date = fields.Date(string="man.date", required=True, states={'sale': [('readonly', True)]})
    yard_no = fields.Integer(string="yard.no", states={'sale': [('readonly', True)]})

    ship_age = fields.Integer(string="Age computing")

    man_cost = fields.Float(string="manufacturing Cost", states={'sale': [('readonly', True)]})
    shipng_cost = fields.Float(string="shipping cost", states={'sale': [('readonly', True)]})
    misc_cost = fields.Float(string="miscellaneous cost", states={'sale': [('readonly', True)]})
    serv_cost = fields.Float(string="service cost", states={'sale': [('readonly', True)]})

    tot_cost = fields.Char(compute='_compute_total', string="Total computing")

    # def _compute_total(self):
    #     for record in self:
    #        record.tot_cost=record.man_cost + record.shipng_cost + record.misc_cost + record.serv_cost

    @api.onchange('man_date')
    def _compute_age(self):
        cur_date = date.today()
        cu_da = str(cur_date)
        dt = datetime.strptime(cu_da, '%Y-%m-%d')

        dtm = str(self.man_date)
        dtmm = datetime.strptime(dtm, '%Y-%m-%d')

        yr = 12 * (dt.year - dtmm.year)
        mnt = abs(dt.month - dtmm.month)

        self.ship_age = yr + mnt

    def _compute_total(self):
        self.tot_cost = self.man_cost + self.shipng_cost + self.misc_cost + self.serv_cost

    _sql_constraints = [('imo_no_unique', 'unique(imo_no)', 'Number IMO should be unique')]

    def _check_name(self):
        for val in self.read(['name']):
            if val['name']:
                if len(val['name']) < 6:
                    return False
        return True

    _constraints = [
        (_check_name, 'Name must have at least 6 characters.', ['name'])
    ]

    state = fields.Selection([
        ('draft', 'sale'),
        ('sent', 'confirm'),
        ('sale', 'cancelled'),

    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    def action_confirm(self):
        return self.write({'state': 'sent'})

    def action_cancel(self):
        return self.write({'state': 'sale'})
