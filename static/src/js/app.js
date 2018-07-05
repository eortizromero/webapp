odoo.define('webapp.app', function(require){
"use strict";

    var Widget = require('web.Widget');

    var Application = Widget.extend({
        template: 'Application',

        init: function(){
            // console.log(this.$el);
            this._super();
        },
        render: function () {
            console.log(this.$el);
        }
    });

return {Application: Application};

});