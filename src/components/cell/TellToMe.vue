<script>
export default {
  data() {
    return {
      list: [{'id': 0, 'value': 'Twitter'},
        {'id': 1, 'value': 'QQ'},
        {'id': 2, 'value': 'Wechat'},
        {'id': 3, 'value': 'tel'},
        {'id': 4, 'value': 'email'}],

    }
  },
  methods:{
    Tell(item){
      alert('正在跳转'+item.value+'中')
    }
  },

}
</script>

<template>
  <div class="top-est">
  <slot><span class="cn" style="color: aliceblue;">联系我们</span></slot><br>
  <span class="cn" v-for ="item in this.list" :key="item.id"><a @click="Tell(item)">{{item.value}}</a><br></span>
  </div>
</template>

<style scoped>
.top-est{
  height: auto;
  width: auto;
  float: left;
  margin-left: 300px;
  margin-top: 100px;
}
.cn{
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
</style>