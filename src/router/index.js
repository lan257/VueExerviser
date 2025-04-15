import VueRouter from 'vue-router'
//导航
import Vue from  'vue'
import ApiDoc from "@/views/ApiDoc.vue";
import BackBonePage from "@/views/BackBonePage.vue";
import downloadApk from "@/views/downloadApk.vue";
import ProjectAddress from "@/views/ProjectAdress.vue";
import personCenter from '@/views/personCenter.vue';
import dishesMange from '@/views/dishesMange.vue';
import mindMap from "@/components/mindMap/mindMap.vue";
import write from "@/components/kainghe/write.vue";
Vue.use(VueRouter)
const router=new VueRouter({
    routes:[
        { path: '/api',component: ApiDoc},
        { path: '/backBonePage',component:BackBonePage },
        { path: '/downloadApk',component:downloadApk },
        { path: '/Project',component:ProjectAddress },
        { path: '/personCenter',component:personCenter },
        { path: '/dishes',component:dishesMange },
        { path: '/',component:BackBonePage },
        { path: '/mindMap',component:mindMap},
        { path: '/kainghe',component:write},
    ]
})

export default router