<script>

    import Counter from "$lib/components/Counter.svelte"
    import {get_products_list} from "$lib/store.js"
    import Icon from '@iconify/svelte';
    import { onMount } from "svelte";
    import tippy from 'tippy.js';
    import 'tippy.js/themes/light.css';
    let counter_clients = 0;
    let counter_discount = 0;

    let totale = 0;
    let p_list = get_products_list();
    for (let product of p_list) {
        totale += product.price * product.quantity;
    }

    totale = totale.toFixed(2);

    onMount(() => {
        
        // on hover tooltip  for clients, discount, totale, totale-sconto
        tippy('.clients .icon', {
            content: 'Numero di clienti',
            placement: 'top',
            theme: 'light',
        });

        tippy('.discount .icon', {
            content: 'Numero di sconti',
            placement: 'top',
            theme: 'light',
        });

        tippy('.totale .icon', {
            content: 'Totale',
            placement: 'top',
            theme: 'light',
        });

        tippy('.totale-sconto .icon', {
            content: 'Totale scontato',
            placement: 'top',
            theme: 'light',
        });


    });

</script>


<div class="ordina">

    <div class="clients">
        <Icon icon="lets-icons:group-fill" style="font-size: 48px;" class="icon"/>
        <Counter bind:count={counter_clients} />
    </div>


    <div class="discount">
        <Icon icon="ic:baseline-discount" style="font-size: 48px;" class="icon"/>
        <Counter bind:count={counter_discount} />
    </div>

    <div class="totale">
        <Icon icon="mdi:euro" style="font-size: 48px;"/>
        <p> {totale} </p>   
    </div>

    <div class="totale-sconto">
        <Icon icon="lucide:receipt-euro" style="font-size: 48px;" class="icon"/>
        <p> {totale - counter_discount} </p>   
    </div>

</div>



<style>

    .ordina {

        position: relative;
        width: 90%;
        height: 90vh;

        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-inline: auto;

        gap: 10px;
    }

    .clients, .discount, .totale, .totale-sconto {

        position: relative;
        width: 90%;
        height: 12vh;

        display: flex;

        align-items: center;

        border-radius: 15px;
        background-color: white;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);

        padding: 0 10px;
    }

    .totale p, .totale-sconto p {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 150%;
            color: black;


    }




</style>