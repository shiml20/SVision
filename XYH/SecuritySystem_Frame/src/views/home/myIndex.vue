<template>
    <div>
        <el-container>
            <el-header>
                <div style="color: #088; font-size: 25px; text-align: left;" >智慧园区可视化管理系统</div>
                    <el-menu
                    :default-active="activeIndex"
                    mode="horizontal"
                    background-color="#000"  
                    text-color="#fff"
                    router
                    >
                        <!-- background-color: 设置菜单的背景颜色；text-color: 设置菜单的文字颜色 -->
                        <!-- router：让菜单支持路由导航 -->
                        <!-- 点击当前选项菜单，跳转到campSituation组件 -->
                        <el-menu-item index="/situation">营区态势</el-menu-item>
                        <el-menu-item index="/manage">出入管理</el-menu-item>
                        <el-menu-item index="/point">监控点位</el-menu-item>
                        <el-menu-item index="/synthesis">流量综合</el-menu-item>
                        <el-menu-item index="/center">配置中心</el-menu-item>
                        <el-button class="btn1" type="primary" :icon="Edit" />
                    </el-menu>
            </el-header>
            <p></p>
            <el-container>
                <el-main>
                    <div>
                        <!-- 路由出口，即显示位置 -->
                        <router-view></router-view>
                    </div>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
  
  
<script setup>
import {  Edit } from '@element-plus/icons-vue'

</script>

<style scoped>

.el-menu {
    height: 50px;
}

.el-menu-item {
    color: white;
    
}

.btn1 {
    position: absolute;
    height:25px;
    margin: 0;
    top:10px;
    right:20px;
}

</style>