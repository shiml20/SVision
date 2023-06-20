<template>
    <div>
      <el-card class="box-card" style="padding: 0 80 30 80;width: 400px;border-radius: 10px;">
        <div id="del-div">
          <el-link type="primary" icon="el-icon-close" @click="close()"></el-link>
        </div>
        <div style="text-align: center;">
          <h4>详 情</h4>
        </div>
        <p v-if="isInfo">部署 : 测试一下</p>
        <p v-if="isInfo">地点 : 测试一下2222</p>
        <p v-if="isInfo">说明 : 测试一下111111</p>
        <p v-if="!isInfo" style="text-align: center;color: #b3b3b3;">暂无信息</p>
        <div id="infoWindowTool">
          <el-link type="primary" @click="edit()">编辑</el-link>
          <el-link type="primary" @click="del()">删除</el-link>
        </div>
      </el-card>
      <div class="amap-info-sharp">
        <i class="el-icon-caret-bottom"></i>
      </div>
   
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        overlay: null,
        infoWindow: null,
        isInfo: true,
      };
    },
    methods: {
      initialize(e) {
        this.overlay = e.overlay;
        this.infoWindow = e.infoWindow;
      },
      //关闭
      close() {
        this.infoWindow.close();
      },
      edit() {
        console.log("编辑按钮测试");
      },
      del() {
        console.log("删除按钮测试");
      }
    }
  };
  </script>
   
  <style lang="css" scoped>
  .amap-info-sharp {
    bottom: -1px;
    left: 48.5%;
    position: absolute;
    color: #fff;
    z-index: -1;
  }
  #del-div {
    position: absolute;
    right: 20;
    top: 20;
    transform: scale(1.2);
  }
  </style>
  