<template>
  <div id="app">
    <HomePageTop :isLogin.sync="isLogin"  class="simple"></HomePageTop>
    <router-view :isLogin.sync="isLogin"></router-view>
    <PageBelow class="simple" ></PageBelow>
  </div>
</template>

<script>
import PageBelow from "@/components/PageBelow.vue";
import HomePageTop from "@/components/HomePageTop.vue";
export default {
  components:{
    PageBelow,
    HomePageTop,
  },
  data(){
    return{
      isLogin:false,
      logined:false,
    }
  },
  methods:{
  },
}
</script>

<style>
#app {
}

</style>
