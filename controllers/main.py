# -*- coding: utf-8 -*-


from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home


class Webclient(Home):

    @http.route('/', auth='public', csrf=None)
    def index(self):
        qcontext = {
            'title': 'Index Page'
        }
        return request.render('webapp.index', qcontext=qcontext)
