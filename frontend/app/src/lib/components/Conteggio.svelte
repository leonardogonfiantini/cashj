<script>

    import { onMount } from "svelte";
    import { products_list, table_selected } from "$lib/store";
    import Time from "$lib/components/Time.svelte";

    let title = "";
    table_selected.subscribe(value => {
        title = value;
    });

    
    /**
     * @typedef {Object} Product
     * @property {string} name - The name of the product.
     * @property {number} price - The price of the product.
     * @property {number} quantity - The quantity of the product.
     */

    /** @type {Product[]} */
    let p_list = [];

    products_list.subscribe(value => {    
        if (value.length === 0) {
            return;
        }
        p_list = value;
    })

</script>


<div class="conteggio">
    
    <section class="topbar">
        
        <div class="title">
            <h1>{title}</h1>
        </div>
        
        <div class="time">
            <h1> <Time /> </h1>
        </div>
    </section>

    <section class="content">
        <h1>Conteggio</h1>
    </section>        

</div>

<style>

    .conteggio {
        position: relative;
        width: 90%;
        height: 75vh;

        margin-inline: auto;
        top: 5vh;

        border-radius: 15px;
        background-color: rgb(255, 255, 255);


        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);

    }

    .title {
        display: block;
        position: absolute;
        top: 1rem;
        left: 1rem;
    }

    .title h1 {
        font-size: 1.5em;
    }

    .time {
        display: block;
        position: absolute;

        top: 1rem;
        right: 1rem;

    }

    .time h1 {
        font-size: 1.5em;
    }

    .topbar {
        display: block;
        width: 100%;
        height: 3rem;

        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }

    .content {
        padding: 1rem;
    }


</style>