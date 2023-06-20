
<template>

    <div class="aicars">
      <BasicHeader :title="title" style="background-color: black; margin-top: 0;"></BasicHeader>
  
      <div class="main">
        <div class="processed-videos">
          <img src="http://localhost:5000/video_feed">
        </div>
        <div class="videos-info">
          <!-- <img src="http://localhost:5000/video_feed1"> -->
        </div>
      </div>
  
    </div>
  
  </template>
  
  
  <script setup>
  import BasicHeader from '@/components/BasicHeader.vue';
  const title = "人工智能抓拍机制 "

  
  </script>
  
  
  <style lang="scss">
  
  .aicars {
    width: 100vw;
    height: 100vh;
    background-color: #000000;
    color: white;
    padding: 0 20px 20px 20px;
    display: flex;
    flex-direction: column;
  }
  
  .header-aicars {
    height: 50px;
    background: url('../assets/img/background1.png') no-repeat center;
    background-size: cover;
    //border: 1px solid red;
    display: flex;
    justify-content: space-between;
    align-items: center;
    div {
      //border: 1px solid red;
      flex: 1;
    }
  }
  
  .logo {
    font-size: 20px;
  }
  
  .title {
    text-align: center;
    font-size: 20px;
  }
  .time {
    text-align: center;
  }
  
  .main {
    flex: 1;
    //border: 1px solid red;
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  
  
  
    .left {
      width: 27%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
  
      .processed-videos {
        height: 58%;
        //border: 1px solid green;
        position: relative;
        .icon {
          position: absolute;
          top : 10px;
          right: 10px;
        }
      }
  
      .seller {
        height:  38%;
        //border: 1px solid green;
      }
    }
  
    .videos-info {
      width: 43%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      .map {
        height: 64%;
        //border: 1px solid green;
      }
  
      .rank {
        height:  33%;
        //border: 1px solid green;
      }
    }
  }
  
  
  </style>