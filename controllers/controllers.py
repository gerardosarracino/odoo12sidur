# -*- coding: utf-8 -*-
from odoo import http

# class InformacionBasica(http.Controller):
#     @http.route('/informacion_basica/informacion_basica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/informacion_basica/informacion_basica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('informacion_basica.listing', {
#             'root': '/informacion_basica/informacion_basica',
#             'objects': http.request.env['informacion_basica.informacion_basica'].search([]),
#         })

#     @http.route('/informacion_basica/informacion_basica/objects/<model("informacion_basica.informacion_basica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('informacion_basica.object', {
#             'object': obj
#         })