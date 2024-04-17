<script>

    import Tables from "./Tables.svelte";
    import Categories from "./Categories.svelte";
    import Products from "./Products.svelte";
</script>


<div class="selection">
    <Products category="Caffetteria" />
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