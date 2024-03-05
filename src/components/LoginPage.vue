<script>
import {Fetch} from './fetch.js'
export default {

  data(){
    return{
      control:"登录",
      user:
          {
            email: "000@root.com",
            password: "476831",
          },
      isRemember:true,
      isAuto:false,
      isSure:true,
    }
  },
  methods:{
    sign(){
      this.control="注册"
    },
    async login() {
      event.preventDefault(); // 阻止按钮的默认行为
      console.log("登录操作")
      const result= await Fetch("/aaw/login", this.user,"POST");
      alert(result.msg)
      localStorage.setItem('token', result.data);//保存jwt
      window.location.reload();
    }
  }
}
</script>
<template>
  <div class="top-est">
    <div style="height: 40px"></div>
    <div class="loginForm">
    <form>
      <h3 align="center">{{control}}</h3>
      <span v-if="control!=='注册'"><br><br><br><br><br></span>
      <span v-if="control==='注册'">选择头像：<input type="file"></span>
      邮箱：<input type="email" name="email" v-model="user.email" pattern="/^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/" required><br>
      密码：<input type="password" name="password" v-model="user.password" required><br>
      <input  type="checkbox" v-model="isRemember">记住密码
      <input style="margin-left:40px" type="checkbox" v-model="isAuto">自动登录
      <br>
      <button @click="login" style="margin-left:90px" >{{control}}</button>
      <span v-if="control==='注册'">
      <br><input type="checkbox" v-model="isSure"><span>我已知情并同意《缘风相关规定》</span></span>
    <span v-if="control!=='注册'"><br><a style=" border-right:80px double aquamarine;" @click="sign">免费注册账号</a><a>忘记密码</a></span>
    </form>
  </div></div>
</template>

<style scoped>
.loginForm{
  float: right;
  width: 240px;
  height: auto;
  border: outset;
  margin-right: 50px;
  background-color: aquamarine;
}
</style>