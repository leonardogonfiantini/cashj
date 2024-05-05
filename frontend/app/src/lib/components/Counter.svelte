<script>
    import Icon from '@iconify/svelte';

    export let count;

    function up() {
        count++
    }

    function down() {

        if (count-1 < 0) {
            return
        }

        count--
    }

</script>



<div class="counter">
    <button class="arrow-up" on:click={up}> <Icon icon="bxs:up-arrow"/> </button>
    <p> {count} </p>
    <button class="arrow-down" on:click={down}> <Icon icon="bxs:down-arrow"/> </button>

</div>

<style>

    .counter {

        position: relative;
        width: 90%;
        height: 12vh;

        display: flex;
        justify-content: center;
        align-items: center;

        margin-inline: auto;

        gap: 10px;
    }

    .arrow-up, .arrow-down {

        position: relative;
        width: 5vh;
        height: 5vh;

        display: flex;
        justify-content: center;
        align-items: center;

        border-radius: 50%;
        color: white;
        font-size: 100%;

        border: 0;
    }

    .arrow-up {

        border-top-left-radius: 15px;
        border-bottom-left-radius: 15px;
    }

    .arrow-down {

        border-top-right-radius: 15px;
        border-bottom-right-radius: 15px;
    }

    .counter p {

        margin: 0;
        padding: 0;
        width: 5vh;
        height: 5vh;

        display: flex;
        justify-content: center;
        align-items: center;

        font-size: 150%;
    }
    
</style>