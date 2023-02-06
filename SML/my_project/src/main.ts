import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import 'qweather-icons/font/qweather-icons.css'

const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.mount('#app')