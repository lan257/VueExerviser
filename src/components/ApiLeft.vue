<script>
import {Fetch} from "@/components/fetch";

export default {
  data(){
    return{
      list:[
        {'id': 0, 'isShow': false, 'value': 'user'},
        {'id': 1, 'isShow': false, 'value': 'chat'},
        {'id': 2, 'isShow': false, 'value': 'commit'},
        {'id': 3, 'isShow': false, 'value': 'lOperator'},
        {'id': 4, 'isShow': false, 'value': 'video'},
        {'id': 5, 'isShow': false, 'value': 'videoSmail'},
        {'id': 6, 'isShow': false, 'value': 'api'},
        {'id': 7, 'isShow': false, 'value': 'activity'},
        {'id': 8, 'isShow': false, 'value': 'add more'}
      ],
      list2:[
        {'id':0,'value':'/sign'},
        {'id':1,'value':'/sign1'},
        {'id':2,'value':'/selectUser'},
        {'id':3,'value':'/uid/selectUser'},
        {'id':4,'value':'/getUserJwt'},
        {'id':5,'value':'/videoSmail'},
      ],
    }
  },
  methods:{
    off(item){
      this.list[item].isShow=!this.list[item].isShow;
    },
    click(id){
      if (id===8){alert('添加接口记录')}
    },
    select(id){
      this.$emit('update:apiId',id)
    }
  },

  async created() {
    const result = await Fetch("/api/all", this.api, "GET")
    this.list2=result.data
    for (const index in this.list2) {
      if (this.apiId===this.list2[index].apiId){
        for (const index2 in this.list) {
          if (this.list2[index].sort===this.list[index2].value){
            this.list[index2].isShow=true
          }}}}
  },
  props:['apiId'],
}
</script>

<template>
    <div class="ApiLeft">
      <h3 align="center" style="cursor: default;" >目录</h3>
      <div class="choose" v-for="item in list" :key="item.id" @click="click(item.id)"><a style="cursor: default;">{{item.value}}</a>
        <a v-if="item.id!==8" style="color: blue;cursor: pointer; float: right" @click="off(item.id)">{{item.isShow?'[收起]':'[展开]'}}</a><br>
        <div v-show="item.isShow">
          <div v-show="item2.sort===item.value"  class="choose2" @click="select(item2.apiId)" v-for="item2 in list2" :key="item2.apiId" :style="{backgroundColor: item2.apiId===apiId ?  'beige':'aliceblue'}">
            <a >[{{item2.type}}]{{item2.address}}</a><br></div>
      </div>
      </div>
    </div>
</template>

<style scoped>
.ApiLeft{
  margin-left: 100px;
  background-color: aliceblue;
}
.choose{
  margin-top: 30px;
  margin-left: 15px;
  //border: outset;
  //border: outset ;
}
.choose2{
  margin-top: 7px;
  margin-left: 30px;
  cursor: pointer;
  //background-color: aliceblue;
  //border: outset ;
}
</style>