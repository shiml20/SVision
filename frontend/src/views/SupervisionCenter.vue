<template>
    <div class="b-container">
        <BasicHeader :title="title"></BasicHeader>
        <div class="center-info-main">
            <div class="carousel-1">
                <el-carousel :interval="4000" type="card" height="400px" width="300px">
                    <el-carousel-item> 
                      <MonitorCard1></MonitorCard1>
                    </el-carousel-item>
                    <el-carousel-item> 
                        <MonitorCard2></MonitorCard2>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard3></MonitorCard3>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard4></MonitorCard4>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard5></MonitorCard5>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard6></MonitorCard6>
                      </el-carousel-item>
                  </el-carousel> 
            </div>
            <div class="carousel-2">
                <el-carousel :interval="4000" type="card" height="380px" width="300px">
                    <el-carousel-item> 
                      <MonitorCard1></MonitorCard1>
                    </el-carousel-item>
                    <el-carousel-item> 
                        <MonitorCard2></MonitorCard2>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard3></MonitorCard3>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard4></MonitorCard4>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard5></MonitorCard5>
                      </el-carousel-item>
                      <el-carousel-item> 
                        <MonitorCard6></MonitorCard6>
                      </el-carousel-item>
                  </el-carousel> 
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
/* eslint-disable */
import BasicHeader from '@/components/BasicHeader.vue';
import ACard from '@/components/ACard.vue';
import MonitorCard1 from '@/components/MonitorCard1.vue';
import MonitorCard2 from '@/components/MonitorCard2.vue';
import MonitorCard3 from '@/components/MonitorCard3.vue';
import MonitorCard4 from '@/components/MonitorCard4.vue';
import MonitorCard5 from '@/components/MonitorCard5.vue';
import MonitorCard6 from '@/components/MonitorCard6.vue';

const title = "监控中心"


</script>

<style scoped lang="scss">

.center-info-main {
    height: 94%;
    width: 100%;
    //border: 1px solid red;
    margin: 1% 1% 1% 1%;
    display: flex;
    flex-direction: column;
    div {
        flex: 1;
        //border: 1px solid red;
    }
    .carousel-1 {
        height: 45%;
        margin-top: 0%;
        padding: 3% 1% 1% 1%;
        background-color: #414141;
        margin-bottom: 1%;
        margin-right: 2%;
        border-radius: 10px;
    }
    .carousel-2 {
      height: 45%;
      margin-top: 0%;
      padding: 3% 1% 1% 1%;
      background-color: #414141;
      margin-bottom: 3%;
      margin-right: 2%;
      border-radius: 10px;
  }
    
}


.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
  }


  .demo-image__error .block {
    padding: 30px 0;
    text-align: center;
    border-right: solid 1px var(--el-border-color);
    display: inline-block;
    width: 49%;
    box-sizing: border-box;
    vertical-align: top;
  }
  .demo-image__error .demonstration {
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
  }
  .demo-image__error .el-image {
    padding: 0 5px;
    max-width: 300px;
    max-height: 200px;
    width: 100%;
    height: 200px;
  }
  
  .demo-image__error .image-slot {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background: var(--el-fill-color-light);
    color: var(--el-text-color-secondary);
    font-size: 30px;
  }
  .demo-image__error .image-slot .el-icon {
    font-size: 30px;
  }
</style>


    