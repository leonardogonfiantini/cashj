import { get, writable } from "svelte/store";


export let show_status = writable({
    tables: true,
    categories: false,
    products: false,
});
export let get_show_status = () => get(show_status)


export let products_list = writable([]);
export let get_products_list = () => get(products_list)

export let category_selected = writable("Caffetteria");

export let table_selected = writable("Selezionare un tavolo");


/**
* @type {Object.<string, string>}
*/
export let colors = {
    Caffetteria: "orange",
    Bibite: "red",
    Drink: "yellow",
    Vini: "green",
    Birre: "pink",
    Amari: "violet",
    Cibi: "aqua"
}

