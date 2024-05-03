<script>
    import Conteggio from '$lib/components/Conteggio.svelte';
    import Totale from '$lib/components/Totale.svelte';
    import Selection from '$lib/components/Selection.svelte';
</script>

<div class="app">

    <div class="left-side">
        <Conteggio />
        <Totale />
    </div>
    
    <div class="right-side">
        <Selection />
    </div>

</div>

<style>

    .app {
        width: 100vw;
        height: 100vh;

        display: block;
        position: relative;
    }

    .left-side {
        position: absolute;

        width: 40%;
        height: 100%;

        left: 0;

        background-color: rgb(245, 245, 245);
    }

    .right-side {
        position: absolute;

        width: 60%;
        height: 100%;

        right: 0;

        background-color: rgb(245, 245, 245);
    }


</style>