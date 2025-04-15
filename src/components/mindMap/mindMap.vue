<script>
import * as d3 from 'd3';
import {Fetch, GetFetch} from "@/tool/fetch";
export default {
  data(){
    return{
      // 思维导图数据
      dataTree:"",
      //评论数据
      tableData: [],
      searchData:[],//思维导图查询数据表
      select:"",//搜索框绑定数据
      MindMapShow:false,//思维导图展示
      comment:{
        mid:0,
        content:"",
      },//批注绑定数据
      title:'',
      map:"",//思维导图相关信息
      isMine:false,//是否是我的思维导图
      isEdit:false,//是否是编辑状态
      node:{title: "", content:"", x:0},
      anything:false,
      SelectTypeComment:0,
    }
  },
  methods: {
    //生成思维导图
    mindMap(DataTree,id) {this.renderMindMap(DataTree,id)},
    //渲染思维导图
    renderMindMap(dataTree,id) {
      // 清除现有的 SVG 元素
      d3.select('.test11-1').selectAll('*').remove();
      // 添加淡绿色背景色
      var svg10_1 = d3.select('.test11-1').style('width', 1500).style('height', 800).append('svg').style('background-color', 'lightgreen');
      // 建树的适配器
      var tree10_1 = d3.tree().size([800, 600]).separation(function (a, b) {
        return (a.parent === b.parent ? 1 : 2);
      });
      // 创建层次布局并处理json格式数据
      var treeData = tree10_1(d3.hierarchy(dataTree).sum(function (d) {
        return d.value;
      }));
      // 节点信息
      var nodes = treeData.descendants();
      // 边信息
      var links = treeData.links();
      // 改进节点位置。
      nodes[0].offset = nodes[0].data.title.length > 20 ? 20 : nodes[0].data.title.length;
      for (var j = 1; j < nodes.length; j++) {
        nodes[j].offset = nodes[j].data.title.length > 20 ? 20 : nodes[j].data.title.length + nodes[j].parent.offset;
      }
      // 创建一个贝塞尔生成曲线生成器
      var Bezier_curve_generator = d3.linkHorizontal()
          .x(function (d) {return d.y;}).y(function (d) {return d.x;});
      // 绘制边
      svg10_1.append("g").selectAll("path").data(links).enter().append("path").attr("d", function (d) {
        var start = {x: d.source.x, y: d.source.y + 80 + 17 * d.source.offset};
        var end = {x: d.target.x, y: d.target.y + 80 + 17 * d.source.offset};
        return Bezier_curve_generator({source: start, target: end});
      }).attr("fill", "none").attr("stroke", "yellow").attr("stroke-width", 1);
      // 标记节点圆心
      var gs = svg10_1.append("g").selectAll("g").data(nodes).enter().append("g").attr("transform", function (d, i) {
        var cx = d.x;
        var cy = d.y + 70 + 17 * (i > 0 ? d.parent.offset : 0);
        return "translate(" + cy + "," + cx + ")";
      });
      // 节点矩形
      gs.append("rect").data(nodes).style('fill',function(d){return d.data.nodeId === id ? 'lightblue':'white'})
          .attr("x", 10).attr('y', -12).attr('width', function (d) {
            return 17 * (d.data.title.length > 20 ? 20 : d.data.title.length);
          })
          .attr('height', 20).attr("fill", "white").attr("stroke", "blue").attr("stroke-width", 1).attr("rx", 4).attr("ry", 4) // 添加圆角
          .on('mousemove', function () {
            d3.select(this).transition().style("fill", "lightblue");
          })
          .on('mouseout', function () {
            d3.select(this).transition().duration(500).style("fill", "white");
          })
          .on('click', (event, d) => {
            // 使用箭头函数以确保 `this` 指向的是正确的对象
            if(this.isEdit){this.editFloatingCard(d.data, "0");}
            else{this.viewFloatingCard(d.data);}})

      // 文字
      gs.append("text")
          .attr("x", 10).attr("y", -5).attr("dy", 10)
          .text(function (d) {
            return d.data.title;
          })
          .attr('fill', 'red')
          .on('mousemove', function () {
            d3.select(this).transition().style("fill", "blue");
          })
          .on('mouseout', function () {
            d3.select(this).transition().duration(500).style("fill", "red");
          })
          .on('click', (event, d) => {
            // 使用箭头函数以确保 `this` 指向的是正确的对象
            if(this.isEdit){this.editFloatingCard(d.data, "0");}
            else{this.viewFloatingCard(d.data);}});
    },
    //创建浮动节点卡片(查看)
    viewFloatingCard(data) {
      if(!d3.select('.floating-card').empty()){
        d3.select('.floating-card').remove();
      }
      d3.select("body").append("div").attr("class", "floating-card").style("position", "fixed").style("left", "50%").style("top", "50%")
          .style("transform", "translate(-50%, -50%)").style("width", "400px").style("height", "auto") // 增加高度以容纳输入框和按钮
          .style("background-color", "white").style("border", "1px solid blue").style("box-shadow", "0 0 10px rgba(0,0,0,0.1)")
          .style("padding", "10px").style("text-align", "center").style("z-index", "1000")
          .html(`<div style="position: relative;">
               <span style="position: absolute; right: 10px; top: 10px; cursor: pointer; font-size: 16px;color: blue;">x</span><br>
               <h3>${data.title}</h3>
               <p>${data.content}</p></div>`)
          .on('click', function (event) {
            event.stopPropagation(); // 阻止事件冒泡，以屏蔽其他底层操作
          });
      // 添加关闭卡片的功能
      d3.select('.floating-card span').on('click', function () {d3.select('.floating-card').remove();})
    },
    //创建浮动节点卡片(编辑)
    editFloatingCard(data, mode) {
      if (!d3.select('.floating-card').empty()) {
        d3.select('.floating-card').remove();
      }
      d3.select("body").append("div").attr("class", "floating-card").style("position", "fixed").style("left", "50%").style("top", "50%")
          .style("transform", "translate(-50%, -50%)").style("width", "400px").style("height", "auto") // 动态调整高度
          .style("border", "1px solid blue").style("box-shadow", "0 0 10px rgba(0,0,0,0.1)").style("padding", "10px").style("text-align", "center")
          .style("z-index", "1000").style("background-color", "white")
          .html(`<div style="position: relative;">
               <span style="position: absolute; right: 10px; top: 10px; cursor: pointer; font-size: 16px; color: blue;">x</span>
               <br>
               <label for="mode">模式:</label>
               <input type="radio" id="edit-mode" name="mode" value="1">
               <label for="edit-mode">编辑</label>
               <input type="radio" id="add-mode" name="mode" value="2">
               <label for="add-mode">新添</label>
               <input type="radio" id="delete-mode" name="mode" value="3">
               <label for="delete-mode">删除</label>
               <br>
               <label for="title-input-nodeAdd">标题:</label>
               <input type="text" id="title-input-nodeAdd" placeholder="请输入节点标题" value="${mode==="2"?"":data.title}">
               <br>
               <label for="card-input-nodeAdd">详情:</label>
               <textarea id="card-input-nodeAdd" placeholder="请输入内容" rows="6" cols="30">${mode==="2"?"":data.content }</textarea>
               <br>
               <button id="confirm-button" style="color: white; background-color: blue; border: none; padding: 5px 10px; cursor: pointer;">确定</button>
            </div>`)
          .on('click', function (event) {
            event.stopPropagation(); // 阻止事件冒泡，以屏蔽其他底层操作
          });

      // 添加关闭卡片的功能
      d3.select('.floating-card span').on('click', function () {
        d3.select('.floating-card').remove();
      });

      // 添加确定按钮的功能
      d3.select('#confirm-button').on('click', async () => {
        this.node={title: "", content:"", x:0};
        const selectedMode = d3.select('input[name="mode"]:checked').node().value;
        this.node.title = d3.select('#title-input-nodeAdd').node().value;
        this.node.content = d3.select('#card-input-nodeAdd').node().value;
        this.node.x = data.nodeId;
        switch (selectedMode) {
          case '1':
            this.node.nodeId = data.nodeId; // 只在编辑节点时设置 nodeId
            // 触发编辑事件
            await Fetch('/aaw/node', this.node, 'PUT');
            console.log('编辑节点:' + this.node);
            break;
          case '2':
            await Fetch('/aaw/node', this.node, 'POST');
            // 触发新添事件
            console.log('新添节点:' + this.node);
            break;
          case '3':
            await Fetch('/aaw/node/'+this.node.x, this.node, 'DELETE');
            // 触发删除事件
            console.log('删除节点:' + this.node);
            break;
          case '0':
            alert('未选择模式');
            break
          default:
            alert('未选择模式');
        }
        this.open1("修改成功");
        await this.getDataTree(this.dataTree.mapId);//更新数据树dataTree
        this.renderMindMap(this.dataTree,0);
        d3.select('.floating-card').remove(); // 确认后关闭卡片
      });
    },
    //创建新的思维导图数据
    creatNewMindMap() {
      // 创建新的思维导图
      d3.select("body").append("div").attr("class", "floating-card").style("position", "fixed").style("left", "50%").style("top", "50%")
          .style("transform", "translate(-50%, -50%)").style("width", "400px").style("height", "300px") // 增加高度以容纳更多输入框和按钮
          .style("background-color", "white").style("border", "1px solid blue").style("box-shadow", "0 0 10px rgba(0,0,0,0.1)")
          .style("padding", "10px").style("text-align", "center").style("z-index", "1000")
          .html(`<div style="position: relative;">
              <span style="position: absolute; right: 10px; top: 10px; cursor: pointer; font-size: 16px; color: blue;" class="close-card">x</span>
              <br>
              <h3>创建思维导图</h3>
              <form>
                <label for="mindmap-name">思维导图名称:</label>
                <input type="text" id="mindmap-name" placeholder="请输入思维导图名称"><br>
                <label for="mindmap-card">简介:</label>
                <textarea id="mindmap-card" placeholder="请输入简介" rows="6" cols="30"></textarea><br>
                <label for="mindmap-public">是否公开:</label>
                <input type="checkbox" id="mindmap-public">
                <button type="button" class="submit-form">提交</button>
              </form>
            </div>`)
          .on('click', function (event) {
            event.stopPropagation(); // 阻止事件冒泡，以屏蔽其他底层操作
          });

      // 添加关闭卡片的功能
      d3.select('.floating-card .close-card').on('click', function () {
        d3.select('.floating-card').remove();
      });
      d3.select('.floating-card .submit-form').on('click', async () => {
        console.log('提交按钮被点击');
        // 获取表单数据
        const mindMap = {
          "title": d3.select("#mindmap-name").node().value,
          "content": d3.select("#mindmap-card").node().value,
          "isPublic": d3.select('#mindmap-public').property('checked'), // 手动获取输入框的值
        };
        console.log(mindMap);
        // 发送请求
        this.Map = await Fetch("/aaw/mindMap", mindMap, "POST");
        this.Map = this.Map.data;
        console.log(this.Map);
        // 关闭卡片
        d3.select('.floating-card').remove();
        this.open1("创建成功,如需修改，请前往‘我的’页面");
        //提交到后端请求
        console.log(this.Map.mapId);
      });
    },
    //成功提示
    open1(msg) {
      this.$notify({
        title: '成功',
        message: msg,
        type: 'success',
        duration:2000
      });
    },
    //查询思维导图列表展示
    async selectMindMap(index) {
      this.anything=false;
      let url='/aaw/mindMap';
      switch (index) {
        case 1://推荐
            this.isMine=false;
          url= url+'/Rec';
          break;
        case 2://热门
            this.isMine=false;
          url = url+'/Hot';
          break;
        case 3://标记
            this.isMine=false;
          url= url+'/marks';
          break;
        case 4://我的
            this.isMine=true;
          url = url+'/mine';
          break;
        case 5://收藏
            this.isMine=false;
          url = url+'/stars';
          break;
      }
      this.searchData = await GetFetch(url);
      this.searchData = this.searchData.data;
      this.open1("搜索成功");
    },
    //根据思维导图id获取思维导图数据
    async getDataTree(mid) {
      this.dataTree = await GetFetch('/aaw/nodeTree/Mid/'+mid);
      this.dataTree = this.dataTree.data;
      this.open1("思维导图获取成功");
    },
    //根据思维导图id获取思维导图评论数据
    async getComment(mid) {
      this.tableData=await GetFetch('/aaw/comment/'+mid);
      this.tableData=this.tableData.data;
      console.log(this.tableData);
      this.SelectTypeComment=0
    },

    async SelectDetail(row) {
      this.isEdit = false;
      this.map = row;
      await this.getDataTree(row.mapId);
      this.MindMapShow = true;
      if(row.type==="节点"){this.mindMap(this.dataTree,row.id);}
      else{this.mindMap(this.dataTree,0);}
      await this.getComment(this.map.mapId);
      if(row.type==="批注"){this.SelectTypeComment=row.id;}
      this.open1("详情成功：" + row.title);
    },

    //查看思维导图树状结构详情
    async handleDetail(row) {
      //加载思维导图
      this.isEdit = false;
      this.map = row;
      await this.getDataTree(row.mapId);
      this.MindMapShow = true;
      this.mindMap(this.dataTree,0);
      //加载评论
      await this.getComment(this.map.mapId);
      this.open1("详情成功：" + row.title);
    },
    //收藏思维导图
    async handleCollect(row) {
      const res = await GetFetch('/aaw/mindMap/love+-/' + row.mapId );
      // 实现收藏逻辑，row是当前行的数据
      this.open1(res.data+'' + row.title);
    },
    //编辑思维导图
    async editMindMap(row) {
      //加载思维导图
      this.isEdit = true;
      this.map = row;
      await this.getDataTree(row.mapId);
      this.MindMapShow = true;
      this.mindMap(this.dataTree);
      //加载评论
      await this.getComment(this.map.mapId);
      this.open1("编辑界面打开成功：" + row.title);
    },
    //标记思维导图
    async Collect(row) {
      const res = await GetFetch('/aaw/mindMap/mark+-/' + row.mapId );
      await this.handleDetail(row);
      // 实现标记逻辑，row是当前行的数据
      this.open1(res.data+'' + row.title);
    },
    //删除思维导图
    async deleteMindMap(row) {
      await Fetch('/aaw/mindMap/' + row.mapId, "", 'DELETE')
      // 实现删除逻辑，row是当前行的数据
      this.open1("删除成功：" + row.title);
      await this.selectMindMap(4)
    },
    //上传批注
    async handleConfirm() {
      this.comment.mid = this.map.mapId;
      console.log(this.comment);
      this.tableData = await Fetch('/aaw/comment', this.comment, 'POST');
      this.tableData = this.tableData.data;
      this.comment.content = "";
    },
    //取消批注
    handleCancel() {
      this.$message('取消');
    },
    //手动查询
    async selectAnything(){
      this.anything=true;
      this.searchData=await GetFetch("/aaw/anything/"+this.select)
      this.searchData=this.searchData.data;
      console.log(this.searchData);
    }
  },
  created() {
    this.selectMindMap(2);
  }
}
</script>

