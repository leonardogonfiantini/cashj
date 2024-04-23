<script>

    import { PUBLIC_IP_BACKEND } from "$env/static/public" 
    import { onMount } from "svelte";
    import { show_status, colors, category_selected } from "$lib/store";

    let categories = [{name: "loading...", color: "white"}];
    
    async function fetch_categories() {
        const response = await fetch(`${PUBLIC_IP_BACKEND}/categories`);
        const data = await response.json();
        categories = data;
        for (let i = 0; i < categories.length; i++) {
            categories[i].color = colors[categories[i].name]
        }

    }

    onMount(async () => {
        await fetch_categories()

        let categories_element = document.getElementsByClassName("choice")
        for (let category of categories_element) {
            category.addEventListener("click", () => {
                
                show_status.update(value => {
                    value.tables = false;
                    value.categories = false;
                    value.products = true;
                    return value;
                })

                category_selected.update(value => {
                    value = category.id;
                    return value;
                })

            })
        }
    })

</script>

<div class="categories">

    {#each categories as category}
        <div class="choice" id={category.name} style={`background-color:${category.color}`}>
            {category.name}
        </div>
    {/each}

</div>


<style>

    .categories {

        position: relative;
        width: 90%;
        height: 90vh;

        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;

        margin-inline: auto;

        gap: 10px;

    }



    .choice {
            
            position: relative;
            width: 30%;
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