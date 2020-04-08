{
    'name': 'POS Arabic Receipt / POS Customized Receipt(Arabic Receipt)',
    'version': '12.0.2',
    'sequence': 1,
    'email': 'apps@maisolutionsllc.com',
    'website':'http://maisolutionsllc.com/',
    'category': 'Point of Sale',
    'summary': 'POS Arabic Receipt',
    'author': 'MAISOLUTIONSLLC',
    'price': 28,
    'currency': 'EUR',
    'license': 'OPL-1',
    'description': """
POS Customized Receipt(Arabic Receipt)
        """,
    "live_test_url" : "",
    'depends': ['point_of_sale','bi_pos_order_note'],
    'qweb': ['static/src/xml/templates.xml'],
    'data': ['views/pos_receipt_template.xml'],
    'images': ['static/description/main_screenshot.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}