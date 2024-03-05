<script>
import TellToMe from "@/components/TellToMe.vue";
export default {
  components: {
    TellToMe,
  }
}
</script>

<template>
  <div class="down">
    <div style="height:50px;"/>
    <div class="in" >
    <TellToMe/><TellToMe/><TellToMe/><TellToMe/><TellToMe/>
    </div>
    <div style="height:50px "/>
</div>
</template>

<style scoped>
.down{
  width: 100%;
  height: 470px;
  left: 0;
  bottom: 0;
  background-color: RGB(36,36,36) ;
}
.in{
  width: 70%; /* 设置宽度为父元素宽度的70% */
  height: 70%;
  margin:  auto; /* 水平居中 */
}
</style>