from odoo import models, api, fields

class MailActivityInherit(models.Model):
    _inherit = "mail.activity"


    @api.model
    def create(self, vals):
        r = super(MailActivityInherit,self).create(vals)

        obj_create = self.env["activities"]
        
        if r.res_model_id.id == 79:
        
            values = {

                "mail_activity_type_id":r.activity_type_id.id,
                "date_deadline": r.date_deadline,
                "res_users_id":r.user_id.id,
                "summary":r.summary,
                "note": r.note,
                "res_id":r.res_id
                
            }

            obj_create.create(values)
        
        if r.res_model_id.id == 390:

            lead = self.env["crm.lead"].search([('id', '=', r.res_id)])

            if lead.partner_id.id:
                
                values = {

                    "mail_activity_type_id":r.activity_type_id.id,
                    "date_deadline": r.date_deadline,
                    "res_users_id":r.user_id.id,
                    "summary":r.summary,
                    "note": r.note,
                    "res_id": lead.partner_id.id
                    
                }

                obj_create.create(values)
        
        return r
