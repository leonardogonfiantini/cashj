<script>

    import {PUBLIC_IP_BACKEND} from "$env/static/public" 
    import { onMount } from "svelte";
    

    let categories = [{name: "loading...", color: "black"}];
    let colors = ["orange", "red", "yellow", "green", "pink", "violet", "aqua"]
    
    async function fetch_categories() {
        const response = await fetch(`${PUBLIC_IP_BACKEND}/categories`);
        const data = await response.json();
        categories = data;
        for (let i = 0; i < categories.length; i++) {
            categories[i].color = colors[i % colors.length]
        }

    }

    onMount(() => {
        fetch_categories()
    })

</script>

<div class="categories">

    {#each categories as category}
        <div class="choice" style={`background-color:${category.color}`}>
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