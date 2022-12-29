# Copyright (C) 2013 Therp BV (<http://therp.nl>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Remove odoo.com Bindings",
    "version": "12.0.1.0.1",
    "author": "Therp BV,GRAP,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "base",
    "depends": [
        'mail',
    ],
    "data": [
        'views/ir_ui_menu.xml',
    ],
    "qweb": [
        'static/src/xml/base.xml',
    ],
    'installable': True,
}
