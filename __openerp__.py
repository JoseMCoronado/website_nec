# -*- coding: utf-8 -*-

###################################################################################
#
#    Copyright (C) 2017 JDC Systems
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': 'National Equipment Corp. Website Modifications',
    'category': 'Website',
    'summary': 'Custom',
    'version': '1.0',
    "website": "http://www.jdcsystems.net/",
    "author": "JDC Systems",
    'description': """


Features:
-Renamed "Add to Cart" to "Add to Request" from website product view
-Removed price column from webiste cart_lines view
-Renamed 'Billing & Shipping' to 'Customer Information' on website wizard_checkout view
-Rerouted 'Continue Shopping' button to go to the first website category of the first cart line
-Renamed 'Billing Information' to 'Customer Information' on website checkout
-Added Addtl. Info. Step (using base Extra Info) functionality.
-Removed 'Feedback' and 'Reject' buttons on the online quotation
-Renamed 'Accept' button to 'Accept terms & conditions' on the online quotation
        """,
    'depends': ['base_import','website_sale','website_quote','sale_ebay','account_accountant'],
    'data': [
        'data/ir_models.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_view.xml',
        'data/ir_ui_qweb.xml',
        'data/ir_actions_server.xml',
    ],
    'installable': True,
}
