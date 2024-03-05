<script>
import ApiLeft from "@/components/ApiLeft.vue";
import ApiRight from "@/components/ApiRight.vue"
export default {
  components:{
    ApiLeft,
    ApiRight,
  }
}
</script>

<template>
  <div class="TopEst">
<!--    <h1 align="center">这是api接口文档</h1>-->
    <br>
    <div class="mid">
<ApiLeft class="left"></ApiLeft>
    <ApiRight class="right"></ApiRight>
  </div></div>
</template>

<style scoped>
.TopEst{

}
.mid{
  display: flex;
}
.left{
  flex:1
}
.right{
  flex: 3;
}
</style>