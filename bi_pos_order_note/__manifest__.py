# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Order Note in odoo",
    "version" : "12.0.0.2",
    "category" : "Point of Sale",
    "depends" : ['base','sale','point_of_sale',
                 ],
    "author": "BrowseInfo",
    'summary': 'This apps helps to add POS order note on TouchScreen, Receipt and Backend Order',
    "description": """
    
    Purpose :- 
    This Module allow us to add bag charges on particular order.
    POS order Note point of sales order note , point of sales note
	


    Add Note on POS

    POS Note

    POS Order line Note

    POS line Note

    POS Receipt Note

    POS backend NOte

    Add note on POS order

    Point Of Sale Note

    POS order Note

    Add Note on POS

    POS line Note

    Point of Sale Order line Note

    Point of Sale line Note

    Point of Sale Receipt Note

    Point of Sale backend NOte

    Add note on Point of Sale order

 This Module allow us to add advance order note particular order line in point of sales.
    POS order Note Add Note on POS
    POS Notes POS Advance Order Note POS Order line Note
    order note on line in pos remarks on order pos note suggestion 
    POS line Note POS Receipt Note POS backend NOte Add note on POS order
    Point Of Sale Note POS order Note Add Note on POS POS line Note
    Point of Sale Order line Note Point of Sale line Note
    Point of Sale Receipt Note Point of Sale backend NOte Add note on Point of Sale order

    Point of Sales Note Add Note on Point of Sales
    Point of Sales Notes Point of Sales Advance Order Note Point of Sales Point of Sales line Note
    order note on line in Point of Sales remarks on order Point of Sales note suggestion 
    Point of Sales line Note Point of Sales Receipt Note Point of Sales backend NOte Add note on Point of Sales order
    Point Of Sale Note Point of Sales order Note Add Note on Point of Sales Point of Sales line Note
    Point of Sales Order line Note Point of Sales line Note
    Point of Sales Receipt Note Point of Sales backend NOte Add note on Point of Sale order

    Point of Sale order Note Add Note on Point of Sale
    Point of Sale Notes Point of Sale Advance Order Note Point of Sale Order line Note
    order note on line in Point of Sale remarks on order Point of Sale note suggestion 
    Point of Sale line Note Point of Sale Receipt Note Point of Sale backend NOte Add note on Point of Sale order
    Point Of Sale Note Point of Sale order Note Add Note on Point of Sale Point of Sale line Note print pos note print point of sale note print point of sales note
    print pos note on receipt print point of sale note on receipt print point of sales note on receipts
    print pos note on bill receipt print point of sale note on bill receipt print point of sales note on bill receipts

    add pos note on receipt add point of sale note on receipt add point of sales note on receipts
    add pos note on bill receipt add point of sale note on bill receipt add point of sales note on bill receipts
    """,
    "price": 7.99,

    "currency": 'EUR',
    "website" : "www.browseinfo.in",
    "data": [
        'views/bi_pos_order_note.xml',
    ],
    'qweb': [
        'static/src/xml/pos_order_note_template.xml',
    ],
    "auto_install": False,
    "installable": True,
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
