
<script>

import * as d3 from 'd3';
export default {
  data(){
    return{
      dataset:[120,150,170,320,250],
      dataset5_1:[12,15,17,32,25],
      dataset6_1:[1200,1500,1700,3200,2500],
      dataset7_1:[10,20,30,40,33,24,12,5],
      index:[1,2,3,4,5],
      input:'',
      visible1:true,
      dataTree:{
        "name":"中华人民共和国",
        "children":
            [
              {
                "name":"浙江" ,
                "children":
                    [
                      {"name":"杭州" },
                      {"name":"宁波" },
                      {"name":"温州" },
                      {"name":"绍兴" }
                    ]
              },
              {
                "name":"广西维吾尔自治区" ,
                "children":
                    [
                      {
                        "name":"桂林市人民政府",
                        "children":
                            [
                              {"name":"秀峰区"},
                              {"name":"叠彩区"},
                              {"name":"象山区"},
                              {"name":"七星区"}
                            ]
                      },
                      {"name":"南宁"},
                      {"name":"柳州"},
                      {"name":"防城港"}
                    ]
              },
              {
                "name":"黑龙江省",
                "children":
                    [
                      {"name":"哈尔滨"},
                      {"name":"齐齐哈尔"},
                      {"name":"牡丹江"},
                      {"name":"大庆"}
                    ]
              },
              {
                "name":"新疆" ,
                "children":
                    [
                      {"name":"乌鲁木齐"},
                      {"name":"克拉玛依"},
                      {"name":"吐鲁番"},
                      {"name":"哈密"}
                    ]
              }
            ]
      },
      study:false,
      upload:{"name":"添加根目录"},
      node:'',
      tableData: [{
        date: '2016-05-03',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-02',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-08',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-06',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-07',
        name: '王小虎',
        text: '上海市普陀区金沙江路 1518 弄'
      }
      ]
    }
  },
  methods:{
    click(c){
      if (c===0){
        this.study=!this.study
      }
    },

    //   实验十
    //   添加画板
    mindMap(){
      var svg10_1=d3.select('.test11-1').style('width',1000).style('height',400).append('svg')
      //建树的设配器
      var tree10_1 = d3.tree().size([400, 400]).separation(function(a, b) { return (a.parent === b.parent ? 1:2); });
      //创建层次布局并处理json格式数据
      var treeData=tree10_1(d3.hierarchy(this.dataTree).sum(function(d){return d.value}));
      //节点信息
      var nodes=treeData.descendants();
      //边信息
      var links=treeData.links();
      //改进节点位置。
      nodes[0].offset = nodes[0].data.name.length>20?20:nodes[0].data.name.length;
      for(var j=1;j<nodes.length;j++){
        nodes[j].offset=nodes[j].data.name.length>20?20:nodes[j].data.name.length+nodes[j].parent.offset
      }
      //创建一个贝塞尔生成曲线生成器
      var Bezier_curve_generator = d3.linkHorizontal()
          .x(function(d) { return d.y; })
          .y(function(d) { return d.x; });
      //绘制边
      svg10_1.append("g").selectAll("path").data(links).enter().append("path").attr("d",function(d){
            var start = {x:d.source.x,y:d.source.y+80+17*d.source.offset};
            var end = {x:d.target.x,y:d.target.y+80+17*d.source.offset};
            return Bezier_curve_generator({source:start,target:end});
          })
          .attr("fill","none").attr("stroke","yellow").attr("stroke-width",1);
      //标记节点圆心
      var gs = svg10_1.append("g").selectAll("g").data(nodes).enter().append("g").attr("transform",function(d,i){
            var cx = d.x;
            var cy=  d.y+70+17*(i>0?d.parent.offset:0)
            return "translate("+cy+","+cx+")";
          });
      gs.append("rect").data(nodes).attr("x",10).attr('y',-12).attr('width',function (d){return 17*(d.data.name.length>20?20:d.data.name.length)}).attr('height',20).attr("fill","white").attr("stroke","blue").attr("stroke-width",1)
          .on('mousemove',function (){
            d3.select(this).transition().style("fill","red");
          }).on('mouseout',function (){
            d3.select(this).transition().duration(500).style("fill","white");
          }   )
      //文字
      gs.append("text").attr("x",10)//如果某节点有子节点，则对应的文字前移
          .attr("y",-5).attr("dy",10).text(function(d){return d.data.name;}).attr ('fill','red') .on('mousemove',function (){
        d3.select(this).transition().style("fill","blue");
      }).on('mouseout',function (){
        d3.select(this).transition().duration(500).style("fill","red");
      }   )
    },
    upload1(){
      var svgUpload=d3.select('.upload').style('width',1000).style('height',400).append('svg')
      var tree10_1 = d3.tree().size([400, 400]).separation(function(a, b) { return (a.parent === b.parent ? 1:2); });
      var dataUpload=tree10_1(d3.hierarchy(this.upload).sum(function(d){return d.value}));
      var nodes=dataUpload.descendants();
      var links=dataUpload.links();
      nodes[0].offset = nodes[0].data.name.length>20?20:nodes[0].data.name.length;
      for(var j=1;j<nodes.length;j++){
        nodes[j].offset=nodes[j].data.name.length>20?20:nodes[j].data.name.length+nodes[j].parent.offset
      }
      //创建一个贝塞尔生成曲线生成器
      var Bezier_curve_generator = d3.linkHorizontal()
          .x(function(d) { return d.y; })
          .y(function(d) { return d.x; });
      //绘制边
      svgUpload.append("g").selectAll("path").data(links).enter().append("path").attr("d",function(d){
        var start = {x:d.source.x,y:d.source.y+80+17*d.source.offset};
        var end = {x:d.target.x,y:d.target.y+80+17*d.source.offset};
        return Bezier_curve_generator({source:start,target:end});
      }).attr("fill","none").attr("stroke","yellow").attr("stroke-width",1);
      //标记节点圆心
      var gs = svgUpload.append("g").selectAll("g").data(nodes).enter().append("g").attr("transform",function(d,i){
        var cx = d.x;
        var cy=  d.y+70+17*(i>0?d.parent.offset:0)
        return "translate("+cy+","+cx+")";
      });
      gs.append("rect").data(nodes).attr("x",10).attr('y',-12).attr('width',function (d){return 17*(d.data.name.length>20?20:d.data.name.length)}).attr('height',20).attr("fill","white").attr("stroke","blue").attr("stroke-width",1)
          .on('mousemove',function (){
            d3.select(this).transition().style("fill","red");
          }).on('mouseout',function (){
        d3.select(this).transition().duration(500).style("fill","white");
      })
      //文字
      gs.append("text").attr("x",10)//如果某节点有子节点，则对应的文字前移
          .attr("y",-5).attr("dy",10).text(function(d){return d.data.name;}).attr ('fill','red')
      //     .on('mousemove',function (){
      //   d3.select(this).transition().style("fill","blue");
      // }).on('mouseout',function (){
      //   d3.select(this).transition().duration(500).style("fill","red");}
      .on('click', () =>{
        console.log(this.$data.visible1)
        this.$data.visible1=!this.$data.visible1
        console.log('打开'+this.$data.visible1)
      })

    }
  },
    mounted() {
    // this.test1()
    this.mindMap()
      this.upload1()
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
                    <span slot="title">推荐</span>
                  </el-menu-item>
                  <el-menu-item index="2">
                    <i class="el-icon-s-data"></i>
                    <span slot="title">热门</span>
                  </el-menu-item>
                  <el-menu-item index="3">
                    <i class="el-icon-collection-tag"></i>
                    <span slot="title">标记</span>
                  </el-menu-item>
                  <el-menu-item index="4">
                    <i class="el-icon-s-home"></i>
                    <span slot="title">我的</span>
                  </el-menu-item>
                  <el-menu-item index="5">
                    <i class="el-icon-star-off"></i>
                    <span slot="title">收藏</span>
                  </el-menu-item>
                  <el-menu-item index="6">
                    <i class="el-icon-folder-add"></i>
                    <span slot="title">上传</span>
                  </el-menu-item>
                  <el-menu-item index="7">
                    <i class="el-icon-setting"></i>
                    <span slot="title" @click="click(0)">实验</span>
                  </el-menu-item>
                </el-menu>
            </el-row>
          </el-aside>
<!--       右展示-->
        <el-main>
          <div>
          <el-input v-model="input" style="width: 80%" placeholder="请输入内容"></el-input>
          <el-button type="primary" icon="el-icon-search">搜索</el-button>
            <br>
            <el-table  stripe show-header="false">
              <el-table-column label="标题" prop="name" width="450"></el-table-column >
              <el-table-column label="简介" prop="text"></el-table-column>
              <el-table-column label="作者" prop="text" width="150"></el-table-column>
              <el-table-column label="浏览量" prop="text" width="100" sortable></el-table-column>
              <el-table-column label="收藏" prop="text" width="100" sortable></el-table-column>
              <el-table-column label="日期" style="display: none" prop="date" width="180" sortable></el-table-column>
            </el-table>
          </div>
          <div>
            <h3>行政区划</h3>
            <svg class="test11-1" >
              <rect></rect>
            </svg><br>
              <el-input v-model="input" style="width: 80%;" placeholder="千山万水总是情，留下批注行不行"></el-input>
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
<!--          {{this.visible1}}-->
          <el-popover
              placement="bottom"
              width="320"
              v-model="visible1">
            <div class="text item" >
              <el-input v-model="input" placeholder="请输入内容"></el-input>
              <el-button size="mini" type="text" @click="visible1 = false">添加节点</el-button>
              <el-button type="text" size="mini" @click="visible1 = false">删除节点</el-button>
              <el-button type="text" size="mini" @click="visible1 = false">查看卡片</el-button>
            </div>
          </el-popover>

<!--            上传-->
            <svg class="upload" >
              <rect></rect>
            </svg>
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

<!--// handleOpen(key, keyPath) {-->
<!--//   console.log(key, keyPath);-->
<!--// },-->
<!--// handleClose(key, keyPath) {-->
<!--//   console.log(key, keyPath);-->
<!--// },-->

<!--//   {d3.selectAll('.test1').text("测试1-1成功!!!").style('color','red')-->
<!--//   d3.selectAll('#test1-2').text('测试1-2成功！！！').style('font-size','32px')-->
<!--//   d3.selectAll('.test2-1').style('color','yellow').datum(this.dataset).text(function (d,i){return '测试2-1:数据'+i+':'+d})-->
<!--//   d3.selectAll('.test2-1').style('color','yellow').datum(this.dataset).text(function (d,i){return '测试2-1:数据'+i+':'+d})-->
<!--//   d3.selectAll('.test3-1').append('p').text('测试3-1成功')-->
<!--//   d3.selectAll('.test3-2').insert('p').text('测试3-2成功')-->
<!--//   d3.selectAll('.test3-3').remove()}-->
<!--//   //实验四-->
<!--//   {var width = 400,height = 150,rectHeight = 25-->
<!--//   var svg4_1 =d3.select('svg').style('width',width).style('height',height).style('background',' #42b983').append('svg')-->
<!--//   svg4_1.selectAll('rect').data(this.dataset).enter().append('rect')-->
<!--//       .attr('x',20)-->
<!--//       .attr('y',function (d,i){return i * rectHeight })-->
<!--//       .attr('width',function (d){return d})-->
<!--//       .attr('height',rectHeight-2)-->
<!--//       .attr ('fill','steelblue')}-->
<!--//   //实验五-->
<!--//   {//比例尺-->
<!--//   var linear5_1 = d3.scaleLinear().domain([0,d3.max(this.dataset5_1)]).range([0,width*1.3])-->
<!--//   var svg5_1 =d3.selectAll('.test5-1').style('width',width*1.5).style('height',height*1.5).style('background',' #42b983').append('svg')-->
<!--//   svg5_1.selectAll('rect').data(this.dataset5_1).enter().append('rect')-->
<!--//       .attr('x',30)-->
<!--//       .attr('y',function (d,i){return i * rectHeight * 1.5 })-->
<!--//       .attr('width',function(d){return linear5_1(d);})-->
<!--//       .attr('height',rectHeight * 1.5-3)-->
<!--//       .attr ('fill','steelblue')}-->
<!--//   //实验六-->
<!--//   {var linear6_1 = d3.scaleLinear().domain([0,3500]).range([0,400])-->
<!--//   var svg6_1 =d3.selectAll('.test6-1').style('width',width*1.3).style('height',height*1.7).style('background',' #42b983').append('svg')-->
<!--//   svg6_1.selectAll('rect').data(this.dataset6_1).enter().append('rect')-->
<!--//       .attr('x',20)-->
<!--//       .attr('y',function (d,i){return i * rectHeight*1.5 })-->
<!--//       .attr('width',function(d){return linear6_1(d);})-->
<!--//       .attr('height',rectHeight*1.5-2)-->
<!--//       .attr ('fill','steelblue')-->
<!--//   var xAxis =d3.axisBottom(linear6_1)-->
<!--//   svg6_1.append('g')-->
<!--//       .attr("transform","translate(20,187.5)")-->
<!--//       .call(xAxis);}-->
<!--//   //实验七-->
<!--//   {var svg7_1= d3.select('.test7-1').style('width',400).style('height',400).style('background',' #42b983').append('svg')-->
<!--//   var padding ={left:30,right:30,top:20,bottom:20}-->
<!--//   var xScale7_1=d3.scaleLinear().domain([0,this.dataset7_1.length]).range([0,400-padding.right-padding.left])-->
<!--//   var yScale7_1=d3.scaleLinear().domain([0,d3.max(this.dataset7_1)]).range([400-padding.top-padding.bottom,0])-->
<!--//-->
<!--//   var yAxis7_1=d3.axisLeft(yScale7_1)-->
<!--//   var xAxis7_1=d3.axisBottom(xScale7_1)-->
<!--//   //矩形之间的空白-->
<!--//   var rectPadding7 = 4;-->
<!--//   svg7_1.selectAll('rect').data(this.dataset7_1).enter().append('rect')-->
<!--//       .attr('x',function (d,i){-->
<!--//         return 340/8*i+rectPadding7/2+padding.left-->
<!--//       })-->
<!--//       .attr('y',function (d){return yScale7_1(d)+padding.top })-->
<!--//       .attr("width", 340/8-rectPadding7 )-->
<!--//       .attr("height", function(d){-->
<!--//         return 400 - padding.top - padding.bottom -yScale7_1(d);})-->
<!--//       .attr ('fill','steelblue')-->
<!--//-->
<!--//   svg7_1.append('g')-->
<!--//       .attr("transform","translate(" + padding.left + "," + padding.top + ")")-->
<!--//       .call(yAxis7_1);-->
<!--//-->
<!--//   svg7_1.append('g')-->
<!--//       .attr("transform","translate(" + padding.left + "," + (400 - padding.bottom) + ")")-->
<!--//       .call(xAxis7_1);}-->
<!--//   {var svg8_1= d3.select('.test8-1').style('width',400).style('height',400).style('background',' #42b983').append('svg')-->
<!--//   var xScale8_1=d3.scaleLinear().domain([0,this.dataset7_1.length]).range([0,400-padding.right-padding.left])-->
<!--//   var yScale8_1=d3.scaleLinear().domain([0,d3.max(this.dataset7_1)]).range([400-padding.top-padding.bottom,0])-->
<!--//   var yAxis8_1=d3.axisLeft(yScale8_1)-->
<!--//   var xAxis8_1=d3.axisBottom(xScale8_1)-->
<!--//   //矩形之间的空白-->
<!--//   svg8_1.selectAll('rect').data(this.dataset7_1).enter().append('rect')-->
<!--//       // .append('p').text(function (d){return d;})-->
<!--//       .attr('x',function (d,i){return 340/8*i+rectPadding7/2+padding.left})-->
<!--//       .attr('y',380)-->
<!--//       .attr("width", 340/8-rectPadding7 ).attr ('fill','steelblue')-->
<!--//       // .attr('height',0)-->
<!--//       // .transition().delay(function (d){return 100*d}).duration(3000)-->
<!--//       .attr('height',0)-->
<!--//       .transition().duration(function (d){return 100*d})-->
<!--//       // .delay()-->
<!--//       .attr('y',function (d){return yScale8_1(d)+padding.top })-->
<!--//       .attr("height", function(d){-->
<!--//     return 400 - padding.top - padding.bottom -yScale8_1(d);})-->
<!--//-->
<!--//   // svg8_1.selectAll('p').data(this.dataset7_1).enter().append('p')-->
<!--//   //     .text(function (d){return d;})-->
<!--//   //     .attr('x',function (d,i){return 340/8*i+rectPadding7/2+padding.left})-->
<!--//   //     .attr('y',function (d){return yScale8_1(d)+padding.top })-->
<!--//   svg8_1.append('g')-->
<!--//       .attr("transform","translate(" + padding.left + "," + padding.top + ")")-->
<!--//       .call(yAxis8_1);-->
<!--//   svg8_1.append('g')-->
<!--//       .attr("transform","translate(" + padding.left + "," + (400 - padding.bottom) + ")")-->
<!--//       .call(xAxis8_1);-->
<!--//-->
<!--//   //  svg8_1.selectAll('rect').attr ('fill','steelblue')-->
<!--//   //  .transition().duration(3000).delay(function (d){return 3000+100*d}).attr('fill','red')-->
<!--//   var svg8_2= d3.select('.test8-2').style('width',400).style('height',400).style('background',' #42b983').append('svg')-->
<!--//   var circle1 = svg8_2.append("circle")-->
<!--//       .attr("cx", 100)-->
<!--//       .attr("cy", 100)-->
<!--//       .attr("r", 45)-->
<!--//       .style("fill","green");-->
<!--//   //在1秒（1000毫秒）内将圆心坐标由100变为300-->
<!--//   circle1.transition()-->
<!--//       .duration(1000)-->
<!--//       .attr("cx", 300);-->
<!--//   var circle2 = svg8_2.append("circle")-->
<!--//       .attr("cx", 100)-->
<!--//       .attr("cy", 100)-->
<!--//       .attr("r", 45)-->
<!--//       .style("fill","green");-->
<!--//   //与第一个圆一样，省略部分代码-->
<!--//   //在1.5秒（1500毫秒）内将圆心坐标由100变为300，-->
<!--//   //将颜色从绿色变为红色-->
<!--//   circle2.transition()-->
<!--//       .duration(1500)-->
<!--//       .attr("cx", 300)-->
<!--//       .attr('cy',300)-->
<!--//       .style("fill","red");-->
<!--//   var circle3 = svg8_2.append("circle")-->
<!--//       .attr("cx", 100)-->
<!--//       .attr("cy", 100)-->
<!--//       .attr("r", 45)-->
<!--//       .style("fill","green");-->
<!--//   //与第一个圆一样，省略部分代码-->
<!--//   //在2秒（2000毫秒）内将圆心坐标由100变为300-->
<!--//   //将颜色从绿色变为红色-->
<!--//   //将半径从45变成25-->
<!--//   //过渡方式采用bounce（在终点处弹跳几次）-->
<!--//   circle3.transition()-->
<!--//       .duration(2000)-->
<!--//       .style("fill","red")-->
<!--//       .attr("r", 25);}-->
<!--//   //实验九-->
<!--//   {var svg9_1= d3.select('.test9-1').style('width',400).style('height',400).style('background',' #42b983').append('svg')-->
<!--//   var xScale9_1=d3.scaleLinear().domain([0,this.dataset7_1.length]).range([0,400-padding.right-padding.left])-->
<!--//   var yScale9_1=d3.scaleLinear().domain([0,d3.max(this.dataset7_1)]).range([400-padding.top-padding.bottom,0])-->
<!--//   var yAxis9_1=d3.axisLeft(yScale9_1)-->
<!--//   var xAxis9_1=d3.axisBottom(xScale9_1)-->
<!--//   svg9_1.selectAll('rect').data(this.dataset7_1).enter().append('rect')-->
<!--//       .attr('x',function (d,i){return 340/8*i+rectPadding7/2+padding.left})-->
<!--//       .attr('y',380)-->
<!--//       .attr("width", 340/8-rectPadding7 ).attr ('fill','steelblue')-->
<!--//       .attr('height',0)-->
<!--//       .transition().duration(function (d){return 50*d})-->
<!--//       .attr('y',function (d){return yScale9_1(d)+padding.top })-->
<!--//       .attr("height", function(d){-->
<!--//         return 400 - padding.top - padding.bottom -yScale9_1(d);})-->
<!--//-->
<!--//   svg9_1.append('g')-->
<!--//       .attr("transform","translate(" + padding.left + "," + padding.top + ")")-->
<!--//       .call(yAxis9_1);-->
<!--//   svg9_1.append('g')-->
<!--//       .attr("transform","translate(" + padding.left + "," + (400 - padding.bottom) + ")")-->
<!--//       .call(xAxis9_1);-->
<!--//   svg9_1.selectAll('rect').on('mouseover',function (){-->
<!--//     d3.select(this).transition().style("fill","red");-->
<!--//   }).on('mouseout',function (){-->
<!--//     d3.select(this).transition().duration(500).style("fill","steelblue");-->
<!--//   })}-->
<!--<div>-->
<!--&lt;!&ndash;          <div v-show="this.study" >&ndash;&gt;-->
<!--&lt;!&ndash;          <h2>这是思维导图主页面测试实验</h2>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验一：获取元素</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test1">测试1-1</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test1">测试1-1</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p id="test1-2">测试1-2</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验二：绑定数据</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test2-1">测试2-1</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test2-2">测试2-2数组绑定暂停工</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验三：增删元素</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test3-1">测试3-1</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test3-2">测试3-2</p>&ndash;&gt;-->
<!--&lt;!&ndash;          实验3-3：<p class="test3-3">测试3-3</p>成功&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验四：简单制图（长条）</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test4-1" >&ndash;&gt;-->
<!--&lt;!&ndash;            <rect></rect>&ndash;&gt;-->
<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验五：简单制图（比例尺）</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test5-1" >&ndash;&gt;-->
<!--&lt;!&ndash;            <rect></rect>&ndash;&gt;-->
<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <p class="test2-2">测试5-2序号比例尺暂停工</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验六：坐标轴</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test6-1" >&ndash;&gt;-->
<!--&lt;!&ndash;            <rect class="test6-2"></rect>&ndash;&gt;-->
<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验七：条形图</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test7-1" >&ndash;&gt;-->
<!--&lt;!&ndash;            <rect></rect>&ndash;&gt;-->
<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验八：动图</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test8-1" >&ndash;&gt;-->
<!--&lt;!&ndash;            <rect></rect>&ndash;&gt;-->
<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test8-2" >&ndash;&gt;-->

<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <hr><hr>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验九：交互图</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test9-1" >&ndash;&gt;-->
<!--&lt;!&ndash;          </svg>&ndash;&gt;-->
<!--&lt;!&ndash;          <h3>实验十：树图（思维导图）</h3>&ndash;&gt;-->
<!--&lt;!&ndash;          <svg class="test10-1" >&ndash;&gt;-->
<!--&lt;!&ndash;            <rect></rect>&ndash;&gt;-->
<!--&lt;!&ndash;            <el-button></el-button>&ndash;&gt;-->
<!--&lt;!&ndash;          </svg><br>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;          思维导图页面&ndash;&gt;-->
<!--</div>-->
