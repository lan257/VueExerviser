
<template>
<div class="TopEst">
<!--  这是主页顶部导航组件-->
  <router-link :to="href[item.id]" class="aBorder a1" v-for="item in choose " :key="item.id" @click="click(item.id)">
    <span style="color:white">{{ item.value }}</span>
  </router-link>
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
      // else if (item===7){this.href='#/api'}
      // else if (item===8){this.href='#/api'}
      // else if (item===3){this.href='#/downloadApk'}
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
  height: 30px;
  background-color: black;
  border:15px solid black;
}
.aBorder{
  border: 15px solid black;
  border-top-width:7px;
  border-bottom-width: 7px;
}
.a1{
  float: left;
}
.a2{
  float: right;
}
</style>