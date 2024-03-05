import Vue from 'vue'
import App from './App.vue'
Vue.config.productionTip = false
import ButtonForAll from "@/components/ButtonForAll.vue";
import router from "@/router";
Vue.component('ButtonForAll',ButtonForAll)
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
