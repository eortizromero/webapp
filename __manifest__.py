# -*- encoding: utf-8 -*-

{
    "name": "Odoo Web Application",
    "version": "1.0",
    "author": "Edgar Ortiz",
    "website": "https://github.com/eortizromero",
    "depends": [],
    "description": "Odoo Application for Web",
    "sequence": 1,
    "data": [
        "views/webapp_templates.xml",
        "views/webapp.xml"
    ],
    "qweb": ['static/src/xml/app.xml'],
    "installable": True,
    "application": True
}