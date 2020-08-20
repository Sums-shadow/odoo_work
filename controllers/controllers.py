# -*- coding: utf-8 -*-
# from odoo import http


# class Gestion(http.Controller):
#     @http.route('/gestion/gestion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion/gestion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion.listing', {
#             'root': '/gestion/gestion',
#             'objects': http.request.env['gestion.gestion'].search([]),
#         })

#     @http.route('/gestion/gestion/objects/<model("gestion.gestion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion.object', {
#             'object': obj
#         })
