<script>

    import { products_list, show_status, table_selected, get_show_status, get_table_selected, get_products_list } from "$lib/store.js";
    import { PUBLIC_IP_BACKEND } from "$env/static/public"
    import Time from "./Time.svelte";

    products_list.subscribe(value => {

        if (value.length === 0) {
            return;
        }

        let ordina = document.getElementsByClassName('totale')[0].querySelector('p');
        let tot = 0;
        for (let product of value) {
            tot += product.price * product.quantity;
        }
        ordina.textContent = `TOT: € ${tot.toFixed(2)}`
    })

    function ordina() {

        let show_status_t = get_show_status();
        if (show_status_t.ordina) {

            let p_list_temp = get_products_list();
            let p_list = {}
            for (let product of p_list_temp) {
                p_list[product.id] = product.quantity;
            }

            let body = {
                "billNo": Math.floor(Math.random() * 1000000000),
                "date": new Date().toISOString().slice(0, 10),
                "table": get_table_selected(),
                "discount": parseInt(document.querySelector('.discount .counter p').textContent),
                "price": parseFloat(document.querySelector('.totale-sconto p').textContent),
                "n_client": parseInt(document.querySelector('.clients .counter p').textContent),
                "order_details": p_list
            }

            fetch(`${PUBLIC_IP_BACKEND}/order`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            })

            let ordina = document.getElementsByClassName('totale')[0].querySelector('p');
            ordina.textContent = `TOT: € 0.00`

            show_status.update(value => {
                return {
                    tables: true,
                    categories: false,
                    products: false,
                    ordina: false
                }
            })

            products_list.update(value => {
                return []
            })

            table_selected.update(value => {
                return "Selezionare un tavolo"
            })
        
            return;
        }


        show_status.update(value => {
            return {
                tables: false,
                categories: false,
                products: false,
                ordina: true
            }
        })

        let ordina = document.getElementsByClassName('totale')[0].querySelector('p');
        ordina.textContent = `ORDINA`

    }

</script>


<button class="totale" on:click={ordina}>
    <p> TOT: € 0.00 </p>

    <div class="freccetta">
        &#x2192; 
    </div>
</button>



<style>

    .totale {

        position: relative;
        width: 80%;
        height: 12vh;

        margin-inline: auto;
        margin-top: 8vh;

        border-radius: 15px;
        background-color: red;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
        
        text-align: center;
        justify-content: center;
        align-items: center;
        display: flex;
        font-size: 300%;
        color: white;

        border: 0;
    }

    .totale p {
        margin: 0;
        padding: 0;
        width: 80%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 100%;
        color: white;
    }

    .freccetta {

        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        width: 20%;
        color: white;
        font-size: 200%;
        display: flex;
        justify-content: center;
        align-items: center;
    }


</style>