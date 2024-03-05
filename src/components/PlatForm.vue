<script>
export default {
  data(){
    return{
      imgId:1,
      imgList:[],
    }
  },
  props:['title','imgUri','text'],

}
</script>

<template>
<div class="TopEst">
  <h3>{{ title }}</h3>
  <p>text</p>
<!--  <span  v-show="imgId>0" @click="imgId&#45;&#45;">《</span>-->
<!--  <img :src='imgList[imgId]' alt="" width="270px" height="200px">-->
<!--  <span  v-show="imgId<3" @click="imgId++">》</span>-->
</div>
</template>

<style scoped>
.TopEst{
  //margin-left: 150px;
  //background-color: aquamarine;
}
</style>