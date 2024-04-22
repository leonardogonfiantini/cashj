<script>
    import { onMount } from "svelte";
    import { show_status } from "$lib/store";

    const tables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    const table_name = "tavolo-"
    const banco_name = "banco"

    const colors = ["orange", "red"]

    onMount(() => {
        let tables_element = document.getElementsByClassName("choice")
        for (let table of tables_element) {
            table.addEventListener("click", () => {
                show_status.update(value => {
                    value.tables = false;
                    value.categories = true;
                    value.products = false;
                    return value;
                })
            })
        }
    })

</script>

<div class="tables">

    {#each tables as table}
        <div class="choice" style={`background-color: ${colors[0]}`}>
            {table_name + table}
        </div>
    {/each}

    <div class="choice" style={`background-color: ${colors[1]}`}>
        {banco_name}
    </div>

</div>

<style>

    .tables {

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
            width: 20%;
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