<template>
  <div>
    <el-container>
      <el-header style="height: 100px"><h1>思维导图</h1></el-header>
      <el-container>
          <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
            <el-row class="tac">
<!--              左导航-->
                <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
                  <el-menu-item index="1">
                    <i class="el-icon-menu"></i>
                    <span slot="title" @click="MindMapShow=false; selectMindMap(1)">推荐</span>
                  </el-menu-item>
                  <el-menu-item index="2">
                    <i class="el-icon-s-data"></i>
                    <span slot="title" @click="MindMapShow=false; selectMindMap(2)">热门</span>
                  </el-menu-item>
                  <el-menu-item index="3">
                    <i class="el-icon-collection-tag"></i>
                    <span slot="title" @click="MindMapShow=false; selectMindMap(3)">标记</span>
                  </el-menu-item>
                  <el-menu-item index="4">
                    <i class="el-icon-s-home"></i>
                    <span slot="title" @click="MindMapShow=false;selectMindMap(4)">我的</span>
                  </el-menu-item>
                  <el-menu-item index="5">
                    <i class="el-icon-star-off"></i>
                    <span slot="title" @click="MindMapShow=false; selectMindMap(5)">收藏</span>
                  </el-menu-item>
                  <el-menu-item index="6">
                    <i class="el-icon-folder-add"></i>
                    <span slot="title" @click="creatNewMindMap()">上传</span>
                  </el-menu-item>
                </el-menu>
            </el-row>
          </el-aside>
