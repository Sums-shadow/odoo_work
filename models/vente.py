# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *
import time
from odoo.exceptions import UserError

class vente(models.Model):
    _name = 'gestion.vente'
    _description = 'gestion.vente'

    def _getEmploye(self):
        employe_ids=self.env['hr.employee'].search([('user_id','=',self.env.user.id)])
        if not employe_ids:
            raise UserError(_('ce compte n est pas lié à un utilisteur'))
        else:
            return employe_ids.id



    client_id = fields.Many2one('gestion.client')
    lignevente_ids=fields.One2many('gestion.lignevente', 'vente_id', string='ligne de vente')
    date_vendue=fields.Date('Date de la vente', default= datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    employe_id=fields.Many2one('hr.employee', default=_getEmploye, readonly=True)
    total=fields.Float('Total')

    @api.depends('lignevente_ids')
    def _ligne_depend(self):
        somme=0.0
        if self.lignevente_ids:
            for ligne in self.lignevente_ids:
                somme=somme+(ligne.quantite*ligne.prix)

        self.total=somme
    
    # boutique_id=fields.Many2one('gestion.boutique', readonly=True)

    # @api.onchange('employe_id')
    # def onChangeEmploye(self):

    #     if not self.employe_id:
    #         return True
        
    #     self.boutique_id=self.employe_id.boutique_id.id

    # @api.depends('lignevente_ids')
    # def onDepend(self):
    #     somme=0.0
    #     for lignevente_id in self.lignevente_ids:
    #         somme+=lignevente_id.quantite * lignevente_id.prix
        
    #     self.total=somme

    # def create (self, vals):
        
    #     for ligne in vals.get('lignevente_ids'):

    #         produit_id=ligne[2].get['produit_id']
    #         quantite=ligne[2].get['quantite']

    #         prod=self.env['gestion.stock'].search([()])




        return super(vente, self).create(vals)



class lignevente(models.Model):
    _name= 'gestion.lignevente'
    _description='ligne des ventes'

    produit_id=fields.Many2one('gestion.produit', string='Produit')
    prix=fields.Float('Prix')
    quantite=fields.Float('Quantite')
    total=fields.Float()
    vente_id=fields.Many2one('gestion.vente')

    @api.onchange('produit_id')
    def onchange_prix(self):

        self.prix = self.produit_id.prix_unitaire
        self.quantite=1.00
        self.total=self.quantite*self.produit_id.prix_unitaire
        
    @api.onchange('quantite', 'prix')
    def onchange_quantite(self):
        self.total=self.quantite*self.prix


