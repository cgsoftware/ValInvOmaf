# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import decimal_precision as dp
import time
import base64
from tempfile import TemporaryFile
import math
from osv import fields, osv
import tools
import ir
import pooler
import tools
from tools.translate import _
import csv
import sys
import os
import re


class  gruppi_val(osv.osv):
        _description = 'Gruppo di Valorizzazione'
        _name = "gruppi.val"

        _columns = {
                    'name': fields.char('Codice', size=4, required=True, translate=True, select=True),
                    'descrizione': fields.char('Descrizione', size=30, required=False, translate=True, select=True),
                    }

    
gruppi_val()    



class  categoria_val(osv.osv):
        _description = 'Categoria di Valorizzazione'
        _name = "categoria.val"
        _columns = {
                    'name': fields.char('Codice', size=4, required=True, translate=True, select=True),
                    'descrizione': fields.char('Descrizione', size=30, required=False, translate=True, select=True),
                    }

    
categoria_val()    

def _ListaGruppi(self, cr, uid, context={}):
            res = []
            ids = self.pool.get('gruppi.val').search(cr, uid, [])
            if ids:
                 for gruppo in self.pool.get('gruppi.val').browse(cr, uid, ids):
                        res.append((gruppo.name, gruppo.descrizione))
            return res


def _ListaCat(self, cr, uid, context={}):
            res = []
            ids = self.pool.get('categoria.val').search(cr, uid, [])
            if ids:
                 for gruppo in self.pool.get('categoria.val').browse(cr, uid, ids):
                        res.append((gruppo.name, gruppo.descrizione))
            return res

class  costi_prestazioni(osv.osv):
        _description = 'Prezzi costo base per singola unità di produzione'
        _name = "costi.prestazioni"
        _columns = {
                    'name': fields.char('Codice', size=64, required=True, translate=True, select=True),
                    'descrizione': fields.char('Descrizione', size=128, required=False, translate=True, select=True),
                    'gruppo_val':fields.selection(_ListaGruppi, 'Codice Raggruppamento', required=True),
                    'costo':fields.float('Costo Unitario', required=False, digits=(11, 5)),
                    }




costi_prestazioni()


class  skcosti_prod_head(osv.osv):
        _description = 'Scheda costi di produzione per singola unità'
        _name = "skcosti.prod.head"
        _columns = {
                    'name': fields.char('Codice', size=64, required=True, translate=True, select=True),
                    'descrizione': fields.char('Descrizione', size=128, required=False, translate=True, select=True),
                    'costo_fisso':fields.float('Costo Fisso', required=False, digits=(11, 5)),
                    'righe_prestaz': fields.one2many('skcosti.prod.line', 'scheda_id', 'Righe Prestazioni'),
}
        
skcosti_prod_head()        
        



class  skcosti_prod_line(osv.osv):
        _description = 'Scheda costi di produzione per singola unità righe'
        _name = "skcosti.prod.line"
        _columns = {
                    'scheda_id': fields.many2one('skcosti.prod.head', 'Testa Template Busta', required=True, ondelete='cascade', select=True, readonly=False),
                    'cod_costo':fields.many2one('costi.prestazioni', 'Prestazione/Servizio', required=True, ondelete='cascade', select=True, readonly=False),
                    'qta_prest':fields.float('Quant', required=True, digits=(11, 5)),
                    'gruppo_val': fields.related('cod_costo', 'gruppo_val', string='ragruppamento', type='char', relation='costi.prestazioni'),
                    'costo': fields.related('cod_costo', 'costo', string='Prezzo/Costo', type='float', relation='costi.prestazioni'),
}
skcosti_prod_line()


class  product_skprod(osv.osv):
        _description = 'Schede costi di produzione assegnate all articolo'
        _name = "product.skprod"
        _columns = {
                    'product_id': fields.many2one('product.product', 'Articolo', ondelete='set null', select=True, required=True),
                    'categoria_val':fields.selection(_ListaCat, 'Codice Valorizzazione', required=True),
                    'schedaco_id': fields.many2one('skcosti.prod.head', 'Scheda Costi', ondelete='set null', select=True, required=True),
}
    
product_skprod()    


class product_product(osv.osv):
    _inherit = "product.product"

    _columns = {
                'tipo_valoriz': fields.one2many('product.skprod', 'product_id', 'Righe Valorizzazioni di Costi'),
                }
    
product_product()    

    
