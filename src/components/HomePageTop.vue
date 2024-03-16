
<template>
<div class="TopEst">
<!--  这是主页顶部导航组件-->
  <router-link :to="href[item.id]" class="aBorder a1" v-for="item in choose " :key="item.id" @click="click(item.id)">
    <span style="color:white">{{ item.value }}</span>
  </router-link>
<!--  <input style="margin-left: 100px; color: RGB(36,36,36); width:700px" height="200px" type="search" v-model="search" placeholder="查询">-->
<!--  <button @click="search" style="color: aliceblue ; margin-left: 70px; font-size: 20px">查询</button>-->
<!--  v-show="isShow(item.id)"-->
<!--  <span style=" border-right:470px double black;"/>-->
  <a :href="href[item.id]" v-show="!((item.id===0&&!user)||(item.id===2&&!user)||(item.id===5&&user))" class="aBorder a2" v-for="item in choose2 " :key="item.id" @click="click(item.id)">
    <span style="color:white">{{ item.value }}</span>
  </a>
  <a v-if="user" @click="click('user')" class="aBorder a2" >
    <span style="color:white">{{ me.nickname }}</span></a>
</div>
</template>
<script>

import {GetFetch} from "@/components/fetch";

export default {
  data(){
    return{
      choose:[
        {'id':6,'value':"缘风"},
        {'id':7,'value':"Project"},
        {'id':8,'value':"API"},
         ],
      choose2:[
        {'id':0,'value':'edit'},
        {'id':1,'value':'language'},
        {'id':3,'value':'download for android'},
        {'id':4,'value':'use in web'},
        {'id':5,'value':'login'}],
      me:{},
      search:'',
      user:false,
      href:['/','/','/','#/downloadApk','#/backBonePage','#/backBonePage','/backBonePage','/Project','/api'],
    }
  },
  methods:{
    click(item){
      // alert(item);
      if (item===5){
        this.$emit('update:isLogin',!this.isLogin)
        // this.href='#/backBonePage'
      }
      else if (item===0){
        localStorage.setItem('token', '');//保存jwt
        this.user=!this.user;
      }
      else if (item===1){
        alert("你没得选")
      }
      // else if (item===0){}
      else if (item===6){this.$emit('update:isLogin',false);
        // this.href='#/backBonePage'
      }
    },
  },
  async created() {
    this.me = await GetFetch('/aaw/getUserJwt',"GET");
    this.me=this.me.data
    this.user=!this.user
  },
  props:["isLogin"],
}
</script>

<style scoped>
.TopEst{
  //height: 34px;
  background-color: black;
  //border:15px solid black;
}
.aBorder{
  //border-left: 15px solid black;
  //border-right: 15px solid black;
  //border-top-width:7px;
  ////border-bottom-width: 7px;
  //display: inline-block;
  //text-align: center;
  //line-height: 70px; /* 控制文本垂直居中 */
}
.a1{
  width: 100px;
  display: inline-block;
  text-align: center;
  line-height: 70px; /* 控制文本垂直居中 */
  float: left;
}
.a2{
  display: inline-block;
  border-right: 30px solid black;
  text-align: center;
  line-height: 70px; /* 控制文本垂直居中 */
  float: right;
}
.router-link-exact-active{
background-color: cornflowerblue;
}
</style>