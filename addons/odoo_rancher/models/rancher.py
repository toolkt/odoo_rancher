# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _




class OdooRancherTest(models.Model):
    _name = 'odoo.rancher.test'

    name = fields.Char("Name")
