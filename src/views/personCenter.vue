<!--个人中心导航页面-->
<script>
import { Fetch } from "@/tool/fetch";
export default{
  data(){
    return{
      user:{'buyAddress':''},
      isChange:false,
    }
  },
  methods:{
    exit(){
      localStorage.setItem('token', '');//保存jwt
      alert('登出成功')
    },
    async update() {
      const result = await Fetch('/aaw/baUpdate', this.user, "POST");
      alert(result.msg)
    }
  }
}
</script>

<template>
  <div>
  <h1>个人中心</h1>
    <h2 @click="exit()"><a :href="'/'" class="a2">退出登录</a></h2>
    <h2> 最新订单查询</h2>
    <h2> 历史订单</h2>
    <h2 class="a2" @click="isChange=!isChange"> 地址管理-修改地址</h2>
    <input v-if="isChange" type="text" v-model="user.buyAddress">
    <input @click="update()" type="button" v-if="isChange" readonly value="√">
  </div>
</template>

<style>
.a2{
  cursor: pointer;
}
</style>