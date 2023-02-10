<template>
    <div>
        <!-- 上下布局 容器 -->
        <el-container>  
            <!-- padding颜色由background-color决定 -->
            <el-header style="width: 100%; padding: 0 32px; background-color: #000; height: 100px;">
                <div>
                    <el-menu
                    mode="horizontal"
                    background-color="#000"  
                    text-color="#fff"
                    router
                    >
                        <!-- white-space: nowrap; // 强制一行 -->
    
                        <span style="font-size: 30px; color: #088; text-align: center; line-height: 40px; white-space: nowrap; height: 100px;line-height:100px;" >智慧园区可视化管理系统</span>

                        <!-- 占位 左侧空白部分 -->
                        <el-menu-item :disabled="true" id="el-menu-item-placeholder1"></el-menu-item>

                        <!-- background-color: 设置菜单的背景颜色；text-color: 设置菜单的文字颜色 -->
                        <!-- router：让菜单支持路由导航 -->
                        <!-- 点击当前选项菜单，跳转到campSituation组件 -->
                        <!-- 导航菜单默认为垂直模式，通过将 mode 属性设置为 horizontal 来使导航菜单变更为水平模式 -->
                        <!-- Menu 还提供了background-color、text-color和active-text-color，分别用于设置菜单的背景色、菜单的文字颜色和当前激活菜单的文字颜色。 -->
                        <el-menu-item index="/situation">营区态势</el-menu-item>
                        <el-menu-item index="/manage">出入管理</el-menu-item>
                        <el-menu-item index="/point">监控点位</el-menu-item>
                        <el-menu-item index="/synthesis">流量综合</el-menu-item>
                        <el-menu-item index="/center">配置中心</el-menu-item>

                        <!-- 占位 右侧空白部分 -->
                        <el-menu-item :disabled="true" id="el-menu-item-placeholder2"></el-menu-item>

                        <span style="color: white; margin: auto;">
                            {{ nowTime }}
                        </span>
                        
                        <span style="margin: auto; ">
                            <el-button :icon="UserFilled" circle />
                            <span style="color: white; text-decoration-line: underline; padding: 8px;">Admin </span>
                        </span>

                        <span style="margin: auto">
                            <el-button :icon="SwitchButton" circle @click="Jump" />
                        </span>
                    </el-menu>
                </div>
            </el-header>
            <el-container>
                <el-main style="padding:0px">
                    <div>
                        <!-- 路由出口，即显示位置 -->
                        <router-view></router-view>
                    </div>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
  
  
<script lang="ts" setup>
// 图标 不能删
import {
    UserFilled,
    SwitchButton,
} from '@element-plus/icons-vue'

import { onMounted, reactive, toRefs } from 'vue'

import { useRouter } from 'vue-router'
const router = useRouter()

const state = reactive({
    nowTime: new Date().toLocaleString(),
})

function getnowTime() {
    setInterval(() => {
        let date = new Date();
        nowTime.value = date.toLocaleString();
    }, 1000)
}
onMounted(() => {
    getnowTime()
});
const { nowTime } = toRefs(state)

// 跳转到登陆页面
function Jump() {
    router.push("/login");
}

</script>

<style scoped>
.el-menu {
    height: 100px;
    width: 100%;
}

.el-menu-item {
    color: white;
}

/* 鼠标悬停时的样式 双引号 */
.el-menu-item:hover{
    background-color: #5a85a2 !important;
}

/* 选中时的样式 点号 */
.el-menu-item.is-active {
  background-color: #247bb4 !important;
}

#el-menu-item-placeholder1 {
    width: 12%;
    max-width: 12%;
    cursor: default;
}

#el-menu-item-placeholder2 {
    width: 15%;
    max-width: 15%;
    cursor: default;
}

.el-menu--horizontal>.el-menu-item {
    top: 30px;
    height: 60px;
    /* border-bottom: none;
    text-decoration: none; */
    font-size: 15px;
}

.icon {
    background: url(@/assets/images/admin.png);
    color: white;
   
}

</style>