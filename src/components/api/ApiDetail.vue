<script>

</script>

<template>
<div class="topEst">
  <slot name="title" class="cn"></slot>
  <slot name="detail" class="cn"></slot>
  <div style="height: 20px"></div>
</div>
</template>

<style scoped>
.topEst{
  margin-left: 30px;
}
.cn{font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  cursor: default}
</style>