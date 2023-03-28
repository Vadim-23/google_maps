/** @odoo-module **/

import {PivotView} from "@web/views/pivot/pivot_views"
import { registry } from "@web/core/registry";



const viewRegistry = registry.category("views");
//const PivotView = viewRegistry.get("pivot");
debugger;
console.log(PivotView);

export class MyPivotView extends PivotView {
    add_color() {
        console.log('sssss');
                };

}
viewRegistry.remove("pivot");
viewRegistry.add("pivot", MyPivotView);