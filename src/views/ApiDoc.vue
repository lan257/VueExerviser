
//api文档交互导航页面
<script>
import ApiRight from "@/components/api/ApiRight.vue"
import ApiLeft from "@/components/api/ApiLeft.vue";
export default {
  components:{
    ApiRight,
    ApiLeft,
  },
}
</script>

<template>
  <div class="TopEst">
<!--    <h1 align="center">这是api接口文档</h1>-->
    <br>
    <div class="mid">
      <ApiLeft class="left" ></ApiLeft>
      <ApiRight class="right" ></ApiRight>
  </div>
  </div>
</template>

<style scoped>
.TopEst{

}
.mid{
  display: flex
}
.left{
  flex: 1
}
.right{
  flex: 3
}
</style>