<!--       右展示-->
        <el-main>
<!--          搜索栏-->
          <div>
          <el-input v-model="select" style="width: 80%" placeholder="请输入内容"></el-input>
          <el-button @click="MindMapShow=false; selectAnything()" type="primary" icon="el-icon-search">搜索</el-button><br></div>

<!--          思维导图搜索列表展示-->
            <div v-show="!MindMapShow">
              <el-table v-if="!anything" :data="this.searchData" stripe show-header="false">
                <el-table-column label="标题" prop="title" width="450">
                  <template #default="{ row }">
                    <div @click="handleDetail(row)" style="cursor: pointer;">{{ row.title }}</div>
                  </template>
                </el-table-column>
                <el-table-column label="内容" prop="content">
                  <template #default="{ row }">
                    <div @click="handleDetail(row)" style="cursor: pointer;">{{ row.content }}</div>
                  </template>
                </el-table-column>
                <el-table-column label="作者" prop="nickName" width="150">
                  <template #default="{ row }">
                    <div @click="handleDetail(row)" style="cursor: pointer;">{{ row.nickName }}</div>
                  </template>
                </el-table-column>
                <el-table-column v-show="!anything" label="收藏" prop="stars" width="100" sortable>
                  <template #default="{ row }">
                    <div @click="handleDetail(row)" style="cursor: pointer;">{{ row.stars}}</div>
                  </template>
                </el-table-column>
                <el-table-column label="日期" style="display: none" prop="time" width="180" sortable>
                  <template #default="{ row }">
                    <div @click="handleDetail(row)" style="cursor: pointer;">{{ row.time }}</div>
                  </template>
                </el-table-column>
                <el-table-column v-show="!this.anything" label="操作" width="200">
                  <template #default="{ row }">
                    <el-button v-if="row.star" icon="el-icon-star-on" @click="handleCollect(row)" circle></el-button>
                    <el-button v-if="!row.star" icon="el-icon-star-off" @click="handleCollect(row)" circle></el-button>
                    <el-button icon="el-icon-edit" v-show="isMine" @click="editMindMap(row)" circle></el-button>
                    <el-button icon="el-icon-delete" v-show="isMine" @click="deleteMindMap(row)" circle></el-button>
                  </template>
                </el-table-column>
              </el-table>
              <el-table v-if="anything" :data="this.searchData" stripe show-header="false">
                <el-table-column label="类型" prop="stars" width="100" >
                  <template #default="{ row }">
                    <div @click="SelectDetail(row)" style="cursor: pointer;">{{ row.type}}</div>
                  </template>
                </el-table-column>
                <el-table-column label="标题" prop="title" width="450">
                  <template #default="{ row }">
                    <div @click="SelectDetail(row)" style="cursor: pointer;">{{ row.title }}</div>
                  </template>
                </el-table-column>
                <el-table-column label="内容" prop="content">
                  <template #default="{ row }">
                    <div @click="SelectDetail(row)" style="cursor: pointer;">{{ row.content }}</div>
                  </template>
                </el-table-column>
                <el-table-column label="作者" prop="nickName" width="150">
                  <template #default="{ row }">
                    <div @click="SelectDetail(row)" style="cursor: pointer;">{{ row.nickName }}</div>
                  </template>
                </el-table-column>
                <el-table-column label="日期" style="display: none" prop="time" width="180" sortable>
                  <template #default="{ row }">
                    <div @click="SelectDetail(row)" style="cursor: pointer;">{{ row.time }}</div>
                  </template>
                </el-table-column>
              </el-table>
            </div>

