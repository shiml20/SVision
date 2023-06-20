<template>
    <div class="b-container">
        <BasicHeader :title="titleMain"></BasicHeader>
        <div class="park-info-main">
            <div class="left">
                <AMap></AMap>
            </div>
            <div class="right">
                <div class="right-1">
                    <div class="title">天气信息</div>
                    <div class="item">
                        <span><WeatherCard :title=title[0]></WeatherCard></span>
                        <span><WeatherCard :title=title[1]></WeatherCard></span>
                    </div>
                </div>
                <div class="right-2">
                    <div class="title">周边地理信息</div>
                    <div class="item">
                        <!-- <div class="item-sub"><ACard></ACard></div>
                        <div class="item-sub"><ACard></ACard></div> -->
                        <img src="..\..\public\monitors\realmonitor3.png" alt="">
                        <img src="..\..\public\monitors\realmonitor4.png" alt="">
                    </div>
                </div>
                <div class="right-3">
                    <div class="title">建设情况</div>
                    <div class="item">
                        <div>
                            <ProgressCard :percentage="90" :msg=msg[0]></ProgressCard>
                        </div>
                        <div>
                            <ProgressCard :percentage="20" :msg=msg[1]></ProgressCard>
                        </div>
                        <div>
                            <ProgressCard :percentage="30" :msg=msg[2]></ProgressCard>
                        </div>
                    </div>
                </div>
            </div> 
        </div>
    </div>
</template>


<script lang="ts" setup>
/* eslint-disable */
import AMap from '@/components/AMap.vue';
import WeatherCard from '@/components/WeatherCard.vue';
import ProgressCard from '@/components/ProgressCard.vue';
import BasicHeader from '@/components/BasicHeader.vue';

const titleMain = "综保区地理"

const msg = [
    '一期建设',
    '二期建设',
    '其他建设'
]

const title = [
    '绍兴市域天气情况',
    '重点地区天气情况'
]

</script>

<style scoped lang="scss">

.park-info-header {
    height: 5%;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 10px;
    //border: 1px solid red;

    color: white;
    display: flex;
    justify-content: space-between;
    .weather-report{
        font-size: 50px;
        color: white;
    }
}

.park-info-main {
    height: 90%;
    width: 100%;
    //border: 1px solid red;
    display: flex;
    div{
        flex: 1;
        margin-left: 2px;
        //border: 1px solid green;
    }
    .right {
        height: 100%;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        //div {
        //    border: 1px solid yellow;
        //}

    }
}

.right-1 {
    height: 44%;
    .item {
        display: flex;
        padding: 2% 4%;
        justify-content: space-between;
        width: 100%;
    }
}

.right-2 {
    height: 30%;
    .item {
        
        height: 100%;
        display: flex;
        padding: 2% 5%;
        .item-sub {
            margin-left: 2%;
            height: 100%;
        }
    }
}
.right-3 {
    height: 35%;
    padding-top: 5%;
    .title{
        height: 20%;
    }
    .item {
        height: 80%;
        display: flex;
        align-items: center;
        padding-left: 10%;
        padding-right: 10%;
    }
}


</style>


