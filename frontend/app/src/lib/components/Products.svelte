<script>

    import {PUBLIC_IP_BACKEND} from "$env/static/public" 
    import { onMount } from "svelte";
    
    export let category = "Caffetteria";
    
    let products = [{name: "loading...", color: "black", category_name: "loading..."}];
    let colors = ["orange", "red", "yellow", "green", "pink", "violet", "aqua"]

    function fetch_product_by_category() {
        fetch(`${PUBLIC_IP_BACKEND}/products?limit=100`)
            .then(response => response.json())
            .then(data => {
                products = data;
                console.log(products)
                products = products.filter(product => product.category_name === category)
                for (let i = 0; i < products.length; i++) {
                    products[i].color = colors[i % colors.length]
                }
            })

    }

    onMount(() => {
        fetch_product_by_category()
    })

</script>


<div class="products">

    {#each products as product}
        <div class="choice" style={`background-color:${product.color}`}>
            {product.name}
        </div>
    {/each}

</div>

<style>
    
        .products {
    
            position: relative;
            width: 90%;
            height: 90vh;
    
            display: flex;
            flex-wrap: wrap;
            justify-content:space-evenly;
            align-items: center;
    
            margin-inline: auto;
    
            gap: 10px;
    
        }

        .choice {
            position: relative;
            width: 25%;
            height: 20vh;

            border-radius: 15px;
            background-color: rgb(255, 255, 255);
            box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);

            text-align: center;
            justify-content: center;
            align-items: center;
            display: flex;
            font-size: 150%;
            color: black;
        }
</style>