<template>
    <el-row style="height:100%">
        <el-col :span="3">
            <el-menu
                background-color="#000"  
                text-color="#fff"
                router
            >
            <!-- default-active="xxx" 默认高亮的路由 -->
                <el-menu-item index="/users">
                    <el-icon>
                        <UserFilled />
                    </el-icon>
                    <span>用户管理</span>
                </el-menu-item>

                <el-menu-item index="/rule">
                    <el-icon>
                        <Bell />
                    </el-icon>
                    <span>报警规则</span>
                </el-menu-item>
            </el-menu>
        </el-col>
        <el-col :span="21">
            <router-view></router-view>
        </el-col>
    </el-row>
  </template>
  
<style>

.el-menu {
    height: 900px;
}


.el-menu-item {
  background-color: black;
}

/* 鼠标悬停时的样式 双引号 */
.el-menu-item:hover{
    background-color: #5a85a2 !important;
}

/* 选中时的样式 点号 */
.el-menu-item.is-active {
  background-color: #247bb4 !important;
}

</style>
  
<script lang="ts" setup>
import {
    UserFilled,
    Bell
} from '@element-plus/icons-vue'


</script>
