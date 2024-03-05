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
  <slot><span style="color: aliceblue;">联系我们</span></slot><br>
  <span v-for ="item in this.list" :key="item.id"><a @click="Tell(item)">{{item.value}}</a><br></span>
  </div>
</template>

<style scoped>
.top-est{
  height: auto;
  width: auto;
  float: left;
  margin-left: 200px;
  margin-top: 70px;
}
</style>