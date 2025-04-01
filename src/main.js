import Vue from 'vue'
import App from './App.vue'
Vue.config.productionTip = false
import ButtonForAll from "@/components/cell/ButtonForAll.vue";
import router from "@/router";
import store from "@/store/login"
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import apiStore from "@/store/api"
Vue.component('ButtonForAll',ButtonForAll)
Vue.use(ElementUI, { size: 'small', zIndex: 3000 })
new Vue({
  render: h => h(App),
  router,
  store,
  // d3,


  // apiStore,
}).$mount('#app')
