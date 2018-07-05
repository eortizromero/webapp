odoo.define('webapp.loader', function(require){
"use strict";

var app = require('webapp.app');
var core = require('web.core');

core.action_registry.add('app.ui', app.Application);
});