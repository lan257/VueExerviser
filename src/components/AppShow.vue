<script>
// import PlatForm from "@/components/PlatForm.vue";
export default {
  data(){
    return{
      imgUri:[
          '@/assets/2ba11ad9-fe7e-4977-8aea-9a878475ec41.png',
          '@/assets/2ba11ad9-fe7e-4977-8aea-9a878475ec41.png',
          '@/assets/2ba11ad9-fe7e-4977-8aea-9a878475ec41.png',
          '@/assets/2ba11ad9-fe7e-4977-8aea-9a878475ec41.png',
      ],
      title:['Browser web','Android']
    }
  },
  components:{
    // PlatForm,
  }
}
</script>

<template>
  <div >
    <h1 style=" font-size: 60px; color: paleturquoise; margin-top: 60px;margin-left: 200px;">缘风，跨越诸多平台</h1>
    <h1 style=" font-size: 50px; color: paleturquoise; margin-top: 20px;margin-left: 600px;">探索用户体验的极限</h1>
    <h1 style=" font-size: 60px; color: paleturquoise; margin-top: 60px;margin-left: 270px;">期望，你述说给我的</h1>
    <h1 style=" font-size: 50px; color: paleturquoise; margin-top: 20px;margin-left: 700px;">化作正在感受的暖心</h1>
<!--    <div style="display: flex;"><div style="flex:0.6"></div>-->
<!--    <PlatForm :title="title[0]" :imgUri="imgUri" style="flex:1"></PlatForm>-->
<!--      <div style="flex:0.5"></div>-->
<!--    <PlatForm :title="title[1]" :imgUri="imgUri" style="flex:1"></PlatForm><div style="flex:0.6"></div></div>-->
  </div>
</template>

<style scoped>

</style>