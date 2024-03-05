import VueRouter from 'vue-router'

import Vue from  'vue'
import ApiDoc from "@/views/ApiDoc.vue";
import BackBonePage from "@/views/BackBonePage.vue";
import downloadApk from "@/views/downloadApk.vue";
import ProjectAdress from "@/views/ProjectAdress.vue";
Vue.use(VueRouter)
const router=new VueRouter({
    routes:[
        { path: '/api',component: ApiDoc},
        { path: '/backBonePage',component:BackBonePage },
        { path: '/downloadApk',component:downloadApk },
        { path: '/Project',component:ProjectAdress },
        { path: '/',component:BackBonePage},
    ]
})
export default router