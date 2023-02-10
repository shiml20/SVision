import { createApp } from 'vue'
import App from './App.vue'

import router from './router'
import ElementPlus from 'element-plus' // 1.导入组件库 ElementPlus html
import 'element-plus/theme-chalk/index.css' // 2.导入组件的样式文件 css

import axios from 'axios' // 1.导入组件库 axios
import * as echarts from 'echarts'


const app = createApp(App) // 创建一个 Vue 实例

app.use(router) // 配置路由
app.use(ElementPlus) // 3.在 Vue 实例上配置 ElementPlus
app.config.globalProperties.$http = axios // 2.在 Vue 实例上绑定 axios
app.config.globalProperties.$echarts = echarts

app.mount('#app') // 将 id 为 app 的节点挂载到 Vue 上