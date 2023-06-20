<template>
    <div class="main-header">
      <router-link class='logo' to="/" style="height: 10%; width: 10%; align-items: center;">
        <img  src="../assets/img/SVision2.svg" 
        alt="SVision" style="zoom: 100%;">
      </router-link>
      <div class="main-title">智慧园区安保系统</div>
      <div class="main-weather">
        <WeatherReport></WeatherReport>
      </div>
    </div>
  
    <div class="main-layout">
      <div class="main-aside">
        <el-radio-group v-model="isCollapse" style="margin-bottom: 10px">
          <el-radio-button :label="false">展开</el-radio-button>
          <el-radio-button :label="true">收缩</el-radio-button>
        </el-radio-group>
  
        <el-menu default-active="1" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
          @close="handleClose" router background-color="#000000" text-color="#fff" active-text-color="#ffd04b">
  
        <!-- 监控中心 -->
        <el-menu-item index="center">
          <el-icon><Monitor /></el-icon>
          <template #title>监控中心</template> </el-menu-item>


        <!-- 出入管理 -->
        <el-sub-menu index="1">

          <template #title>
            <el-icon>
              <location />
            </el-icon>
            <span>出入管理</span>
          </template> 
          <el-menu-item-group>
            <el-menu-item index="vehicles">车辆进出记录</el-menu-item>
            <el-menu-item index="visitors">人员进出记录</el-menu-item>
          </el-menu-item-group>

        </el-sub-menu>
        <!-- 营区态势 -->
        <el-menu-item index="area">
          <el-icon><icon-menu /></el-icon>
          <template #title>营区态势</template> </el-menu-item>

        <!-- 监控点位 -->
        <el-menu-item index="monitors">
          <el-icon>
            <VideoCamera />
          </el-icon>
          <template #title>监控点位</template> </el-menu-item>

        <!-- 流量综合 -->
        <el-menu-item index="flow">
          <el-icon>
            <Bicycle />
          </el-icon>
          <template #title>流量综合</template> </el-menu-item>

        <!-- AI分析 -->
        <el-sub-menu index="ai">

          <template #title>
            <el-icon>
              <Platform />
            </el-icon>
            <span>AI分析</span>
          </template> 
          <el-menu-item-group>
            <template #title><span>智能选项</span></template> <el-menu-item index="cardetection">车辆分析</el-menu-item>
            <el-menu-item index="detection">人物分析</el-menu-item>
            <el-menu-item ><a href="http://127.0.0.1:5001" style="color:white; text-decoration:none;">人脸识别</a></el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
  
          <!-- 警情处理 -->
          <el-menu-item index="alarm">
            <el-icon><Bell /></el-icon>
            <template #title>警情处理</template> </el-menu-item>
  
          <!-- 地理信息 -->
          <el-menu-item index="geo">
            <el-icon><MapLocation /></el-icon>
  
            <template #title>地理信息</template> </el-menu-item>
  
          <!-- 货仓安保 -->
          <el-menu-item index="warehouses">
            <el-icon>
              <HomeFilled />
            </el-icon>
            <template #title>货仓安保</template> </el-menu-item>
  
          <!-- 工作日志 -->
          <el-menu-item index="log">
            <el-icon>
              <Document />
            </el-icon>
            <template #title>工作日志</template> </el-menu-item>
  
          <!-- 配置中心 -->
          <el-sub-menu index="5">
            <template #title>
              <el-icon>
                <setting />
              </el-icon>
              <span>配置中心</span>
            </template> <el-menu-item-group>
              <template #title><span>配置</span></template> <el-menu-item index="users">管理员信息</el-menu-item>
              <el-menu-item index="info">基本信息</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
  
        </el-menu>
  
      </div>
      <div class="main-main">
        <AboutComp></AboutComp>
      </div>
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
  import WeatherReport from '../components/WeatherReport.vue';
  import AboutComp from '../components/AboutComp.vue';
  
  
  document.title = "SVision"
  
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
  <style scoped lang="scss">
  @import url("https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Roboto:ital,wght@0,100;1,900&display=swap");
  
  .logo {
    height: 10%;
    width: 10%;
  }
  .main-header {
    background-color: #000000;
    width: 100%;
    height: 5%;
  
    //border: 1px solid red;
  
    color: white;
    display: flex;
    justify-content: space-between;
  
    div {
      flex: 1;
    }
  
    .main-title {
      //border: 1px solid red;
      padding-left: 1%;
      padding-top: 5px;
      font-size: 25px;
    }
  
    .main-weather {
      width: 30%;
      color: white;
      //border: 1px solid red;
      float: left;
    }
  }
  
  
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 100%;
    min-height: 400px;
  }
  
  .main-layout {
    width: 100%;
    height: 100%;
    font-family: "微软雅黑", "Times New Roman";
    font-size: x-large;
    font-weight: 500;
    display: flex;
  
    .main-aside {
      background-color: #000000;
      //border: 1px solid green;
      width: 10%;
    }
  
    .main-main {
      width: 90%;
    }
  
    //div {
    //  border: 1px solid red;
    //}
  }
  </style>