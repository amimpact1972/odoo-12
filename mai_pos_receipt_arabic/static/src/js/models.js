odoo.define("mai_pos_receipt_arabic.models", function (require) {
"use strict";

var models = require('point_of_sale.models');

models.load_fields('res.company', ['street','street2','city','state_id','vat', 'name_arabic', 'street_arabic', 'street2_arabic', 'city_arabic', 'state_arabic']);
models.load_fields('product.product',['name','name_arabic']);

})