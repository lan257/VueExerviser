import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

const store = new Vuex.Store({
    state:{
        isLogin:false,//是否已登陆
        test:'测试',
        isShow:false,//登录窗口状态
        apiId:5,
        me: {},
    },
    mutations:{
      login(state){
          state.isLogin=!state.isLogin
      },
        login2(state){
            state.isLogin=true
        },
      show(state){
          state.isShow=!state.isShow
      },
        change(state,n){
            state.apiId=n
        },changeMyself(state,user){
            state.me=user
        },
    },

})
export default store