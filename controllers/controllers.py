# -*- coding: utf-8 -*-
from odoo import http

# class /home/administrator/enterprise/clinicaDiadema(http.Controller):
#     @http.route('//home/administrator/enterprise/clinica_diadema//home/administrator/enterprise/clinica_diadema/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/administrator/enterprise/clinica_diadema//home/administrator/enterprise/clinica_diadema/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/administrator/enterprise/clinica_diadema.listing', {
#             'root': '//home/administrator/enterprise/clinica_diadema//home/administrator/enterprise/clinica_diadema',
#             'objects': http.request.env['/home/administrator/enterprise/clinica_diadema./home/administrator/enterprise/clinica_diadema'].search([]),
#         })

#     @http.route('//home/administrator/enterprise/clinica_diadema//home/administrator/enterprise/clinica_diadema/objects/<model("/home/administrator/enterprise/clinica_diadema./home/administrator/enterprise/clinica_diadema"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/administrator/enterprise/clinica_diadema.object', {
#             'object': obj
#         })