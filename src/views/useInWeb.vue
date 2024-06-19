<!--课设基本功能实现-->
<script>
export default{
  methods:{
    exit(){
      localStorage.setItem('token', '');//保存jwt
    }
  }
}
</script>

<template>
<div>
  <h1>use in web</h1>
  <h2>菜品管理</h2>
  <h3>批量删除</h3>
  <h3>起售停售</h3>
  <h2>订单管理</h2>
  <h3>修改</h3>
  <h3>起售停售</h3>
  <h2>订单明细</h2>
  <h2>购物车</h2>
  <h3 onclick="alert('已清空')">删除购物车中的商品</h3>
</div>
</template>

<style scoped>

</style>