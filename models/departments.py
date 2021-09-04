# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from datetime import *
import time
from datetime import datetime, timedelta
from odoo.exceptions import Warning


class Departments(models.Model):
	_name = "departments"

	name = fields.Char("Departamento")

	municipalities_ids = fields.One2many("municipalities","departments_id","municipalities_ids")

class Municipalities(models.Model):
	_name = "municipalities"

	name = fields.Char("Municipio")

	departments_id = fields.Many2one("departments","departments_id")


	