/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { ConfirmPopup } from "@point_of_sale/app/utils/confirm_popup/confirm_popup";
import { _t } from "@web/core/l10n/translation";

patch(Order.prototype, {
    async add_product(product, options = {}) {
        const price = product.get_price ? product.get_price() : product.lst_price;

        if (price === 0) {
            const { confirmed } = await this.pos.env.services.popup.add(ConfirmPopup, {
                title: _t("¡Producto sin precio!"),
                body:  _t("Has seleccionado un producto sin precio. ¿Deseas continuar?"),
                confirmText: _t("Continuar"),
                cancelText:  _t("Cancelar"),
            });

            if (!confirmed) {
                return;
            }
        }
        return super.add_product(product, options);
    },
});