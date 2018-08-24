# -*- coding: utf-8 -*-

from odoo import models, fields


class Product(models.Model):
    _inherit = 'product.template'

    link = fields.One2many(comodel_name='uplevo.link', inverse_name='product_id', string='Link Drive')