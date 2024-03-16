<script>
export default {
  props:['user','color']
}
</script>

<template>
<div class="est" :style="{ backgroundColor: color===1 ?  'beige':'white'  }">
  <span class="square" style="width: 100px; height: 100px;">{{user.uid}}</span>
  <span v-if="user.uid==='用户uid'" class="block square" style="width: 100px; height: 100px;">{{user.img}}</span>
  <img  v-if="user.uid!=='用户uid'" class="square block" :src="'http://localhost:8080/uploads/'+user.img" alt="" style="width: 100px; height: 100px;" align="center">
  <span class="block square" style="width: 300px">{{user.nickname}}</span>
<!--  <span class="block square" style="width: 500px">{{user.email}}</span>-->
  <span v-if="user.uid==='用户uid'" class="block square" style="width: 150px">{{user.type}}</span>
  <span v-if="user.uid!=='用户uid'" class="block square" style="width: 150px">{{user.type===2?'用户':(user.type===1?'vip':'管理员')}}</span>
  <span class="block square" style="width: 300px">{{user.create}}</span>
</div>
</template>

<style scoped>
.est{
  margin-top:5px ;
}
.block{
  margin-top: 2px;
  margin-left: 20px;
  //background: beige;
}
.square {
  display: inline-block;
  text-align: center;
  line-height: 100px; /* 控制文本垂直居中 */
}
</style>
