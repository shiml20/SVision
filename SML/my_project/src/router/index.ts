import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import HomeView from '../views/HomeView.vue'
import StudyResources from '../components/StudyResources.vue'
import UserStore from '../components/UserStore.vue'
import VisitorsRecord from '../views/VisitorsRecord.vue'
import VehiclesRecord from '../views/VehiclesRecord.vue'
import AiCars from '../components/AiCars.vue'
import WeatherReport from '../components/WeatherReport.vue'

const routes = [
  {
    path: '/resources',
    name: 'StudyResources',
    component: StudyResources
  },
  {
    path: '/weather',
    name: 'WeatherReport',
    component: WeatherReport
  },
  {
    path: '/main',
    name: 'MainPage',
    component: MainPage,
    children: [
      {
        path: '/visitors',
        name: 'VisitorsRecord',
        component: VisitorsRecord
      },
      {
        path: '/vehicles',
        name: 'vehicles',
        component: VehiclesRecord
      },
      {
        path: '/users',
        name: 'UserStore',
        component: UserStore
      },
      {
        path: '/aicars',
        name: 'AiCars',
        component: AiCars
      },
    ]
  },
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
