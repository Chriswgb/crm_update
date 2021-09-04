# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from datetime import *
import time
from datetime import datetime, timedelta
from odoo.exceptions import Warning


class ResPartnertInherit(models.Model):
	_inherit = "res.partner"

	def stage_groups(self, present_ids, domain, **kwargs):
		stage = self.env['res.partner.stage'].search([]).name_get()
		return stage, None

	_group_by_full = {
		'stage_id': stage_groups,
	}

	@api.depends("name")
	def getCount(self):

		for rec in self:
			count_email = self.env["activities"].search([('res_id','=',rec.id),('mail_activity_type_id','=',1)])
			count_call = self.env["activities"].search([('res_id','=',rec.id),('mail_activity_type_id','=',2)])
			count_metting = self.env["activities"].search([('res_id','=',rec.id),('mail_activity_type_id','=',3)])
			count_to_do = self.env["activities"].search([('res_id','=',rec.id),('mail_activity_type_id','=',4)])

			rec.email_count = len(count_email)
			rec.call_count = len(count_call)
			rec.metting_count = len(count_metting)
			rec.to_do_count = len(count_to_do)


	rtn = fields.Char("RTN")
	stage_id = fields.Many2one("res.partner.stage","Etapa")
	email_count = fields.Integer("Cantidad email", compute=getCount)
	call_count = fields.Integer("Cantidad llamadas", compute=getCount)
	metting_count = fields.Integer("Cantidad reuniones", compute=getCount)
	to_do_count = fields.Integer("Cantidad por hacer", compute=getCount)

	department_id = fields.Many2one("departments","Departamento")
	municipality_id = fields.Many2one("municipalities","Municipio")

	references = fields.Many2one("references", "Referencia")

	@api.onchange("department_id")
	def clearMunicipality(self):

		self.municipality_id = False


class StageResPartner(models.Model):
	_name = "res.partner.stage"
	_order = 'sequence, id'

	name = fields.Char('Stage Name')
	sequence = fields.Integer('Sequence', default=1)
	
