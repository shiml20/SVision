<template>
    <div class="b-container">
        <BasicHeader :title="title"></BasicHeader>
        <div class="park-info-main">
            <div class="left">
                <SxzbqContent></SxzbqContent>
            </div>
            <div class="right">
                <SVisionContent></SVisionContent>
            </div>
        </div>
    </div>
</template>


<script lang="ts" setup>
import BasicHeader from '@/components/BasicHeader.vue';
import SVisionContent from '@/components/SVisionContent.vue';
import SxzbqContent from '@/components/SxzbqContent.vue';


const title = "基本信息"

</script>

<style scoped lang="scss">

.park-info-main {
    height: 80%;
    width: 100%;
    //border: 1px solid red;
    display: flex;
    margin-top: 3%;
    margin-left: 1%;
    justify-content: space-between;
    div {
        margin-left: 2px;
        //border: 1px solid green;
    }
    .left{
        width: 48%;
        background-color: #414141;
        
        border-radius: 10px;
    }
    .right {
       width: 48%;
        border-radius: 10px;
        margin-right: 2%;
    }

}
</style>


    