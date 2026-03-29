from odoo import models

class PosSession(models.Model):
    _inherit = "pos.session"

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        if "res.users" not in result:
            result.append("res.users")
        return result

    def _loader_params_res_users(self):
        result = super()._loader_params_res_users()
        result["search_params"]["fields"].append("pos_close_session_access")
        return result