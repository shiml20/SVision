<template>
    <div class="common-layout">
      <el-container>
        <el-header>
            <common-header />
        </el-header>
        <el-container>
          <common-aside />
          <el-main>
            <!--Main是变化的-->
            <router-view />
          </el-main>
        </el-container>
      </el-container>
    </div>
  </template>  

<script>
import { defineComponent } from 'vue';
import CommonHeader from '../components/CommonHeader.vue';
import CommonAside from '../components/CommonAside.vue';
export default defineComponent ({
    components: {
        CommonHeader,
        CommonAside,
    },
});
</script>

<style lang="less" scoped> 
    .el-container {
        flex-wrap: wrap;
    }
    .common-layout {
        height: 100%;
        & > .el-container{
            height: 100%;
            &>.el-aside{
                height: 100%;
                background-color: #545c64;
            }
            &>.el-head{
                height: 100%;
                background-color: #545c64;
            }
        }
    }
</style>