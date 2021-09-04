# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from datetime import *
import time
from datetime import datetime, timedelta
from odoo.exceptions import Warning


class Activities(models.Model):
	_name = "activities"
	_rec_name = "summary"
	
	mail_activity_type_id = fields.Many2one("mail.activity.type", "Tipo de actividad")
	date_deadline = fields.Date("Fecha de vencimiento")
	res_users_id = fields.Many2one("res.users", "Asignada a")
	summary = fields.Char("Resumen")
	note = fields.Html("Notas")
	res_id = fields.Many2one("res.partner", "Contacto")

	