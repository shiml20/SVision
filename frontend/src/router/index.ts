import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import HomeView from '../views/HomeView.vue'
import StudyResources from '../components/StudyResources.vue'
import UserRecord from '../views/UsersRecord.vue'
import VisitorsRecord from '../views/VisitorsRecord.vue'
import VehiclesRecord from '../views/VehiclesRecord.vue'
import ObjectDetection from '../views/ObjectDetection.vue'
import WareHouses from '../views/WareHouses.vue'

const routes = [
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
        name: 'UserRecord',
        component: UserRecord
      },
      {
        path: '/log',
        name: 'log',
        component: () => import('../views/LogInfo.vue')  
      }
    ]
  },
  {
    path: '/cardetection',
    name: 'cardetection',
    component: () => import('../views/CarDetection.vue')
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
  {
    path: '/info',
    name: 'info',
    component: () => import('../views/ParkInfo.vue')
  },
  {
    path: '/area',
    name: 'area',
    component: () => import('../views/AreaConditions.vue')
  },
  {
    path: '/flow',
    name: 'flow',
    component: () => import('../views/FlowInfo.vue')
  },
  {
    path: '/monitors',
    name: 'monitors',
    component: () => import('../views/MonitorsInfo.vue')
  },
  {
    path: '/geo',
    name: 'geo',
    component: () => import('../views/GeoInfo.vue')
  },
  {
    path: '/weather',
    name: 'weather',
    component: () => import('../views/WeatherInfo.vue')
  },
  {
    path: '/center',
    name: 'center',
    component: () => import('../views/SupervisionCenter.vue')
  },
  {
    path: '/facilities',
    name: 'facilities',
    component: () => import('../views/FacilitiesInfo.vue')
  },
  {
    path: '/alarm',
    name: 'alarm',
    component: () => import('../views/AlarmInfo.vue')
  },
  {
    path: '/temp',
    name: 'temp',
    component: () => import('../views/TempSs.vue')    
  },
  {
    path: '/area',
    name: 'area',
    component: () => import('../views/AreaConditions.vue')    
  },
  {
    path: '/videos',
    name: 'videos',
    component: () => import('../views/VideosPlayer.vue')  
  },
  {
    path: '/warehouses',
    name: 'WareHouses',
    component: WareHouses
  },
  {
    path: '/resources',
    name: 'StudyResources',
    component: StudyResources
  },
  {
    path: '/detection',
    name: 'Detection',
    component: ObjectDetection
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
