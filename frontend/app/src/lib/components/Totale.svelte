<script>

    import { products_list, show_status } from "$lib/store.js";


    products_list.subscribe(value => {

        if (value.length === 0) {
            return;
        }

        let ordina = document.getElementsByClassName('ordina')[0].querySelector('p');
        let tot = 0;
        for (let product of value) {
            tot += product.price * product.quantity;
        }
        ordina.textContent = `TOT: € ${tot.toFixed(2)}`
    })

    function ordina() {
        show_status.update(value => {
            return {
                tables: false,
                categories: false,
                products: false,
                ordina: true
            }
        })
    }

</script>


<button class="ordina" on:click={ordina}>
    <p> TOT: € 0.0 </p>

    <div class="freccetta">
        &#x2192; 
    </div>
</button>



<style>

    .ordina {

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

    .ordina p {
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