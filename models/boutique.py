# -*- coding: utf-8 -*-

from odoo import models, fields, api


class boutique(models.Model):
    _name = 'gestion.boutique'
    _description = 'gestion.boutique'

    name = fields.Char(string="Nom")
    adresse = fields.Char(string="Adresse")
    
