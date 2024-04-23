<script>
    let time = "";

    setInterval(() => {
        let time_now = new Date();

        let time_day = time_now.getDate();
        let time_month = time_now.getMonth();
        let time_year = time_now.getFullYear();

        let time_now_hours = time_now.getHours() < 10 ? `0${time_now.getHours()}` : time_now.getHours();
        let time_now_minutes = time_now.getMinutes() < 10 ? `0${time_now.getMinutes()}` : time_now.getMinutes();
        let time_now_seconds = time_now.getSeconds() < 10 ? `0${time_now.getSeconds()}` : time_now.getSeconds();

        time = `${time_day}/${time_month}/${time_year} ${time_now_hours}:${time_now_minutes}:${time_now_seconds}`;
    }, 1000);
</script>

{time}