 #-*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import Warning
import time

class AddElementWizard(models.TransientModel):
	_name = "bim.finance.add.element.wizard"

	def get_id2(self):
		ctx = self._context
		if (self.env.context.get('id_context')):

			return self.env.context.get('id_context')
		
		else:
			
			id_apu = self.env["bim.finance.apu"].browse(ctx['active_id'])
			return id_apu.id


	category_id = fields.Many2one("bim.finance.categories","Categoría")
	founding_request_id = fields.Integer("id", default=get_id2)
	rate_of_exchange = fields.Float("Tipo de cambio")
	

	bim_finance_add_element_wizard_detail_ids = fields.One2many("bim.finance.add.element.wizard.detail","bim_finance_add_element_wizard_id", "bim_finance_add_element_wizard_detail_ids")

	@api.onchange("founding_request_id")
	def getRate(self):

		if self.founding_request_id:
			
			apu = self.env["bim.finance.apu"].search([('id','=',self.founding_request_id)])

			if apu:
				self.rate_of_exchange = apu.rate_of_exchange




	def enterElements(self):
		
		if len(self.bim_finance_add_element_wizard_detail_ids) == 0:
			raise Warning(('Ningun elemento agregado'))
		
		obj_create = self.env["bim.finance.apu.detail"]
		
		for r in self.bim_finance_add_element_wizard_detail_ids:

			vals ={
				"category_id":self.category_id.id,
				"sequence":self.category_id.sequence,
				"element_id":r.element_id.id,
				"unit_of_measurement":r.unit_of_measurement.id,
				"performance":r.performance,
				"waste_percentage":r.waste_percentage,
				"cost_lempiras":r.cost_lempiras,
				"subtotal":r.subtotal,
				"cost_usd":r.cost_usd,
				"grades":r.grades,
				"bim_finance_apu_id": self.founding_request_id
			}

			obj_create.create(vals)
		

		view_id = self.env.ref("bim_finance.bim_finance_add_element_wizard_form_view", False)
	
		return {
			'name':("Agregar elementos"),
			'view_mode':'form',
			'view_id':view_id.id,
			'view_type':'form',
			'res_model':'bim.finance.add.element.wizard',
			'type':'ir.actions.act_window',
			'nodestroy':True,
			'target':'new',
			'context':{'id_context':self.founding_request_id},
			'domain':'[]'
		}
		


class  AddElementWizardDetail(models.TransientModel):
	_name = "bim.finance.add.element.wizard.detail"

	@api.depends("performance","cost_lempiras")
	def getTotal(self):
		for r in self:
			total = r.performance*r.cost_lempiras
			r.subtotal = total

			if r.bim_finance_add_element_wizard_id.rate_of_exchange == 0:
				raise Warning("La tasa de cambio no puede ser 0")
			r.cost_usd = total/r.bim_finance_add_element_wizard_id.rate_of_exchange

	element_id = fields.Many2one("bim.finance.elements","Descripción")
	unit_of_measurement = fields.Many2one("uom.uom","Unidad de medida")
	performance = fields.Float("Rendimiento")
	waste_percentage = fields.Float("% Desperdicio")
	cost_lempiras = fields.Float("Costo (Lp.)")
	subtotal = fields.Float("Sub Total (Lp.)", compute=getTotal)
	cost_usd = fields.Float("Costo en USD$", compute=getTotal)
	grades = fields.Char("Notas")
	
	bim_finance_add_element_wizard_id = fields.Many2one("bim.finance.add.element.wizard","bim_finance_add_element_wizard_id")

	@api.onchange("element_id")
	def getUom(self):

		if self.element_id:

			veri =  self.env["bim.finance.apu.detail"].search([('element_id','=',self.element_id.id),
							                                   ('bim_finance_apu_id','=',self.bim_finance_add_element_wizard_id.founding_request_id)])

			if veri:
				raise Warning("Ya existe la línea "+self.element_id.name + " en este APU")
			
			self.unit_of_measurement = self.element_id.unit_of_measurement.id

			
		

	

