<script>
export default {
  data(){
    return{
      bit:16,
      former:0,
      latter:0,
      result:0,
      result1:0,
      mathMod:'+',
      ten:[0,0,0],
      isEnd:'0+0=0',
    }
  },
  created() {
    this.former=this.getTwo()
    this.latter=this.getTwo()
    this.result=this.getTwo()
  },
  methods: {
    //二进制转十进制
    toTen(a){
      let result = 0;
      for (let i = 1; i < this.bit ; i++) {
        if (a[i]) {
          result= result+Math.pow(2,this.bit -i-1)
        }}
      return result;
    },
    startRun(){
      let res=this.runOperation(this.former,this.latter)
      this.result=this.o(res)
    },
    runOperation(a,b){
      if (this.mathMod==='+'){
        return this.ADD(a,b)
      }
      else if (this.mathMod==='-'){
        return this.minus(a,b)
      }
      else if (this.mathMod==='*'){
        return this.taken(a,b)
      }
      else {
        return this.exp(a,b)
      }
    },
    //定点整数加法(补码)
    ADD(a,b){
      return this.complement(this.Add(this.complement(a),this.complement(b)))
    },
    //无符号数加法
    Add(a,b){
      let res=this.getTwo()
      let enter = false;
      for (let i = this.bit-1; i >= 0; i--) {
        let s1=(!(a[i] && b[i])) && (a[i]||b[i])
        res[i]=(!(s1 && enter)) && (s1||enter)
        enter=(a[i] && b[i])||(enter && s1)
      }
      return res;
    },
    //定点整数减法(补码)
    minus(a,b) {
      b[0]=!b[0]
      let c= this.ADD(a,b)
      b[0]=!b[0]
      return c
    },
    //定点整数乘法
    taken(a,b) {
      let d=this.getTwo()
      for (let i = 1; i < this.bit; i++) {
        if (b[i]){
          d=this.Add(d,this.left(a,this.bit- i-1))
        }
      }
      d[0]=((!a[0]&&b[0])||(a[0]&&!b[0]))
      return d;
    },
    //定点整数除法
    exp(a,b){
      let t, c,f,e=this.getTwo()
      let d=this.o(a)
      d[0]=false
      for (let i = 1; i < this.bit; i++) {
        f=this.o(b)
        f[0]=false
        for (let j = 0; j < this.bit-1-i ; j++) {
          f = this.leftMove(f)
          if (f[1]) {
            t = j
            i = this.bit - t - 2
            break}}
        c=this.minus(d,f)
        e[i]=!c[0]
        d=c[0]?d:c
        }
      e[0]=((!a[0]&&b[0])||(a[0]&&!b[0]))
      this.result1='...'+this.toTen(d);
      return e;
    },
    //求补码
    complement(a){
      if (a[0]){
        let t=false,b=this.getTwo()
        b[0]=a[0];
        for (let i = this.bit-1; i>0 ; i--) {
          b[i]=t?!a[i]:a[i]
          t=a[i]?true:t
        }
        return b;}
      return a;
    },
    //左移i位
    left(a,i){
      let b=this.o(a);
      for (let j = 0; j < i; j++) {
        b = this.leftMove(b)
      }
      return b
    },
    //左移×2
    leftMove(a){
      let x=this.o(a);
      for (let i = 1; i < this.bit; i++) {
        x[i]=x[i+1]
      }
      x[this.bit-1]=false
      return x
    },
    //获得默认二进制值
    getTwo(){
      let x=[false,false];
      for (let i = 0; i < this.bit; i++) {
        x[i]=false
      }
      return x
    },
    //轻赋值
    o(a){
      let x=this.getTwo();
      for (let i = 0; i < this.bit; i++) {
        x[i]=a[i]
      }
      return x
    },
    //右移/2
    rightMove(a){
      let x=this.o(a);
      for (let i = this.bit-1; i >1; i--) {
        x[i]=x[i-1]
      }
      x[1]=false
      return x
    },
    //求移码
    // frameCode(a){
    //   a=this.complement(a)
    //   a[0]=!a[0]
    //   return a
    // },
    //回原码
    // reFC(a){
    //   //回补码
    //   a[0]=!a[0]
    //   //回原码
    //   return this.reCC(a)
    // },
  },
  watch:{
    former(){
      let result=this.toTen(this.former)
      this.ten[0]=this.former[0]===false?result:-result
    },
    latter(){
      let result=this.toTen(this.latter)
      this.ten[1]=this.latter[0]===false?result:-result
    },
    result(){
      let result=this.toTen(this.result)
      this.ten[2]=this.result[0]===false?result:-result
      this.isEnd=this.ten[0]+this.mathMod+this.ten[1]+"="+this.ten[2]
      if (this.mathMod==='/'){ this.isEnd+=this.result1}
    }
  }
}
</script>

<template>
<div>
  <h1 align="center">基本逻辑组件</h1>
  <table style="border: 1px solid black;">
    <tr>
      <th>被运算值</th>
      <th>运算方法</th>
      <th>运算值</th>
      <th>运行操作</th>
      <th>运算结果</th>
    </tr>
    <tr>
      <th>
        <table>
          <tr>
            <th v-for="( item,index) in former" :key="index">
              <input type="checkbox" v-model="former[index]">
            </th>
          </tr>
        </table>
      </th>
      <th>
        <select v-model="mathMod">
          <option value='+'>＋</option>
          <option value='-'>-</option>
          <option value='*'>*</option>
          <option value='/'>/</option>
        </select>
      </th>
      <th>
        <table>
          <tr>
            <th v-for="( item,index) in latter" :key="index">
              <input type="checkbox" v-model="latter[index]">
            </th>
          </tr>
        </table>
      </th>
      <th>
        <span><button @click="startRun">开始计算</button></span>
      </th>
      <th>
        <table>
          <tr>
            <th v-for="( item,index) in result" :key="index">
              <input type="checkbox" :checked="result[index]">
            </th>
          </tr>
        </table>
      </th>
    </tr>
    <tr>
      <th>{{ ten[0] }}</th>
      <th>{{ mathMod }}</th>
      <th>{{ ten[1] }}</th>
      <th>{{isEnd}}</th>
      <th>{{ ten[2] }}</th>
    </tr>
  </table>
<h1></h1>
</div>
</template>

<style scoped>

</style>