# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from datetime import *
import time
from datetime import datetime, timedelta
from odoo.exceptions import Warning


class CrmLeadInherit(models.Model):
	_inherit = "crm.lead"

	crm_lead_whatsapp_ids = fields.One2many("crm.lead.whatsapp", "crm_lead_id", "crm_lead_whatsapp_ids")


class CrmLeadWhatsapp(models.Model):
	_name = "crm.lead.whatsapp"

	message = fields.Char("Mensaje")
	to = fields.Char("Para")
	sender_name = fields.Char("Nombre del remitente")
	chat_name = fields.Char("Nombre del chat")
	date_time = fields.Datetime("Hora y fecha")
	state = fields.Selection([('sent','Enviado'),('recived','Recibido')], "Estado")

	crm_lead_id = fields.Many2one("crm.lead","crm_lead_id")
