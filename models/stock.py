# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *
import time

class stock(models.Model):
    _name = 'gestion.stock'
    _description = 'gestion.stock'

    # def _retour_date(self):

    #     this_now = datetime.now()
    #     this_date = this_now.strftime('%Y-%m-%d %H:%M:%S')

    #     return this_datesss

    quantite = fields.Char(string="Quantité")
    produit = fields.Many2one('gestion.produit')
    boutique=fields.Many2one('gestion.boutique')
    date_stock= fields.Date('Date de stock', default= datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



    