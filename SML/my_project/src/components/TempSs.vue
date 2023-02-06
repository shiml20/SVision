<template>
  
  <!-- <el-sub-menu index="2">
      <template #title>Workspace</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="3" disabled>Info</el-menu-item>
    <el-menu-item index="4">Orders</el-menu-item>
  <div class="h-6" /> -->
  <div class="header">
    <h1 class="h1-text" index="/users"><img src="/assets/logo.png" alt="logo" style="zoom:25%">
      SVison - Smart Security System</h1>
    <WeatherReport></WeatherReport>
  </div>

  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
          <el-radio-button :label="false">展开</el-radio-button>
          <el-radio-button :label="true">收缩</el-radio-button>
        </el-radio-group>
        <el-menu default-active="1" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
          @close="handleClose" router>
          <el-sub-menu index="1">
            <template #title>
              <el-icon>
                <location />
              </el-icon>
              <span>出入管理</span>
            </template>
            <el-menu-item-group>
              <template #title><span>Group One</span></template>
              <el-menu-item index="cars">车辆进出记录</el-menu-item>
              <el-menu-item index="persons">人员进出记录</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group Two">
              <el-menu-item index="1-3">item three</el-menu-item>
            </el-menu-item-group>
            <el-sub-menu index="1-4">
              <template #title><span>item four</span></template>
              <el-menu-item index="1-4-1">item one</el-menu-item>
            </el-sub-menu>
          </el-sub-menu>
          <el-menu-item index="2">
            <el-icon><icon-menu /></el-icon>
            <template #title>营区态势</template>
          </el-menu-item>
          <el-menu-item index="3" disabled>
            <el-icon>
              <document />
            </el-icon>
            <template #title>监控点位</template>
          </el-menu-item>
          <el-menu-item index="4">
            <el-icon>
              <setting />
            </el-icon>
            <template #title>流量综合</template>
          </el-menu-item>

          <el-sub-menu index="5">
            <template #title>
              <el-icon>
                <location />
              </el-icon>
              <span>AI分析</span>
            </template>
            <el-menu-item-group>
              <template #title><span>Group One</span></template>
              <el-menu-item index="aicars">车辆分析</el-menu-item>
              <el-menu-item index="persons">人物分析</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group Two">
              <el-menu-item index="1-3">item three</el-menu-item>
            </el-menu-item-group>
            <el-sub-menu index="1-4">
              <template #title><span>item four</span></template>
              <el-menu-item index="1-4-1">item one</el-menu-item>
            </el-sub-menu>
          </el-sub-menu>
          

          <el-menu-item index="6">
            <el-icon>
              <setting />
            </el-icon>
            <template #title>配置中心</template>
          </el-menu-item>


          <el-menu-item index="7">
            <el-icon>
              <setting />
            </el-icon>
            <template #title>气象信息</template>
          </el-menu-item>

          
          <el-menu-item index="8">
            <el-icon>
              <setting />
            </el-icon>
            <template #title>工作日志</template>
          </el-menu-item>

          <el-menu-item index="8">
            <el-icon>
              <setting />
            </el-icon>
            <template #title>货物管理</template>
          </el-menu-item>

        </el-menu>
      </el-aside>
      <router-view></router-view>
      <!-- <el-container>  

        <el-main>我是存在的！！</el-main>
      </el-container> -->
    </el-container>
  </div>




</template>
  
<script lang="ts" setup>
/* eslint-disable */
import { ref } from 'vue'
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
import WeatherReport from './WeatherReport.vue';


const activeIndex = ref('users')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}


const isCollapse = ref(false)
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>
  
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Roboto:ital,wght@0,100;1,900&display=swap");

.header {
 display: flex;
}

.h1-text {
  color: #409EFF;
  margin: 1%;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

.common-layout {
  font-family: "宋体", "Times New Roman";
}
</style>