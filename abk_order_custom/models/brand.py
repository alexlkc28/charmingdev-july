# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ABKBrand(models.Model):
    _name = 'abk.brand'
    _description = 'Brand'
    _order = "sequence, name, id"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)
