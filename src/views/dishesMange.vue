<!--课设基本功能实现-->
<script>
import {Fetch, GetFetch} from "@/tool/fetch";

export default{
    data() {
      return {
        item:'',
        result:'',
        tableData: Array(20).fill(this.item),
        item2:{},
        dishes:{},
        isAdd:false,
        thing:'',//1：菜品，0：订单
        form: {
          name: '',
          region: '',
          price:'',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        orderThing:0,
        num:[],
        orderList: Array(20).fill(this.order),
        type:'0',//1展示菜品
        order:{inputValue:0},
        formLabelWidth: '120px',
        dialogTableVisible: false,
        dialogFormVisible: false,
        sum:0,
        i:{},
      }
    },
  methods:{
    exit()
    {
      localStorage.setItem('token', '');//保存jwt
    },
    async dishesAdd() {
      this.dialogFormVisible = false
      this.dishes = {name: this.form.name, price: this.form.price}
      this.result = await Fetch("/aaw/dishes/Add", this.dishes, "POST")
      await this.update();
      // Fetch{"/aaw/dishes/Add",this.dishes,"POST"}
    },
    //起售/停售
    async eIs(dishes) {
      this.result = await Fetch('/aaw/dishes/is',dishes, 'POST')
      console.log(this.result.msg)
      await this.update();
    },
    //自己菜品更新
    async update(){
      this.item = await GetFetch('/aaw/dishes/select/mine', 'GET')
      this.dishes=this.item.data
      this.tableData=this.dishes
      this.thing=2
      this.type=1
    },
    //删除菜品
    async del(dishes) {
      this.result = await Fetch('/aaw/dishes/del', dishes, 'POST')
      console.log(this.result.msg)
      await this.update();
    },
    //推荐刷新
    async referrer(){
      this.item = await GetFetch('/aaw/dishes/select/all', 'GET')
      this.dishes=this.item.data
      this.tableData=this.dishes
      this.thing=1;//推荐
      this.type=1
    },
    //下单
    // async orderAdd(num,dishes){
    //   this.order={did:dishes.did,address:this.$store.state.me.buyAddress,num}
    //   this.result=await Fetch("/aaw/order/add",this.order,"Post")
    //   await this.referrer()
    // },
    //购物车
    async shopCart(){
      this.result= await GetFetch("/aaw/order/select/buyCart","GET");
      this.orderList=this.result.data
      this.type=0;
      this.thing=0;
      this.orderThing=1
    },
    //获得全部订单
    async getAllOrder(){
      this.result= await GetFetch("/aaw/order/select/mine","GET");
      this.orderList=this.result.data
      this.type=0;
      this.thing=0;
      this.orderThing=0
    },
    // getFinish(i){
    //   console.log(i)
    //   return 5
    // },
    //下单弹窗
    async buy(dishes) {
      this.order = {did: dishes.did, address: this.$store.state.me.buyAddress,num:dishes.zero}
      this.result = await Fetch("/aaw/order/add", this.order, "Post")
      await this.referrer()
      this.$message({
        message: '下单成功了，快去付款吧',
        type: 'success'
      });
    },
    async goBuy(order) {
      this.result = await Fetch('/aaw/order/is', order, "POST")
      this.$message({
        message: '购买成功了，很快就到哟',
        type: 'success'
      });
      this.orderThing? await this.shopCart():await this.getAllOrder()
    },
    evaluate(order) {
      console.log(order)
      // this.result = await Fetch('/aaw/order/is', order, "POST")
      this.$message({
        message: '谢谢评价',
        type: 'success'
      });
      this.getAllOrder()
    },
    async end(order) {
      this.result = await Fetch('/aaw/order/is', order, "POST")
      this.$message({
        message: '账单结算成功',
        type: 'success'
      });
     await this.getAllOrder()
    },
    //删除菜品
    async del2(order) {
      this.result = await Fetch('/aaw/order/del', order, 'POST')
      this.orderThing ? await this.shopCart():await this.getAllOrder()
    },
    async buyCartAll() {
      for (const index in this.orderList) {
        this.result = await Fetch('/aaw/order/is',this.orderList[index], "POST")
      }
      this.$message({
        message: '购买成功了，很快就到哟',
        type: 'success'
      });
      this.orderThing? await this.shopCart():await this.getAllOrder()
    },
    Sum(){
      let a = 0;
      for (const order in this.orderList) {
        // alert(order)
        a = a +this.orderList[order].num*this.orderList[order].dishes.price;
      }
      this.sum=a
    }
  },
  watch:{
    orderList(){
      this.Sum()
    }
  },
  async created() {
   await this.update();
   this.type=1
    // this.i=await Fetch('/aaw/uid/selectUser',this.me,"POST")
    // console.log(this.i.data)
  }
}
</script>

<template>
  <el-container style=" border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu :default-openeds="['1', '3']">
        <el-menu-item index="1" @click="update"><i class="el-icon-message"></i>菜品管理</el-menu-item>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-menu"></i>订单管理</template>
            <el-menu-item index="2-1" @click="getAllOrder">全部订单</el-menu-item>
            <el-menu-item index="2-2">删除订单</el-menu-item>
        </el-submenu>
        <el-menu-item index="3" @click="referrer"><i class="el-icon-s-shop"></i>推荐</el-menu-item>
        <el-menu-item index="4" @click="shopCart"><i class="el-icon-goods"></i>购物车</el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-dropdown>
          <i class="el-icon-setting" ></i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>查看</el-dropdown-item>
            <el-dropdown-item ><el-button type="text" @click="dialogFormVisible = true">新增</el-button></el-dropdown-item>
            <el-dropdown-item>删除</el-dropdown-item>
          </el-dropdown-menu><span>{{this.$store.state.me.nickname}}</span>
        </el-dropdown>
      </el-header>
      <el-main>
<!--        {{this.form.name}}{{this.form.price}}-->
        <el-dialog title="添加菜品" :visible.sync="dialogFormVisible">
          <el-form :model="form">
            <el-form-item label="菜品名称" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="菜品单价" :label-width="formLabelWidth">
              <el-input v-model="form.price" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="dishesAdd">确 定</el-button>
          </div>
        </el-dialog>
        <el-table :data="this.tableData" v-if="this.type">
          <el-table-column prop="name" label="菜品名" width="100">
          </el-table-column>
          <el-table-column prop="price" label="价格" width="80">
          </el-table-column>
          <el-table-column prop="ct" label="创建时间">
          </el-table-column>
          <el-table-column prop="et" label="修改时间">
          </el-table-column>
          <el-table-column prop="num" label="销售量">
          </el-table-column>
          <el-table-column  width="300" prop="isCanBuy" v-if="this.thing===1"  label="下单"><template scope="scope">
              <el-button  plain type="primary" @click="buy(scope.row)">下单</el-button>
            <el-input-number v-model="scope.row.zero" :min="1" :max="999" size="mini"></el-input-number></template>
          </el-table-column>
          <el-table-column prop="isCanBuy" v-if="this.thing===2" label="起售/停售">
            <template scope="scope">
            <span :class="{'text-danger': !scope.row, 'text-success': scope.row}">
              <el-button type="primary" plain @click="eIs(scope.row)"> {{ !scope.row.isCanBuy ? '起售' : '停售' }}</el-button></span>
          </template>
          </el-table-column>
<!--          <el-table-column v-if="this.thing===2" label="数量">-->
<!--            <div>-->
<!--              <i class="el-icon-plus"></i><input v-model="this.num[]">-->
<!--            </div>-->
<!--          </el-table-column>-->
          <el-table-column prop="num" v-if="this.thing===2" label="删除">
            <template scope="scope">
            <span>
              <el-button type="danger" @click="del(scope.row)">删除</el-button></span>
            </template>
          </el-table-column>
        </el-table>
        <el-table :data="orderList" v-if="!type">
          <el-table-column prop="oid" label="订单号" width="80">
          </el-table-column>
          <el-table-column prop="dishes.name" label="菜品名称" width="80">
          </el-table-column>
          <el-table-column prop="dishes.price" label="单价" width="80">
          </el-table-column>
          <el-table-column prop="num" label="数量" width="80">
          </el-table-column>
          <el-table-column prop="createTime" label="下单时间">
          </el-table-column>
          <el-table-column prop="changeTime" label="修改时间">
          </el-table-column>
<!--          <el-table-column prop="finStatus?'付款'：‘评价’" label="订单状态">-->
<!--          </el-table-column>-->
          <el-table-column label="订单状态">
            <template slot-scope="scope">
              <div v-if="scope.row.finStatus === 0">
                <el-button @click="goBuy(scope.row)" type="primary">付款</el-button>
              </div>
              <div v-else-if="scope.row.finStatus === 1">
                <el-button @click="end(scope.row)" type="success">结算</el-button>
              </div>
              <div v-else-if="scope.row.finStatus >1">
                <el-button @click="evaluate(scope.row)">评价</el-button>
              </div></template></el-table-column>
          <el-table-column prop="num" label="删除">
              <template scope="scope2">
            <span>
              <el-button type="danger" @click="del2(scope2.row)">删除</el-button></span>
              </template>
          </el-table-column>
        </el-table>
        <div style="float: right;width: 200px" v-show="this.orderThing && !this.thing">
        ￥{{sum}}<el-button type="primary" @click="buyCartAll()">全部付款</el-button></div>
      </el-main>
    </el-container>
  </el-container>

</template>

<style scoped>

</style>