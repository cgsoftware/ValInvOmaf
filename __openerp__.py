# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
##############################################################################
{
    'name': 'Calcoli costi di Produzione',
    'version': '1.0',
    'category': 'Product',
    'description': """
     Modifche Specifiche per la valorizzazione dei costi di produzione dell'articolo, tiene conto di tabelle 
     personalizzate di costi di linea di produzione e dei costi materie prime per lotti""",
    'author': 'C & G Software',
    "depends" : ['base', 'product'],
    "update_xml" : [
                    'security/ir.model.access.csv',
                    'skcostiprod_view.xml',
                    ],
    'website': 'http://www.cgsoftware.it',
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
