/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ClosePosPopup } from "@point_of_sale/app/navbar/closing_popup/closing_popup";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";

patch(ClosePosPopup.prototype, {

    async confirm() {

        console.log("Close session confirm triggered");

        const userId = this.pos.user.id;

        const result = await this.pos.data.call(
            "res.users",
            "read",
            [[userId], ["pos_close_session_access"]]
        );

        const hasAccess = result?.[0]?.pos_close_session_access;

        console.log("User access from backend:", hasAccess);

        if (!hasAccess) {
            this.dialog.add(AlertDialog, {
                title: _t("Access Denied"),
                body: _t("Contact your admin for closing POS session access."),
            });
            return;
        }

        return super.confirm(...arguments);
    },

});