<!--          思维导图相关展示-->
          <div v-show="MindMapShow">
            <h2 style="text-align: center">{{title}}</h2>
            <svg class="test11-1" >
              <rect></rect>
            </svg><br>
              <el-input v-model="comment.content" style="width: 90%;" placeholder="千山万水总是情，留下批注行不行"></el-input>
            <template>
            <el-popconfirm  @confirm="handleConfirm" @cancel="handleCancel" title="确定发布？"><el-button  slot="reference">发表</el-button></el-popconfirm>
            </template>
            <el-button v-if="!map.star" icon=" el-icon-star-off" @click="handleCollect(map)"  circle></el-button>
            <el-button v-if="map.star" icon="el-icon-star-on" @click="handleCollect(map)"  circle></el-button>
            <el-button v-if="map.mark" icon="el-icon-s-flag" @click="Collect(map)" circle></el-button>
            <el-button v-if="!map.mark" icon="el-icon-collection-tag" @click="Collect(map)" circle></el-button>
          <br><br>
          <el-table :data="tableData" stripe show-header="false">
            <el-table-column label="用户" prop="nickName" width="180">
<!--              <template #default="{ row }">-->
<!--                <div v-if="row.cid===this.SelectTypeComment" style="background-color:lightblue">{{ row.nickName }}</div>-->
<!--              </template>-->
            </el-table-column >
            <el-table-column label="批注" prop="content">
<!--              <template  #default="{ row }">-->
<!--                <div v-if="row.cid===this.SelectTypeComment" style="background-color:lightblue">{{ row.content }}</div>-->
<!--              </template>-->
            </el-table-column>
            <el-table-column label="日期" style="display: none" prop="time" width="180" sortable>
<!--              <template #default="{ row }">-->
<!--                <div v-if="row.cid===this.SelectTypeComment" style="background-color:lightblue">{{ row.time }}</div>-->
<!--              </template>-->
            </el-table-column>
          </el-table>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.axis path,
.axis line{
  fill: none;
  stroke: black;
  shape-rendering: crispEdges;
}
.axis text {
  font-family: sans-serif;
  font-size: 11px;
}
.test11-1 {
  background-color: #e0ffe0; /* 淡绿色 */
}
</style>
