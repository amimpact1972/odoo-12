# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo.tools import pdf


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def print_airwaybill(self):
        pdf_data = self.env.ref('custom_report.action_report_airway').sudo().render_qweb_pdf(self.ids)[0]
        pdf_data = base64.b64encode(pdf_data)
        logmessage = ("Air waybill generated<br/>")
        attachment = self.env['ir.attachment'].create({
        'name': 'Airwaybill.pdf',
        'type': 'binary',
        'datas': pdf_data,
        'datas_fname': 'Airwaybill.pdf',
        'res_model': self._name,
        'res_id': self.ids[0],
        })
        self.message_post(body=logmessage, attachment_ids=[attachment.id])
        return self.env.ref('custom_report.action_report_airway').report_action(self)
