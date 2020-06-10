# -*- coding: utf-8 -*-
from odoo import http

# class Cpm-accounting(http.Controller):
#     @http.route('/cpm-accounting/cpm-accounting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cpm-accounting/cpm-accounting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cpm-accounting.listing', {
#             'root': '/cpm-accounting/cpm-accounting',
#             'objects': http.request.env['cpm-accounting.cpm-accounting'].search([]),
#         })

#     @http.route('/cpm-accounting/cpm-accounting/objects/<model("cpm-accounting.cpm-accounting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cpm-accounting.object', {
#             'object': obj
#         })