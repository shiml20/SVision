// createRouter 用于创建路由的实例对象
// createWebHashHistory 用于指定路由的工作模式 (hash 模式)
import { createRouter, createWebHashHistory } from "vue-router"

// 1.配置路由 @ 表示src
import Login from '@/views/login/myIndex.vue'
import Index from '@/views/home/myIndex.vue'
// 四个子页面
import Situation from '@/views/situation/myIndex.vue'
import Manage from '@/views/manage/myIndex.vue'
import Point from '@/views/point/myIndex.vue'
import Synthesis from '@/views/synthesis/myIndex.vue'
import Center from '@/views/center/myIndex.vue'

// 2.添加路由
const routes = [{
        path: '/login',
        name: 'login',
        component: Login
    },
    // 项目打开时显示的页面
    {
        path: '/',
        redirect: 'login', // 重定向到name=login的路由上
    },
    {
        path: '/index',
        name: 'index',
        component: Index,
        children: [{
                path: '/situation',
                name: 'situation',
                component: Situation,
            }, {
                path: '/manage',
                name: 'manage',
                component: Manage
            }, {
                path: '/point',
                name: 'point',
                component: Point
            }, {
                path: '/synthesis',
                name: 'synthesis',
                component: Synthesis
            }, {
                path: '/center',
                name: 'center',
                component: Center,
            }] // 子组件
    }
]

// 创建路由实例对象
const router = createRouter({
    // 指定路由工作模式：历史记录模式
    history: createWebHashHistory(),
    // 路由表
    routes: routes
})

// 向外共享路由模块
export default router