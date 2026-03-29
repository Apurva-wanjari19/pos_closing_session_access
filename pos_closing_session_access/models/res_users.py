from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    pos_close_session_access = fields.Boolean(
        string="Access for Closing POS"
    )