import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import 'qweather-icons/font/qweather-icons.css'

import $ from 'jquery';
import './assets/css/global.scss'

import * as ElementPlusIconsVue from '@element-plus/icons-vue'


const app = createApp(App)

app.use(ElementPlus)
app.use(router)

// 全局注册element图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }

app.mount('#app')