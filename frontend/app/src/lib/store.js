import { get, writable } from "svelte/store";


export let show_status = writable({
    tables: true,
    categories: false,
    products: false,
});

export let get_show_status = () => get(show_status)



