<!--项目github地址导航-->
<script>
import ApiDetail from '@/components/api/ApiDetail.vue'
import userLine from "@/components/userLine.vue";
import {Fetch} from "@/tool/fetch";
export default {
  components:{
    ApiDetail,userLine
  },
  data(){
    return{
      userList:{

      },
      page:1,
      head:{
        uid:'用户uid',
        nickname:'用户昵称',
        img:'用户头像',
        // email:'用户邮箱',
        create:'用户创建时间',
        type:'用户类型',
      }
    }
  },
  async created() {
    const result = await Fetch("/aaw/selectUser", {nickname:'all'}, "POST");
    this.userList = result.data
  }
}
//background: aqua;
</script>

<template>
  <div>
    <h1 align="center" class="cn">项目地址</h1>
    <ApiDetail align="center"><template v-slot:title><span class="cn">作者github主页地址:</span></template>
    <template v-slot:detail><br><a href="https://github.com/lan257">https://github.com/lan257</a></template></ApiDetail>
    <ApiDetail align="center"><template v-slot:title><span class="cn">后端SpringBoot项目github地址:</span></template>
    <template v-slot:detail><br><a href="https://github.com/lan257/exerciser">https://github.com/lan257/exerciser</a></template></ApiDetail>
    <ApiDetail align="center"><template v-slot:title><span class="cn">前端Vue项目github地址:</span></template>
      <template v-slot:detail><br><a href="https://github.com/lan257/VueExerviser">https://github.com/lan257/VueExerviser</a></template> </ApiDetail>
    <ApiDetail align="center">
      <template v-slot:title><span class="cn">Android端项目github地址:</span></template>
      <template v-slot:detail><br><a href=" https://github.com/lan257/AndroidExerviser">https://github.com/lan257/AndroidExerviser</a>
      </template>
    </ApiDetail>


    <div class="table">
      <h2 class="cn" align="center">项目开发团队</h2>
      <span class="cn" style="float: right;color: lightgray;">(仅列出部分开发人员)</span><br>
    <userLine :user.sync="head" :color="1"></userLine>
    <div v-for="(item,index) in userList" :key="item.uid">
      <userLine :user.sync="userList[index]" :color="index%2===1?1:0"></userLine>
    </div>
      <el-pagination class="table"
          background
          layout="prev, pager, next"
          :total="1000">
      </el-pagination>
    </div>
  </div>
</template>

<style scoped>
.table{
  margin-left: 375px;
  margin-right: 435px;
}
.cn{font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  cursor: default}
</style>