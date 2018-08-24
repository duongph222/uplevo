# -*- coding: utf-8 -*-

from odoo import models, fields


class Link(models.Model):
    _name = 'uplevo.link'

    name = fields.Char('Name')
    link = fields.Char('Link')
    product_id = fields.Many2one(comodel_name='product.template', string='Product')