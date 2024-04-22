<script>

    import Tables from "./Tables.svelte";
    import Categories from "./Categories.svelte";
    import Products from "./Products.svelte";

    import { get_show_status, show_status } from "$lib/store"

    let status = get_show_status();
    show_status.subscribe((value) => {
        status = value;
    })


</script>


<div class="selection">

    {#if status.tables}
        <Tables />
    {/if}

    {#if status.categories}
        <Categories />
    {/if}

    {#if status.products}
        <Products />
    {/if}
    
</div>


<style>

    .selection {

        position: relative;
        width: 90%;
        height: 90vh;

        margin-inline: auto;
        top: 5vh;

        border-radius: 15px;
        background-color: rgb(255, 255, 255);
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
        

    }

</style>