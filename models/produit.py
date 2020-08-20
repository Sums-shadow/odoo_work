# -*- coding: utf-8 -*-

from odoo import models, fields, api


class produit(models.Model):
    _name = 'gestion.produit'
    _description = 'gestion.produit'

    name = fields.Char(string="Libelle")
    categorie = fields.Many2one('gestion.categorie')
    prix_unitaire=fields.Float('Prix Unitaire')



class categorie(models.Model):
    _name = 'gestion.categorie'
    _description = 'gestion.categorie'

    name = fields.Char(string="Categorie")
    
