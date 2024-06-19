<script>
export default {
  props:['user','color']
}
</script>

<template>
<div class="est" :style="{ backgroundColor: color===1 ?  'beige':'white'  }">
  <span class="square cn" style="width: 100px; height: 100px;">{{user.uid}}</span>
  <span v-if="user.uid==='用户uid'" class="block square cn" style="width: 100px; height: 100px;">{{user.img}}</span>
  <img  v-if="user.uid!=='用户uid'" class="square block" :src="'http://localhost:8080/uploads/'+user.img" alt="" style="width: 100px; height: 100px;" align="center">
  <span class="block square cn" style="width: 300px">{{user.nickname}}</span>
<!--  <span class="block square" style="width: 500px">{{user.email}}</span>-->
  <span v-if="user.uid==='用户uid'" class="block square cn" style="width: 150px">{{user.type}}</span>
  <span v-if="user.uid!=='用户uid'" class="block square cn" style="width: 150px">{{user.type===2?'用户':(user.type===1?'vip':'管理员')}}</span>
  <span class="block square cn" style="width: 300px">{{user.create}}</span>
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
.cn{font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  cursor: default}
</style>
