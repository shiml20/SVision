<template>
    <div class="b-container">
        <div class="park-info-header">
            <router-link class='logo' to="/main" style="height: 10%; width: 10%;">
                <img  src="../assets/img/SVision2.svg" 
                alt="SVision" style="zoom: 100%;">
            </router-link>
            <h2>工作日志</h2>
            <WeatherReport class="weather-report"></WeatherReport>
        </div>
        <div class="park-info-main">
            <div class="left"></div>
            <div class="right"></div>   
        </div>
    </div>
</template>


<script lang="ts" setup>
import WeatherReport from '@/components/WeatherReport.vue';


</script>

<style scoped lang="scss">
.park-info-header {
    height: 5%;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 10px;
    border: 1px solid red;
    text-align: center;
    color: white;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    .weather-report{
        font-size: 50px;
        color: white;
    }
}

.park-info-main {
    height: 90%;
    width: 100%;
    border: 1px solid red;
    display: flex;
    div{
        flex: 1;
        margin-left: 2px;
        border: 1px solid green;
    }
}


</style>


