<template>
  <div class="ApiLeft">
    <h3 align="center">{{ title }}</h3>
    <div class="detail">
      <div class="left">
<!--        是{{this.$store.state.apiId}}-->
        <ApiDetail v-for="item in titleList" :key="item.id" :item="item" @dblclick="toggleEditMode(item)">
          <template v-slot:title ><span style="cursor: default;">{{ item.value }}</span></template>
          <template v-slot:detail>
            <input v-if="item.id===0" required v-model="item.data1" v-show="item.editMode" type="text">
            <textarea v-if="item.id>2" required v-model="item.data1" style="width: 250px;height: 100px"></textarea>
            <select v-if="item.id===1" v-model="item.data1" v-show="item.editMode">
              <option value="GET">GET</option>
              <option value="POST">POST</option>
              <option value="PUT">PUT</option>
              <option value="DEL">DEL</option>
            </select>
            <select v-if="item.id===2" v-model="item.data1" v-show="item.editMode">
              <option value='user'       >user</option>
              <option value='chat'       >chat</option>
              <option value='commit'     >commit</option>
              <option value='lOperator'  >lOperator</option>
              <option value='video'      >video</option>
              <option value='videoSmail' >videoSmail</option>
              <option value='api'        >api</option>
              <option value='activity'   >activity</option>
              <option value='dishes'     >dishes</option>
              <option value='order'      >order</option>
            </select>
            <!--            <textarea readonly v-if="item.id>2" required v-model="item.data1" style="width: 250px;height: 100px" v-show="!item.editMode && item.id>2"></textarea>-->
            <span v-show="!item.editMode && item.id<3" @dblclick="item.editMode=true;title='修改接口'">{{ item.data }}</span>
          </template>
        </ApiDetail>
        <el-button type="success" plain  class="leftWhite" v-show="title !== '接口'" @click="exitEdit()">退出</el-button>
        <el-button type="success" plain  class="leftWhite" v-show="title === '接口'" @click="uploadApi()">上传接口</el-button>
        <el-button type="success" plain class="leftWhite" v-show="title === '上传接口'" @click="confirmUpload()">确定上传</el-button>
        <el-button type="success" plain  class="leftWhite" v-show="title === '修改接口'" @click="updateApi()">上传修改</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import ApiDetail from '@/components/api/ApiDetail.vue';
import { Fetch } from "@/tool/fetch";
import {mapState}  from "vuex";

export default {
  data() {
    return {
      titleList: [
        { id: 0, editMode: false,value: '接口地址:', data1: '接口地址',data: '接口地址', children:'address'  },
        { id: 1, editMode: false,value: '请求类型:', data1: '请求类型',data: '请求类型', children:'type'     },
        { id: 2, editMode: false,value: '接口分类:', data1: '接口分类',data: '接口分类', children:'sort'     },
        { id: 3, editMode: false,value: '接收数据:', data1: '接收数据',data: '接收数据', children:'getData'  },
        { id: 4, editMode: false,value: '响应数据:', data1: '响应数据',data: '响应数据', children:'reData'   },
        { id: 5, editMode: false,value: '报错信息:', data1: '报错信息',data: '报错信息', children:'errorData'},
        { id: 6, editMode: false,value: '接口作用:', data1: '接口作用',data: '接口作用', children:'use'      },
        { id: 7, editMode: false,value: '接口备注:', data1: '接口备注',data: '接口备注', children:'other'    },
      ],
      title: "接口",
      api: {
        apiId: 4,
      },
    };
  },
  components: {
    ApiDetail
  },
  methods: {
    toggleEditMode(item) {
      item.editMode = !item.editMode;
      if (item.editMode) this.title = '修改接口';
      else item.data1 = item.data;
    },
    exitEdit() {
      this.title = '接口';
      this.titleList.forEach(item => {
        item.editMode = false;
        item.data1 = item.data;
      });
    },
    async uploadApi() {
      this.titleList.forEach(item => {
        item.editMode = true;
        item.data1 = "";
      });
      this.title = '上传接口';
    },
    async confirmUpload() {
      this.api = this.titleList.reduce((acc, item) => {
        acc[item.children] = item.data1;
        return acc;
      }, {});
      // console.log(this.api);
      const msg = await Fetch("/aaw/api", this.api, "POST");
      alert(msg.msg)
      await this.updateApiData();
    },
    async updateApi() {
      this.api = this.titleList.reduce((acc, item) => {
        acc[item.children] = item.data1;
        return acc;
      }, {});
      this.api.apiId=this.$store.state.apiId
      const result = await Fetch("/aaw/api", this.api, "PUT");
      alert(result.msg);
      await this.updateApiData();
    },
    async updateApiData() {
      this.api.apiId = this.$store.state.apiId
      const result = await Fetch("/api/id", this.api, "POST");
      this.api = result.data
      for (let i = 0; i < this.titleList.length; i++) {
        this.titleList[i].data = this.titleList[i].data1 = this.api[Object.keys(this.api)[i + 1]];
      }
    }
  },
  async created() {
    await this.updateApiData();
  },
  computed:{
    ...mapState(['apiId'])
  },
  watch:{
    async apiId(){
      // alert(this.$store.state.apiId)
      // alert("重置api展示"+this.apiId);
      await this.updateApiData();
    }
  },
};
</script>


<style scoped>
.ApiLeft{
  margin-left: 100px;
  margin-right: 100px;
  background-color: aliceblue;
}
.leftWhite{
  margin-left: 50px;
}
</style>
