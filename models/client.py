# -*- coding: utf-8 -*-

from odoo import models, fields, api


class client(models.Model):
    _name='gestion.client'
    _inherits={'res.partner':'partner_id'}


    partner_id = fields.Many2one('res.partner', 'partner_id' , required=True, ondelete='cascade')
    sexe=fields.Selection([('homme','Homme'),('femme','Femme')], string="Sexe")
   