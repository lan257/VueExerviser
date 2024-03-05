<script>
export default {
  data(){
    return{
      list:[
    {'id':0,'isShow':false,'value':'user'},
    {'id':1,'isShow':false,'value':'chat'},
    {'id':2,'isShow':false,'value':'commit'},
    {'id':3,'isShow':false,'value':'lOperator'},
    {'id':4,'isShow':false,'value':'video'},
    {'id':5,'isShow':false,'value':'videoSmail'},
        {'id':6,'isShow':false,'value':'add'}
      ],
      list2:[
        {'id':0,'value':'/sign'},
        {'id':1,'value':'/sign1'},
        {'id':2,'value':'/selectUser'},
        {'id':3,'value':'/uid/selectUser'},
        {'id':4,'value':'/getUserJwt'},
        {'id':5,'value':'videoSmail'},
      ]
    }
  },
  methods:{
    off(item){
      this.list[item].isShow=!this.list[item].isShow;
    },
    click(id){if (id===6){alert('添加接口记录')}}
  }
}
</script>

<template>
    <div class="ApiLeft">
      <h3 align="center">目录</h3>
      <div class="choose" v-for="item in list" :key="item.id" @click="click(item.id)"><a>{{item.value}}</a><a v-if="item.id!==6" style="float: right" @click="off(item.id)">{{item.isShow?'收起':'展开'}}</a><br>
        <div v-show="item.isShow"><div class="choose2" v-for="item2 in list2" :key="item2.id"><a >{{item2.value}}</a><br></div>
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
  //border: outset ;
}
</style>