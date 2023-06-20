<template>
  <div class="c-container">
    <div class="left">
      <h2 style="border-left:5px solid #000;margin-left: 5px;"> 基础信息</h2>
      <hr>
      <p>设备编号：231004</p>
      <p>设备点位：主区1号楼B1层001拐角</p>
      <p>上次检修时间：2023-02-16</p>
      <p>设备状况：正常</p>
      <p>检测人物数量：0</p>
      <p>检测车辆数量：1</p>
    </div>
    <div class="right">
      <img src="../../public/monitors/realmonitor4.png" />
    </div>
</div>
</template>

<script lang="ts" setup>
/* eslint-disable */

</script>


<style scoped lang="scss">
.c-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  background-color: black;
  color: white;
  //border: 1px solid #2cb9eb;;
  border-radius: 5px;
  .left {
    width: 35%;
  }

  .right {
    width: 55%;

    img {
      width: 100%;
      height: 100%;
    }
  }
}
</style>