<template>
  <div class="ApiLeft">
    <h3 align="center">{{ title }}</h3>
    <div class="detail">
      <div class="left">
        <ApiDetail v-for="item in titleList" :key="item.id" :item="item" @dblclick="toggleEditMode(item)">
          <template v-slot:title>{{ item.value }}</template>
          <template v-slot:detail>
            <input v-if="item.id<3" required v-model="item.data1" v-show="item.editMode" type="text">
            <textarea v-if="item.id>2" required v-model="item.data1" style="width: 250px;height: 100px"></textarea>
<!--            <textarea readonly v-if="item.id>2" required v-model="item.data1" style="width: 250px;height: 100px" v-show="!item.editMode && item.id>2"></textarea>-->
            <span v-show="!item.editMode && item.id<3" @dblclick="item.editMode=true;title='修改接口'">{{ item.data }}</span>
          </template>
        </ApiDetail>
        <button class="leftWhite" v-show="title !== '接口'" @click="exitEdit()">退出</button>
        <button class="leftWhite" v-show="title === '接口'" @click="uploadApi()">上传接口</button>
        <button class="leftWhite" v-show="title === '上传接口'" @click="confirmUpload()">确定上传</button>
        <button class="leftWhite" v-show="title === '修改接口'" @click="updateApi()">上传修改</button>
      </div>
    </div>
  </div>
</template>

<script>
import ApiDetail from '@/components/ApiDetail.vue';
import { Fetch } from "@/components/fetch";

export default {
  data() {
    return {
      titleList: [
        { id: 0, editMode: false,value: '接口地址:', data1: '接口地址',data: '接口地址', children:'address', },
        { id: 1, editMode: false,value: '请求类型:', data1: '请求类型',data: '请求类型', children:'type',    },
        { id: 2, editMode: false,value: '接口分类:', data1: '接口分类',data: '接口分类', children:'sort',    },
        { id: 3, editMode: false,value: '接收数据:', data1: '接收数据',data: '接收数据', children:'getData', },
        { id: 4, editMode: false,value: '响应数据:', data1: '响应数据',data: '响应数据', children:'reData',  },
        { id: 5, editMode: false,value: '报错信息:', data1: '报错信息',data: '报错信息', children:'errorData'},
        { id: 6, editMode: false,value: '接口作用:', data1: '接口作用',data: '接口作用', children:'use',     },
        { id: 7, editMode: false,value: '接口备注:', data1: '接口备注',data: '接口备注', children:'other',   },
      ],
      title: "接口",
      apiId:4,
      api: {
        apiId: 4,
        address: 'address1',
        type   : 'type1',
        sort   : 'sort1',
        getData: 'getData1',
        reData : 'reData1',
        errorData: 'errorData1',
        use    : 'user1',
        other  : 'other1',
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
      alert(msg)
    },
    async updateApi() {
      this.api = this.titleList.reduce((acc, item) => {
        acc[item.children] = item.data1;
        return acc;
      }, {});
      this.api.apiId=this.apiId
      const result = await Fetch("/aaw/api", this.api, "PUT");
      alert(result.msg);
    },
  },
  async created() {
    const result = await Fetch("/api/id", this.api, "POST");
    this.api=result.data
    for (let i = 0; i < this.titleList.length; i++) {
      this.titleList[i].data = this.titleList[i].data1 = this.api[Object.keys(this.api)[i+1]];
    }
  }
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
