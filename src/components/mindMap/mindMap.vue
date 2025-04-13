<script>
import * as d3 from 'd3';
import {Fetch, GetFetch} from "@/tool/fetch";
export default {
  data(){
    return{
      // 思维导图数据
      dataTree:{
          "nodeId": 44,
          "mapId": 47,
          "title": "初始根节点",
          "card": null,
          "creatTime": [
            2025,
            4,
            12,
            23,
            20,
            29
          ],
          "wordSize": 0,
          "underLine": 0,
          "delLine": 0,
          "wordStyle": null,
          "wordColor": null,
          "leftValue": 48,
          "rightValue": 0,
          "preId": 44,
          "nextId": 44,
          "x": 0,
          "children": [
            {
              "nodeId": 48,
              "mapId": 47,
              "title": "子节点1",
              "card": null,
              "creatTime": [
                2025,
                4,
                12,
                23,
                52,
                8
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 0,
              "rightValue": 50,
              "preId": 48,
              "nextId": 48,
              "x": 0,
              "children": [],
              "l": null,
              "r": null
            },
            {
              "nodeId": 50,
              "mapId": 47,
              "title": "子节点1",
              "card": null,
              "creatTime": [
                2025,
                4,
                12,
                23,
                55,
                9
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 0,
              "rightValue": 51,
              "preId": 50,
              "nextId": 50,
              "x": 0,
              "children": [],
              "l": null,
              "r": null
            },
            {
              "nodeId": 51,
              "mapId": 47,
              "title": "子节点3",
              "card": null,
              "creatTime": [
                2025,
                4,
                12,
                23,
                58,
                45
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 57,
              "rightValue": 52,
              "preId": 51,
              "nextId": 51,
              "x": 0,
              "children": [
                {
                  "nodeId": 57,
                  "mapId": 47,
                  "title": "子节点7",
                  "card": null,
                  "creatTime": [
                    2025,
                    4,
                    13,
                    0,
                    17,
                    13
                  ],
                  "wordSize": 0,
                  "underLine": 0,
                  "delLine": 0,
                  "wordStyle": null,
                  "wordColor": null,
                  "leftValue": 60,
                  "rightValue": 58,
                  "preId": 57,
                  "nextId": 57,
                  "x": 0,
                  "children": [
                    {
                      "nodeId": 60,
                      "mapId": 47,
                      "title": "子节点10",
                      "card": null,
                      "creatTime": [
                        2025,
                        4,
                        13,
                        0,
                        18,
                        19
                      ],
                      "wordSize": 0,
                      "underLine": 0,
                      "delLine": 0,
                      "wordStyle": null,
                      "wordColor": null,
                      "leftValue": 0,
                      "rightValue": 0,
                      "preId": 60,
                      "nextId": 60,
                      "x": 0,
                      "children": [],
                      "l": null,
                      "r": null
                    }
                  ],
                  "l": null,
                  "r": null
                },
                {
                  "nodeId": 58,
                  "mapId": 47,
                  "title": "子节点8",
                  "card": null,
                  "creatTime": [
                    2025,
                    4,
                    13,
                    0,
                    17,
                    34
                  ],
                  "wordSize": 0,
                  "underLine": 0,
                  "delLine": 0,
                  "wordStyle": null,
                  "wordColor": null,
                  "leftValue": 0,
                  "rightValue": 0,
                  "preId": 58,
                  "nextId": 58,
                  "x": 0,
                  "children": [],
                  "l": null,
                  "r": null
                }
              ],
              "l": null,
              "r": null
            },
            {
              "nodeId": 52,
              "mapId": 47,
              "title": "子节点4",
              "card": null,
              "creatTime": [
                2025,
                4,
                13,
                0,
                4,
                44
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 0,
              "rightValue": 53,
              "preId": 52,
              "nextId": 52,
              "x": 0,
              "children": [],
              "l": null,
              "r": null
            },
            {
              "nodeId": 53,
              "mapId": 47,
              "title": "子节点5",
              "card": null,
              "creatTime": [
                2025,
                4,
                13,
                0,
                12,
                4
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 0,
              "rightValue": 54,
              "preId": 53,
              "nextId": 53,
              "x": 0,
              "children": [],
              "l": null,
              "r": null
            },
            {
              "nodeId": 54,
              "mapId": 47,
              "title": "子节点6",
              "card": null,
              "creatTime": [
                2025,
                4,
                13,
                0,
                12,
                44
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 59,
              "rightValue": 55,
              "preId": 54,
              "nextId": 54,
              "x": 0,
              "children": [
                {
                  "nodeId": 59,
                  "mapId": 47,
                  "title": "子节点9",
                  "card": null,
                  "creatTime": [
                    2025,
                    4,
                    13,
                    0,
                    17,
                    54
                  ],
                  "wordSize": 0,
                  "underLine": 0,
                  "delLine": 0,
                  "wordStyle": null,
                  "wordColor": null,
                  "leftValue": 0,
                  "rightValue": 0,
                  "preId": 59,
                  "nextId": 59,
                  "x": 0,
                  "children": [],
                  "l": null,
                  "r": null
                }
              ],
              "l": null,
              "r": null
            },
            {
              "nodeId": 55,
              "mapId": 47,
              "title": "子节点7",
              "card": null,
              "creatTime": [
                2025,
                4,
                13,
                0,
                14,
                7
              ],
              "wordSize": 0,
              "underLine": 0,
              "delLine": 0,
              "wordStyle": null,
              "wordColor": null,
              "leftValue": 0,
              "rightValue": 0,
              "preId": 55,
              "nextId": 55,
              "x": 0,
              "children": [],
              "l": null,
              "r": null
            }
          ],
          "l": null,
          "r": null
        },
      //评论数据
      tableData: [{
        date: '2016-05-03',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      },  {
        date: '2016-05-07',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }],
      searchData:[],//思维导图查询数据表
      select:"",//搜索框绑定数据
      MindMapShow:false,//思维导图展示
      comment:"",//批注绑定数据
      nameTrue:false,//思维导图名称是否已定
      CreatTree:{"name":"创建根节点","children":[]},//创建思维导图数据
      map:"",//思维导图相关信息
      //mindMap数据
      // mindMapTitle: "请输入思维导图名称", // 思维导图名称
      // mindMapDescription: "请输入思维导图描述", // 思维导图描述
      //node数据
      node:{title: "", card:"", x:0,mapId:0}
    }
  },
  methods: {
    //生成思维导图
    mindMap(DataTree) {this.renderMindMap(DataTree)},
    //渲染思维导图
    renderMindMap(dataTree) {
      // 清除现有的 SVG 元素
      d3.select('.test11-1').selectAll('*').remove();
      var svg10_1 = d3.select('.test11-1').style('width', 1000).style('height', 600).append('svg');
      // 建树的适配器
      var tree10_1 = d3.tree().size([600, 400]).separation(function (a, b) {
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
          .x(function (d) {
            return d.y;
          })
          .y(function (d) {
            return d.x;
          });
      // 绘制边
      svg10_1.append("g").selectAll("path").data(links).enter().append("path").attr("d", function (d) {
        var start = {x: d.source.x, y: d.source.y + 80 + 17 * d.source.offset};
        var end = {x: d.target.x, y: d.target.y + 80 + 17 * d.source.offset};
        return Bezier_curve_generator({source: start, target: end});
      })
          .attr("fill", "none").attr("stroke", "yellow").attr("stroke-width", 1);
      // 标记节点圆心
      var gs = svg10_1.append("g").selectAll("g").data(nodes).enter().append("g").attr("transform", function (d, i) {
        var cx = d.x;
        var cy = d.y + 70 + 17 * (i > 0 ? d.parent.offset : 0);
        return "translate(" + cy + "," + cx + ")";
      });
      gs.append("rect").data(nodes)
          .attr("x", 10)
          .attr('y', -12)
          .attr('width', function (d) {
            return 17 * (d.data.title.length > 20 ? 20 : d.data.title.length);
          })
          .attr('height', 20)
          .attr("fill", "white")
          .attr("stroke", "blue")
          .attr("stroke-width", 1)
          .attr("rx", 4) // 添加圆角
          .attr("ry", 4) // 添加圆角
          .on('mousemove', function () {
            d3.select(this).transition().style("fill", "lightblue");
          })
          .on('mouseout', function () {
            d3.select(this).transition().duration(500).style("fill", "white");
          })
          .on('click', (event, d) => {
            // 使用箭头函数以确保 `this` 指向的是正确的对象
            this.createFloatingCard(d.data);
          });

      // 文字
      gs.append("text")
          .attr("x", 10) // 如果某节点有子节点，则对应的文字前移
          .attr("y", -5)
          .attr("dy", 10)
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
            this.createFloatingCard(d.data);
          });
    },

    //创建浮动卡片
    createFloatingCard(data) {
      d3.select("body")
          .append("div")
          .attr("class", "floating-card")
          .style("position", "fixed")
          .style("left", "50%")
          .style("top", "50%")
          .style("transform", "translate(-50%, -50%)")
          .style("width", "400px")
          .style("height", "250px") // 增加高度以容纳输入框和按钮
          .style("background-color", "white")
          .style("border", "1px solid blue")
          .style("box-shadow", "0 0 10px rgba(0,0,0,0.1)")
          .style("padding", "10px")
          .style("text-align", "center")
          .style("z-index", "1000")
          .html(`<div style="position: relative;" v-show="this.MindMap">
                    <span style="position: absolute; right: 10px; top: 10px; cursor: pointer; font-size: 16px;color: blue;">x</span>
                    <br>
                    <h3>${data.title}</h3>
                    <label for="mindmap-description">标题:</label><input type="text" id="title-input" v-model="node.title" placeholder="请输入节点标题"><br>
                    <label for="mindmap-description">详情:</label>
                    <textarea id="card-input" v-model="node.card" placeholder="请输入内容" rows="4" cols="30"></textarea>
                    <br>
                    <el-link style="color: blue; cursor: pointer;"  class="add-node" type="primary"> 添加节点</el-link>
                    <el-link style="color: blue; cursor: pointer;"  class="delete-node" type="danger"> 删除节点</el-link>
                 </div>`)
          .on('click', function (event) {
            event.stopPropagation(); // 阻止事件冒泡，以屏蔽其他底层操作
          });

      // 添加关闭卡片的功能
      d3.select('.floating-card span').on('click', function () {
        d3.select('.floating-card').remove();
      });

      // 添加按钮点击事件
      d3.select('.floating-card .add-node').on('click', async () => {
        this.node.title=d3.select("#title-input").node().value;
        this.node.card=d3.select("#card-input").node().value;
        this.node.mapId=this.dataTree.mapId;
        this.node.x=data.nodeId;//获取当前节点的id
        console.log(this.node);

        // 发送请求
        this.node = await Fetch("/aaw/nodeAdd", this.node, "POST");
        this.node= this.node.data;
        // 关闭卡片
        d3.select('.floating-card').remove();
        this.open1("创建成功");
        await this.getDataTree(this.dataTree.mapId);//更新数据树dataTree
        this.renderMindMap(this.dataTree);
      });

      d3.select('.floating-card .delete-node').on('click', function () {
        console.log('删除节点按钮被点击');
        // 在这里添加删除节点的逻辑
      });

    },
    //创建新的思维导图数据
    creatNewMindMap() {
      // 创建新的思维导图
      d3.select("body")
          .append("div")
          .attr("class", "floating-card")
          .style("position", "fixed")
          .style("left", "50%")
          .style("top", "50%")
          .style("transform", "translate(-50%, -50%)")
          .style("width", "400px")
          .style("height", "300px") // 增加高度以容纳更多输入框和按钮
          .style("background-color", "white")
          .style("border", "1px solid blue")
          .style("box-shadow", "0 0 10px rgba(0,0,0,0.1)")
          .style("padding", "10px")
          .style("text-align", "center")
          .style("z-index", "1000")
          .html(`<div style="position: relative;">
              <span style="position: absolute; right: 10px; top: 10px; cursor: pointer; font-size: 16px; color: blue;" class="close-card">x</span>
              <br>
              <h3>创建思维导图</h3>
              <form>
                <label for="mindmap-name">思维导图名称:</label><br>
                <input type="text" id="mindmap-name" placeholder="请输入思维导图名称"><br>

                <label for="mindmap-description">简介:</label><br>
                <textarea id="mindmap-description" placeholder="请输入简介" rows="4" cols="50"></textarea><br>

                <label for="mindmap-public">是否公开:</label><br>
                <input type="checkbox" id="mindmap-public"><br>

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
          "description": d3.select("#mindmap-description").node().value,
          "isPublic": d3.select('#mindmap-public').property('checked'), // 手动获取输入框的值
        };
        console.log(mindMap);
        // 发送请求
        this.Map = await Fetch("/aaw/mindMapAdd", mindMap, "POST");
        this.Map = this.Map.data;
        console.log(this.Map);
        // 关闭卡片
        d3.select('.floating-card').remove();
        this.open1("创建成功");
        //提交到后端请求
        this.nameTrue = true;
        console.log(this.Map.mapId);
        await this.getDataTree(this.Map.mapId);
      });
    },
    //成功提示
    open1(msg) {
      this.$notify({
        title: '成功',
        message: msg,
        type: 'success'
      });
    },
    //查询思维导图列表展示
    async selectMindMap(index) {
      let url='/aaw/mindMap';
      switch (index) {
        case 1://推荐
          url= url+'/selectByMid';
          break;
        case 2://热门
          url = url+'?isHot=1';
          break;
        case 3://标记
          url= url+'?isMark=1';
          break;
        case 4://我的
          url = url+'/selectByUser';
          break;
        case 5://收藏
          url = url+'?isCollect=1';
          break;
      }
      this.searchData = await GetFetch(url);
      this.searchData = this.searchData.data;
      this.open1("搜索成功");
    },
    //根据思维导图id获取思维导图数据
    async getDataTree(mid) {
      this.dataTree = await GetFetch('/aaw/node/getByMid/'+mid);
      this.dataTree = this.dataTree.data;
      this.open1("思维导图获取成功");
    },
    //查看思维导图详情
    async handleDetail(row) {
      await this.getDataTree(row.mapId);
      this.MindMapShow = true;
      this.nameTrue = true;
      this.mindMap(this.dataTree);
      // 实现详情逻辑，row是当前行的数据
    },
    //收藏思维导图
    handleCollect(row) {
      // 实现收藏逻辑，row是当前行的数据
      this.open1("收藏成功"+row.title);
    },
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
                    <span slot="title" @click="MindMapShow=false; selectMindMap(1)" >推荐</span>
                  </el-menu-item>
                  <el-menu-item index="2">
                    <i class="el-icon-s-data"></i>
                    <span slot="title" @click="MindMapShow=false">热门</span>
                  </el-menu-item>
                  <el-menu-item index="3">
                    <i class="el-icon-collection-tag"></i>
                    <span slot="title" @click="MindMapShow=false">标记</span>
                  </el-menu-item>
                  <el-menu-item index="4">
                    <i class="el-icon-s-home"></i>
                    <span slot="title" @click="MindMapShow=false;selectMindMap(4)">我的</span>
                  </el-menu-item>
                  <el-menu-item index="5">
                    <i class="el-icon-star-off"></i>
                    <span slot="title" @click="MindMapShow=false">收藏</span>
                  </el-menu-item>
                  <el-menu-item index="6">
                    <i class="el-icon-folder-add"></i>
                    <span slot="title" @click="MindMapShow=true;nameTrue=false;mindMap(CreatTree)">上传</span>
                  </el-menu-item>
                </el-menu>
            </el-row>
          </el-aside>
<!--       右展示-->
        <el-main>
<!--          搜索栏-->
          <div>
          <el-input  v-model="select" style="width: 80%" placeholder="请输入内容"></el-input>
          <el-button type="primary" icon="el-icon-search">搜索</el-button><br></div>
<!--          思维导图搜索列表展示-->
            <div v-show="!MindMapShow">
            <el-table :data="searchData" stripe show-header="false">
              <el-table-column label="标题" prop="title" width="450"></el-table-column >
              <el-table-column label="简介" prop="description"></el-table-column>
              <el-table-column label="作者" prop="uid" width="150"></el-table-column>
<!--              <el-table-column label="浏览量" prop="mapId" width="100" sortable></el-table-column>-->
              <el-table-column label="收藏" prop="stars" width="100" sortable></el-table-column>
              <el-table-column label="日期" style="display: none" prop="createTime" width="180" sortable></el-table-column>
              <el-table-column label="操作" width="200">
                <template #default="{ row }">
                  <el-button type="text" @click="handleDetail(row)">详情</el-button>
                  <el-button type="text" @click="handleCollect(row)">收藏</el-button>
                  <el-button type="text" @click="editMindMap(row)">编辑</el-button>
                  <el-button type="text" @click="deleteMindMap(row)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
<!--          思维导图相关展示-->
          <div v-show="MindMapShow">
            <!--       新建思维导图-->
            <h3 v-show="nameTrue">{{ map.title}}</h3>
            <el-button v-show="!nameTrue" type="primary" @click="creatNewMindMap()">新建思维导图</el-button><br>

            <svg v-show="nameTrue" class="test11-1" >
              <rect></rect>
            </svg><br>
              <el-input v-model="comment" style="width: 80%;" placeholder="千山万水总是情，留下批注行不行"></el-input>
              <el-button type="primary" plain>发表</el-button>
              <el-button type="primary" icon="el-icon-edit" circle></el-button>
              <el-button icon="el-icon-star-off" circle></el-button>
              <el-button icon="el-icon-collection-tag" circle></el-button>
          <br><br>
          <el-table :data="this.tableData" stripe show-header="false">
            <el-table-column label="用户" prop="name" width="180"></el-table-column >
            <el-table-column label="批注" prop="text"></el-table-column>
            <el-table-column label="日期" style="display: none" prop="date" width="180" sortable></el-table-column>
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
.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 20px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>
