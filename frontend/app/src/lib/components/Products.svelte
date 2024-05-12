<script>

    import { PUBLIC_IP_BACKEND } from "$env/static/public" 
    import { onMount } from "svelte";
    import { show_status, products_list, get_table_selected } from "$lib/store";
    import { colors } from "$lib/store.js";
    
    export let category = "Caffetteria";
    
    let products = [{name: "loading...", price_u_retail: 0, price_u_table: 0, color: "white", category_name: "loading...", id: 0}];

    async function fetch_product_by_category() {
        const response = await fetch(`${PUBLIC_IP_BACKEND}/products?limit=100`);
        const data = await response.json();
        products = data;
        
        products = products.filter(product => product.category_name === category)
    
        products.map(product => {
            product.color = colors[product.category_name]
        })

    }

    onMount(async () => {
        await fetch_product_by_category()

        let products_element = document.getElementsByClassName("choice")
        for (let product of products_element) {
            product.addEventListener("click", () => {
                show_status.update(value => {
                    value.tables = false;
                    value.products = false;
                    value.categories = true;
                    return value;
                })

                products_list.update(value => {
                    let p_list = value;

                    if (p_list.length === 0) {
                        p_list = [
                            {
                                name: product.textContent.trim(),
                                price: get_table_selected() == "Banco" ? parseFloat(product.getAttribute("data-price_u_retail")) : parseFloat(product.getAttribute("data-price_u_table")),
                                quantity: 1,
                                id: product.getAttribute("data-id")
                            }
                        ]
                        return p_list;
                    }

                    let found = false;
                    for (let i = 0; i < p_list.length; i++) {
                        if (p_list[i].name === product.textContent.trim()) {
                            p_list[i].quantity += 1;
                            found = true;
                            break;
                        }
                    }

                    if (!found) {
                        p_list.push({
                            name: product.textContent.trim(),
                            price: get_table_selected() == "Banco" ? parseFloat(product.getAttribute("data-price_u_retail")) : parseFloat(product.getAttribute("data-price_u_table")),
                            quantity: 1,
                            id: product.getAttribute("data-id")
                        })
                    }

                    return p_list;

                })
            })
        }
    })

</script>

<div class="products">

    {#each products as product}
        <div class="choice" style={`background-color:${product.color}`} data-price_u_retail={product.price_u_retail} data-price_u_table={product.price_u_table} data-id={product.id_prod}>
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