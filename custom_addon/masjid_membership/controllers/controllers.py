# -*- coding: utf-8 -*-
# from odoo import http


# class MasjidMembership(http.Controller):
#     @http.route('/masjid_membership/masjid_membership', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/masjid_membership/masjid_membership/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('masjid_membership.listing', {
#             'root': '/masjid_membership/masjid_membership',
#             'objects': http.request.env['masjid_membership.masjid_membership'].search([]),
#         })

#     @http.route('/masjid_membership/masjid_membership/objects/<model("masjid_membership.masjid_membership"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('masjid_membership.object', {
#             'object': obj
#         })
