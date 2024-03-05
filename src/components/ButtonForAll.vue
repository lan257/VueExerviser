

<template>
  <div>
  <button class="but" @click="count--" >-</button>
  {{cont}}
  <button class="but" @click="count++" >+</button></div>
</template>

<script>
export default {
  props:['cont'],
  data(){
    return {
      count:999
    }
  }
}
</script>
<style scoped>
.but{
  width: 100px;
  height: 20px;
  background-color: brown;
}
</style>