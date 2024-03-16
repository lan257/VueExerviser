<script>
import ApiLeft from "@/components/ApiLeft.vue";
import ApiRight from "@/components/ApiRight.vue"
export default {
  components:{
    ApiLeft,
    ApiRight,
  },
  data(){
    return{
      apiId:1,
    }
  }
}
</script>

<template>
  <div class="TopEst">
<!--    <h1 align="center">这是api接口文档</h1>-->
    <br>
    <div class="mid">
      <ApiLeft class="left" :apiId.sync="apiId"></ApiLeft>
      <ApiRight class="right" :apiId.sync="apiId"></ApiRight>
  </div>
  </div>
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