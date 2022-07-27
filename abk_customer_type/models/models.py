# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abk_customer_type(models.Model):
    _name = 'abk.customer.type'
    _description = 'Customer Type'

    name = fields.Char()
    description = fields.Text()
