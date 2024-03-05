<script>
export default {
data(){
  return{
    cont:9999
  }
}
}
</script>

<template>
  <div class="heard">
    我是顶页<br>
    <ButtonForAll :cont="cont"></ButtonForAll>
    <ButtonForAll></ButtonForAll>
    <ButtonForAll></ButtonForAll>
  </div>
</template>

<style>
.heard{
  height: 100px;
  width: 100%;
  background-color: azure;
  align-items: center;
}
</style>