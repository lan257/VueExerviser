<!--  这是主页顶部导航组件-->
<template>
<div class="TopEst">

  <el-menu
      style="display: flex;justify-content: space-between"
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
    <router-link :to="href[item.id]" class="aBorder a1" v-for="item in choose " :key="item.id" @click="click(item.id)">
      <el-menu-item index="item.id"><span style="color:white">{{ item.value }}</span></el-menu-item>
    </router-link>
    <span style="flex-grow: 1" />
    <el-menu-item v-if="!this.$store.state.isLogin" index="1" @click="click(5)"><a href="#/backBonePage">login</a></el-menu-item>
<!--    {{this.proUrl}}{{this.me.img}}-->
    <el-submenu index="6" v-if="this.$store.state.isLogin">
    <template slot="title">
            <el-avatar :size="50" :src="this.proUrl+this.me.img"></el-avatar>
    </template>
      <el-submenu index="6-1" ><template slot="title">订单管理</template>
        <el-menu-item index="6-1-1"><a href="">全部订单</a></el-menu-item>
        <el-menu-item index="6-1-2"><a href="">最近订单</a></el-menu-item>
        <el-menu-item index="6-1-3"><a href="">购物车</a></el-menu-item>
      </el-submenu>
      <el-menu-item index="6-3" ><router-link to="/dishes">菜品管理</router-link></el-menu-item>
      <el-menu-item index="6-4" ><template slot="title"><el-button type="text" @click="open">修改地址</el-button></template>
      </el-menu-item>
<!--      <el-menu-item index="6-4" ><span>修改地址</span></el-menu-item>-->
      <el-menu-item index="6-5" ><span @click="click(0)">退出登录</span></el-menu-item>
    </el-submenu>
    <el-menu-item index="3"><a href="#/kainghe" @click="click(4)">kainghe</a></el-menu-item>
    <el-menu-item index="4"><a href="#/downloadApk" @click="click(3)">use in android</a></el-menu-item>
    <el-menu-item index="5"><a href="#/mindMap" >mindMap</a></el-menu-item>
    <el-submenu index="2">
    <template slot="title">language</template>
    <el-menu-item index="2-1" ><span @click="alert('已切换')">chinese</span></el-menu-item>
      <el-menu-item index="2-2"><span @click="alert('未开发')">English(未开发)</span></el-menu-item>
      <el-menu-item index="2-3"><span @click="alert('未开发')">Japanese(未开发)</span></el-menu-item>
   </el-submenu>

<!--    <el-menu-item index="5"><a :href="href[0]" v-show="this.$store.state.isLogin"  @click="click(0)"><span style="color:white">exit</span></a></el-menu-item>-->
  </el-menu>
</div>
</template>
<!--  <router-link :to="href[item.id]" class="aBorder a1" v-for="item in choose " :key="item.id" @click="click(item.id)">-->
<!--    <span style="color:white">{{ item.value }}</span>-->
<!--  </router-link>-->
<!--  <input style="margin-left: 100px; color: RGB(36,36,36); width:700px" height="200px" type="search" v-model="search" placeholder="查询">-->
<!--  <button @click="search" style="color: aliceblue ; margin-left: 70px; font-size: 20px">查询</button>-->
<!--  v-show="isShow(item.id)"-->
<!--  <span style=" border-right:470px double black;"/>-->
<!--  <a :href="href[0]" v-show="this.$store.state.isLogin" class="aBorder a2" @click="click(0)">-->
<!--    <span style="color:white">exit</span>-->
<!--  </a>-->
<!--  <a :href="href[item.id]" class="aBorder a2" v-for="item in choose2 " :key="item.id" @click="click(item.id)">-->
<!--    <span style="color:white">{{ item.value }}</span>-->
<!--  </a>-->
<!--  <a :href="href[5]" v-if="!this.$store.state.isLogin" class="aBorder a2" @click="click(5)">-->
<!--    <span style="color:white">login</span>-->
<!--  </a>-->

<!--  <a :href="href[9]" v-show="this.$store.state.isLogin" class="aBorder a2" >-->
<!--    <span style="color:white" >{{ me.nickname }}</span></a>-->

<script>

import {GetFetch ,Fetch, vid } from "@/tool/fetch";
import { mapMutations} from "vuex";
// import login from "@/store/login";

export default {
  data(){
    return{
      choose:[
        {'id':6,'value':"缘风"},
        {'id':7,'value':"Project"},
        {'id':8,'value':"API"},
         ],
      choose2:[
        {'id':1,'value':'language'},
        {'id':2,'value':'mindMap'},
        {'id':3,'value':'download for android'},
        {'id':4,'value':'kainghe'},],
      me:{},
      result:{},
      proUrl:'',
      search:'',
      // user:false,
      href:['/','/','/','/downloadApk','/kainghe','/backBonePage','/backBonePage','/Project','/api','/personCenter','/mindMap'],
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    ...mapMutations(['login', 'show', 'login2','changeMyself']),
    click(item) {
      if (item === 5) {
        this.show()
        // this.login();
        // this.$emit('update:isLogin',!this.isLogin)
        // this.href='#/backBonePage'
      } else if (item === 0) {
        localStorage.setItem('token', '');//保存jwt
        this.login2()
        this.login();
        // this.user=!this.user;
      } else if (item === 1) {
        alert("你没得选")
      }
      // else if (item===0){}
      else if (item === 6) {
        this.login()
        // this.$emit('update:isLogin',false);
        // this.href='#/backBonePage'
      }

    },
    async update() {
      await Fetch('/aaw/baUpdate', this.me, "POST");
    },
    open() {
      this.$prompt('请输入地址', '修改收货地址', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
      }).then(({ value }) => {
        this.me.buyAddress = value
        this.update();
        this.$message({
          type: 'success',
          message: '你的地址是: ' + value
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        });
      });
    },
  },
  async created() {
    this.proUrl=vid +'/uploads';
    this.me = await GetFetch('/aaw/getUserJwt');
    this.login2()
    if(this.me.iu===0){
      localStorage.setItem('token', '');
      this.login2()
      alert("校验失败")
      this.login();
    }
    else {
    this.me=this.me.data
    this.me =await Fetch('/aaw/uid/selectUser',this.me,"POST");
    this.me=this.me.data
    this.changeMyself(this.me)}
    // // this.user=!this.user
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
  border-radius: 0;
  //border-left: 15px solid black;
  //border-right: 15px solid black;
  //border-top-width:7px;
  ////border-bottom-width: 7px;
  //display: inline-block;
  //text-align: center;
  //line-height: 70px; /* 控制文本垂直居中 */
}
.a1{
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","楷体",Arial,sans-serif;
  width: 100px;
  display: inline-block;
  text-align: center;
  line-height: 70px; /* 控制文本垂直居中 */
  float: left;
}
.a2{
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","楷体",Arial,sans-serif;
  display: inline-block;
  border-right: 30px solid black;
  text-align: center;
  cursor: pointer;
  line-height: 70px; /* 控制文本垂直居中 */
  float: right;
}
</style>