<template>
        <div class="info-header">
            <router-link  class='logo' to="/about" style="height: 10%; width: 10%;">
                <img  src="../assets/img/SVision2.svg" 
                alt="SVision" style="zoom: 10%;">
            </router-link>
            <div class="title">{{props.title}}</div>
            <div  class="weather-report"><WeatherReport></WeatherReport></div>
        </div>
</template>


<script lang="ts" setup>
 /* eslint-disable */ 
import WeatherReport from '@/components/WeatherReport.vue';
import ScrollerTemplate from '@/components/ScrollerTemplate.vue';
import AMap from '@/components/AMap.vue';
import MonitorsPos from '@/components/MonitorsPos.vue';

const props = defineProps({
    title:{
        type:String,
        default:''
    }
})

</script>

<style scoped lang="scss">

.b-container {
    background-color: #010013;
}
.info-header {
    background: url('../assets/img/header2.svg') no-repeat center;
    background-size: cover;
    height: 7%;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 10px;
    //border: 1px solid red;
    text-align: center;
    color: white;
    display: flex;
    justify-content: space-between;
    div {
        width: 60%;
        //border: 1px solid red;
    }
    .logo {
        padding-left: 1%;
        padding-top: 1%;
    }
    .title {
        padding-left: 17%;
        font-size: xx-large;
        padding-bottom: 2%;
    }
    .weather-report {
        padding-top: 1%;
        width: 27%;

    }
}


</style>


