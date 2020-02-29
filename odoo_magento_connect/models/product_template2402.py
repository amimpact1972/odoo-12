# -*- coding: utf-8 -*-
##########################################################################
#
#   Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
#
##########################################################################

import binascii
import requests

from odoo import api, fields, models
from .res_partner import _unescape
import codecs
import io
from urllib.parse import quote

from PIL import Image
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    prod_type = fields.Char(string='Magento Type')
    config_sku = fields.Char(string='SKU')
    categ_ids = fields.Many2many(
        'product.category',
        'product_categ_rel',
        'product_id',
        'categ_id',
        string='Extra Categories')
    attribute_set_id = fields.Many2one(
        'magento.attribute.set',
        string='Magento Attribute Set',
        help="Magento Attribute Set, Used during configurable product generation at Magento.")
    mob_mapping_ids = fields.One2many(
        string='Mappings',
        comodel_name='magento.product.template',
        inverse_name='template_name',
        copy=False
    )

    @api.model
    def create(self, vals):
        ctx = dict(self._context or {})
        tepltIds = 0
        if 'magento' in ctx:
            mageId = vals.pop('mage_id', 0)
            vals = self.update_vals(vals, True)
        prodTempObj = super(ProductTemplate, self).create(vals)
        if 'magento' in ctx and 'configurable' in ctx:
            mappingData = {
                'template_name' : prodTempObj.id,
                'erp_template_id' : prodTempObj.id,
                'mage_product_id' : mageId,
                'base_price' : vals['list_price'],
                'is_variants' : True,
                'instance_id' : ctx.get('instance_id'),
                'created_by' : 'Magento'
            }
            tepltIds = self.env['magento.product.template'].create(mappingData)
            
##auto synch
        successExpIds, successUpdtIds, templateIds = [], [], []
        updtErrorIds, errorIds = [], []
        connection = self.env['magento.configure']._create_connection()
        
        if connection:
            syncHistoryModel = self.env['magento.sync.history']
            templateModel = self.env['product.template']
            url = connection[0]
            token = connection[1]
            ctx = dict(self._context or {})
            instanceId = ctx['instance_id'] = connection[2]
            domain = [('instance_id', '=', instanceId)]
                

            connectionObj = self.env[
                'magento.configure'].browse(instanceId)
            warehouseId = connectionObj.warehouse_id.id
            ctx['warehouse'] = warehouseId
            templateIds = [prodTempObj.id]
            
            mappedObj = self.env['magento.product.template'].search(
            [('instance_id', '=', ctx.get('instance_id'))])
            mapTemplateIds = mappedObj.mapped('template_name').ids
            notMappedTempltIds = list(set(templateIds) - set(mapTemplateIds))
            notMappedTemplateIds = notMappedTempltIds
            if not notMappedTemplateIds:
                    raise UserError(('Information!\nListed product(s) has been already exported on magento.'))
            for templateObj in templateModel.with_context(
                        ctx).browse(notMappedTemplateIds):
                    prodType = templateObj.type
                    if prodType == 'service':
                        errorIds.append(templateObj.id)
                        continue
                    expProduct = self.env['magento.synchronization'].with_context(
                        ctx)._export_specific_template(templateObj, url, token)
                    if expProduct[0] > 0:
                        successExpIds.append(templateObj.id)
                    else:
                        errorIds.append(expProduct[1])
##fin auto synch
            
        return prodTempObj

    @api.multi
    def write(self, vals):
        ctx = dict(self._context or {})
        instanceId = ctx.get('instance_id', False)
        if 'magento' in ctx:
            vals.pop('mage_id', None)
            vals = self.update_vals(vals)
        mapTempModel = self.env['magento.product.template']
        for tempObj in self:
            tempMapObjs = mapTempModel.search(
                [('template_name', '=', tempObj.id)])
            for tempMapObj in tempMapObjs:
                if instanceId and tempMapObj.instance_id.id == instanceId:
                    tempMapObj.need_sync = 'No'
                else:
                    tempMapObj.need_sync = 'Yes'
        return super(ProductTemplate, self).write(vals)

    def update_vals(self, vals, create=False):
        if vals.get('default_code'):
            vals['config_sku'] = _unescape(vals.pop('default_code', ''))
        if vals.get('name'):
            vals['name'] = _unescape(vals['name'])
        if vals.get('description'):
            vals['description'] = _unescape(vals['description'])
        if vals.get('description_sale'):
            vals['description_sale'] = _unescape(vals['description_sale'])
        category_ids = vals.pop('category_ids', None)
        if category_ids:
            categIds = list(set(category_ids))
            defaultCategObj = self.env["magento.configure"].browse(
                self._context['instance_id']).category
            if defaultCategObj and create:
                vals['categ_id'] = defaultCategObj.id
            vals['categ_ids'] = [(6, 0, categIds)]
        imageUrl = vals.pop('image_url', False)
        if imageUrl:
            proImage = binascii.b2a_base64(requests.get(imageUrl).content)
            vals['image'] = proImage
        vals.pop('attribute_list', None)
        vals.pop('magento_stock_id', None)
        return vals

