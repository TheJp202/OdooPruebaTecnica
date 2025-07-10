/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";
import { _t } from "@web/core/l10n/translation";


patch(PaymentScreen.prototype, {

    async onBoletaClick() {
        const total = this.currentOrder.get_total_with_tax();
        await this.popup.add(ConfirmPopup, {
            title: _t("Boleta"),
            body:  _t("El monto total a pagar es: %s", this.env.utils.formatCurrency(total)),
            confirmText: _t("Aceptar"),
        });
    },
});