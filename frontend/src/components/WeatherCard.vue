<template>
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>{{props.title}}</span>
            <a href="http://www.baidu.com" style="color:white; text-decoration:none;">
                <el-button class="button" text >{{props.buttonDescription}}</el-button>
            </a>
        </div>
      </template>
      <div>今天 &nbsp;|&nbsp; 0218&nbsp;  🌤&nbsp;  0℃~9℃</div>
      <div>明天 &nbsp;|&nbsp; 0219&nbsp;  ⛅&nbsp; 2℃~11℃</div>
      <div>周一 &nbsp;|&nbsp; 0220&nbsp;  🌤&nbsp;  2℃~9℃</div>
      <div>周二 &nbsp;|&nbsp; 0221&nbsp;  ⛅&nbsp; 4℃~13℃</div>
    </el-card>
    
  </template>
  
<script setup>
/* eslint-disable */
import { ref, onMounted, defineExpose } from 'vue';
import * as echarts from 'echarts'

const props = defineProps({
    title:{
        type: String,
        default: "Card name"
    },
    buttonDescription:{
        type: String,
        default: "点击获取更多信息"
    }

})



</script>


  <style>
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .text {
    font-size: 14px;
  }
  
  .item {
    margin-bottom: 18px;
  }
  
  .box-card {
    width: 100%;
    height: 100%;
    position: relative;
    background-color: white;
    color: black;
  }
  </style>
  