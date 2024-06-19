<!--首页页面导航-->
<script>
import LoginPage from "@/components/account/LoginPage.vue";
import AppShow from '@/components/home/AppShow.vue'
export default {
  components: {
    LoginPage,AppShow,
  },
  props:['isLogin']
}
</script>

<template>
<div class="TopEst">
<!--  中间展示页面组件-->
  <br>
  <LoginPage v-show="this.$store.state.isShow"></LoginPage>
  <AppShow v-show="!this.$store.state.isShow"/>
</div>
</template>

<style scoped>
.TopEst{
  width: 100%;
  height: 900px ;
  //height: 100%;
  align-items: stretch;
  //background: #42b983;
  background-image: url('../assets/2ba11ad9-fe7e-4977-8aea-9a878475ec41.png');

  /* 设置背景图的大小，可以是 cover（覆盖整个 div）、contain（包含在 div 内）等 */
  background-size: cover;

  /* 设置背景图的重复方式，这里是不重复 */
  background-repeat: no-repeat;

  /* 设置背景图的位置，这里是居中 */
  background-position: center center;
}
</style>