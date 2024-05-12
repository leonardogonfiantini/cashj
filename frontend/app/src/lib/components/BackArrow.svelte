<script>
    import Icon from '@iconify/svelte';
    import {show_status} from '$lib/store'
    
    
    export let status = 'tables';


    function go_back() {
        
        let tmp =  {
            tables: false,
            categories: false,
            products: false,
            ordina: false,
        }

        tmp[status] = true;

        show_status.set(tmp);

    }

</script>


<button class="arrow" on:click={go_back}>
    <Icon icon="emojione-monotone:left-arrow" style="font-size: 400%" />
</button>

<style>

    .arrow {
        position: absolute;
        bottom: 1rem;
        left: 1rem;
        cursor: pointer;
        border: 0;
        background-color: transparent;
    }

    .arrow:hover {
        transform: scale(1.1);
    }

</style>