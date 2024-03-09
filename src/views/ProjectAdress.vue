<script>
import ApiDetail from '@/components/ApiDetail.vue'
export default {
  components:{
    ApiDetail,
  }
}
</script>

<template>
  <div>
    <h1 align="center">项目地址</h1>
    <ApiDetail align="center"><template v-slot:title>前端Vue项目github地址:</template>
      <template v-slot:detail><br><a href="https://github.com/lan257/VueExerviser">https://github.com/lan257/VueExerviser</a></template> </ApiDetail>
    <ApiDetail align="center"><template v-slot:title>后端SpringBoot项目github地址:</template>
      <template v-slot:detail><br><a href="https://github.com/lan257/exerciser">https://github.com/lan257/exerciser</a></template></ApiDetail>
    <ApiDetail align="center">
      <template v-slot:title>Android端项目github地址:</template>
        <template v-slot:detail><br><a href=" https://github.com/lan257/AndroidExerviser">https://github.com/lan257/AndroidExerviser</a></template> </ApiDetail>
     </div>
</template>

<style scoped>

</style>