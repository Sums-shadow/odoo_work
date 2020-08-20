# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employe(models.Model):
    _inherit='hr.employee'
    
    boutique_id = fields.Many2one('gestion.boutique', string="Boutique")
   