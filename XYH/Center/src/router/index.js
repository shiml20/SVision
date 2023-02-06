import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        component: () => import ('../views/Main.vue'),
        redirect: '/home',
        children: [
            {
                path: '/',
                name: 'home',
                component: () => import ('../views/home/Home.vue')
            },
            {
                path:'/user',
                name:'user',
                component:() => import('../views/User/User.vue')
            },
            {
                path:'/rule',
                name:'rule',
                component:() => import('../views/Rule.vue')
            }
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router