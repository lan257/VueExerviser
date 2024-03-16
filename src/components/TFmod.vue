<script>
export default {
  data(){
    return{
      former:[false,false,false,false,false,false,false,false],
      latter:[false,false,false,false,false,false,false,false],
      result:[false,false,false,false,false,false,false,false],
      mathMod:'+',
      ten:[0,0,0],
      isEnd:'0+0=0',
    }
  },
  methods: {
    startRun(){
      let res=this.runOperation(this.former,this.latter)
      // alert(res)
      this.result=[res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7]]
    },
    runOperation(a,b){
      if (this.mathMod==='+'){
        if (!a[0]&&!b[0]){return this.Add(a,b)}
        else if (a[0]&&b[0]){
          let res= this.Add(a,b)
          res[0]=true
          return res
        }
        else if (a[0]&&!b[0]){
          let e =[!a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]]
          return this.minus(b, e)
        }else {
          let d =[!b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]]
          return this.minus(a, d)
        }
      }
      else if (this.mathMod==='-'){
        if (!a[0]&&!b[0]){return this.minus(a,b);}
        else if (a[0]&&b[0]){
          let d =[!b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]]
          let e =[!a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]]
          return this.minus(d, e)
        }
        else if (a[0]&&!b[0]){
          let e =[!a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]]
          let res=this.Add(e,b)
          res[0]=!res[0]
          return res
        }else {
          let d =[!b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]]
          let res=this.Add(a,d)
          res[0]=!res[0]
          return res
        }
      }
      else if (this.mathMod==='*'){
        return this.taken(a,b)
      }
      else {
        return this.exp(a,b)
      }
    },
    Add(c,d){
      let a=[c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7]]
      let b=[d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]]
      let res=[false,false,false,false,false,false,false,false]
      let enter = false;
      for (let i = this.former.length-1; i >= 0; i--) {
        let s1=(!(a[i] && b[i])) && (a[i]||b[i])
        res[i]=(!(s1 && enter)) && (s1||enter)
        enter=(a[i] && b[i])||(enter && s1)
      }
      return res;
    },
    minus(a,b) {
      let d =[b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7]]
      let res=[!b[0],!b[1],!b[2],!b[3],!b[4],!b[5],!b[6],!b[7]]
      let e=[a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]]
      let c=[false,false,false,false,false,false,false,true]
      d=this.Add(res,c)
      res=this.Add(this.complement(e),d)
      if (res[0]){
        let i
        for(i=7;!res[i];i--){
          console.log(res[i])
        }
        for (let j=i-1;j>0;j--){
          res[j]=!res[j]
        }
      }
      return res
    },
    taken(a,b) {
      let c,d=0
      for (let i = 1; i < this.former.length; i++) {
        if (b[i]){
          c=a
          for (let j = 0; j <this.former.length- i-1; j++) {
            c=this.leftMove(c)
          }
          d=this.Add(d,c)
        }
      }
      d[0]=((!a[0]&&b[0])||(a[0]&&!b[0]))
      return d;
    },
    exp(a,b){
      let t=0, c,f,e=[false,false,false,false,false,false,false,false]
      let d=[false,a[1],a[2],a[3],a[4],a[5],a[6],a[7]]
      for (let i = 1; i < this.former.length; i++) {
        f=[false,b[1],b[2],b[3],b[4],b[5],b[6],b[7]]
        for (let j = 0; j < this.former.length-1-i ; j++) {
          f = this.leftMove(f)
          if (f[1]) {
            t = j
            i = this.former.length - t - 2
            break}}
        c=this.minus(d,f)
        e[i]=!c[0]
        d=c[0]?d:c
        }
      e[0]=((!a[0]&&b[0])||(a[0]&&!b[0]))
      return e;
    },
    //左移×2
    leftMove(a){
      return [a[0],a[2],a[3],a[4],a[5],a[6],a[7],false]
    },
    //右移/2
    rightMave(a){
      return [a[0],false,a[1],a[2],a[3],a[4],a[5],a[6]]
    },
    //求反码
    againCode(a){
      if (a[0]){
        for (let i = 1; i < this.former.length; i++) {
          a[i]=!a[i]}}
      return a;
    },
    //回原码
    reAC(a){
      return this.againCode(a)
    },
    //求补码
    complement(a){
      if (a[0]) {
      let b=[false,false,false,false,false,false,false,true]
        a=this.Add(this.againCode(a),b)
      }
      return a;
    },
    //回原码
    reCC(a){
      let i,b
      for (i = this.former.length-1;a[i];i--){b[i]=a[i]}
      for (let j = i-1; j > 0; i--) { b[j]=!a[j]}
      alert(b)
      return b
    },
    //求移码
    frameCode(a){
      a=this.complement(a)
      a[0]=!a[0]
      return a
    },
    //回原码
    reFC(a){
      //回补码
      a[0]=!a[0]
      //回原码
      return this.reCC(a)
    },

  },
  watch:{
    former(){
      let result = 0;
      for (let i = 1; i < this.former.length ; i++) {
        if (this.former[i]) {
          result= result+Math.pow(2,this.former.length -i-1)
        }}
      this.ten[0]=this.former[0]===false?result:-result
      this.isEnd=this.ten[0]+this.mathMod+this.ten[1]+"="+this.ten[2]
    },
    mathMod(){
      this.isEnd=this.ten[0]+this.mathMod+this.ten[1]+"="+this.ten[2]
    },
    latter(){
      let result = 0;
      for (let i = 1; i < this.latter.length; i++) {
        if (this.latter[i]) {
          result= result+Math.pow(2,this.latter.length-1-i)
        }}
      this.ten[1]=this.latter[0]===false?result:-result
      this.isEnd=this.ten[0]+this.mathMod+this.ten[1]+"="+this.ten[2]
    },
    result(){
      let result = 0;
      for (let i = 1; i < this.result.length; i++) {
        if (this.result[i]) {
          result = result + Math.pow(2, this.result.length - i - 1)
        }
      }
      this.ten[2]=this.result[0]===false?result:-result
      this.isEnd=this.ten[0]+this.mathMod+this.ten[1]+"="+this.ten[2]
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
          <option value='+'    >＋</option>
          <option value='-'    >-</option>
          <option value='*'    >*</option>
          <option value='/'    >/</option>
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
              <input type="checkbox" v-model="result[index]">
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

</div>
</template>

<style scoped>

</style>