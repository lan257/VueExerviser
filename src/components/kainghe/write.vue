<script>

import { GetFetch} from "@/tool/fetch";

export default {
    data() {
      return {
        num:123456,
        value: true,
        isEasy:true,
        tableData:[]
    }

  },
  methods:{
    async updateTableData() {
      try {
        const response = this.value
            ? await GetFetch('/CallRecord/getAll')
            : await GetFetch('/AccountTransaction/getAll');

        this.tableData = response.data;
        console.log(this.tableData[1])
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    formatTimestamp(timestamp) {
      const date = new Date(timestamp);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份是 0-11
      const day = String(date.getDate()).padStart(2, '0');
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
      const seconds = String(date.getSeconds()).padStart(2, '0');
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    getDayOfWeek(dateStr) {
      // 替换 '-' 为 '/'，确保兼容 Safari
      const normalizedDateStr = dateStr.replace(/-/g, '/');
      const date = new Date(normalizedDateStr);

      if (isNaN(date.getTime())) {
        throw new Error("无效的日期格式");
      }

      const days = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
      const dayIndex = date.getDay(); // 0（周日）到 6（周六）

      return days[dayIndex];
    }

  },
  watch:{
    async value(){
      await this.updateTableData();
    },
  },
  async created() {
    await this.updateTableData();
  }
}
</script>

<template>
  <el-container>
    <el-header style="height: 100px"><h1>kainghe图表展示</h1></el-header>
    <el-container>
      <el-aside width="200px">
        账单展示
        <el-switch
          v-model="value"
          active-color="#13ce66"
          inactive-color="#13ce66">
      </el-switch>
        话单展示
<!--        <br>-->
<!--        详细{{this.isEasy}}-->
<!--        <el-switch-->
<!--            v-model="isEasy"-->
<!--            active-color="#13ce66"-->
<!--            inactive-color="#13ce66">-->
<!--        </el-switch>-->
<!--        简略-->
      </el-aside>
      <el-main>
<!--        话单-->
        <el-table v-show="value"
          :data="tableData"
          style="width: 100%"
          height="700">
        <el-table-column
            fixed
            prop="id"
            label="账单序号"
            width="150">
        </el-table-column>
          <el-table-column
              prop='aaa'
              label="本人号码"
              width="150">
            13673825321
          </el-table-column>
          <el-table-column
              prop='aaa'
              label="本人户名"
              width="150">
            慕容紫英
          </el-table-column>
          <el-table-column
              prop="callType"
              label="通话类型"
              width="150">
          </el-table-column>
        <el-table-column
            prop="roamingLocation"
            label="通话地(漫游地)"
            width="120">
        </el-table-column>
        <el-table-column
            prop="peerNumber"
            label="对方号码"
            width="300">
        </el-table-column>
          <el-table-column
              prop="startTime"
              label="通话时间"
              width="120">
            <template slot-scope="scope">
              {{formatTimestamp(scope.row.startTime)}}
            </template>
        </el-table-column>
          <el-table-column
              prop='aaa'
              label="星期"
              width="120">
            <template slot-scope="scope">
              {{getDayOfWeek(scope.row.startTime)}}
            </template>
          </el-table-column>
          <el-table-column
              prop="durationSeconds"
              label="时长（秒）"
              width="120">
          </el-table-column>
          <el-table-column
              prop="peerLocation"
              label="对方通话地"
              width="120">
          </el-table-column>
          <el-table-column
              prop="baseStationCode"
              label="LAC"
              width="120">
          </el-table-column>
          <el-table-column
              prop="cellId"
              label="CELL"
              width="120">
            <template slot-scope="scope">
              {{scope.row.cellId.slice(0,4)}}
            </template>
          </el-table-column>

          <el-table-column
              v-show="isEasy"
              prop="endTime"
              label="结束时间"
              width="120">
            <template slot-scope="scope">
              {{formatTimestamp(scope.row.endTime)}}
            </template>
          </el-table-column>


          <el-table-column
            prop="baseFee"
            v-show="isEasy"
            label="基本费(元)"
            width="120">
        </el-table-column>
          <el-table-column
            prop="infoFee"
            v-show="isEasy"
            label=" 信息费(元)"
            width="120">
        </el-table-column>
          <el-table-column
            prop="longDistanceFee"
            v-show="isEasy"
            label="长途费(元)"
            width="120">
        </el-table-column><el-table-column
            prop="discountFee"
            v-show="isEasy"
            label="优惠费(元)"
            width="120">
        </el-table-column><el-table-column
            prop="freeResources"
            v-show="isEasy"
            label="免费资源"
            width="120">
        </el-table-column><el-table-column
            prop="dialMethod"
            v-show="isEasy"
            label="拨打方式"
            width="120">
        </el-table-column>
          <el-table-column
              prop="peerNumberLocation"
              v-show="isEasy"
              label="对端号码归属地"
              width="120">
          </el-table-column>
          <el-table-column
              prop="switchCode"
              v-show="isEasy"
              label="交换机代码"
              width="120">
          </el-table-column>

          <el-table-column
              prop="imei"
              v-show="isEasy"
              label="IMEI号"
              width="120">
          </el-table-column>
          <el-table-column
              prop="discountProcess"
              v-show="isEasy"
              label="优惠过程"
              width="120">
          </el-table-column>
          <el-table-column
              prop="billingProduct"
              v-show="isEasy"
              label="计费产品  "
              width="120">
          </el-table-column>
          <el-table-column
              prop="fileName"
              v-show="isEasy"
              label="文件名"
              width="120">
          </el-table-column>
          <el-table-column
              prop="billingTime"
              v-show="isEasy"
              label="批价处理时间"
              width="120">
            <template slot-scope="scope">
              {{formatTimestamp(scope.row.billingTime)}}
            </template>
          </el-table-column>

      </el-table>
        <!--        账单-->
        <el-table v-show="!value"
                  :data="tableData"
                  style="width: 100%"
                  height="700">
          <el-table-column
              fixed
              prop="id"
              label="话单序号"
              width="150">
          </el-table-column>
          <el-table-column
            prop="counterpartyAccount"
            label="对方账号"
            width="120">
          </el-table-column>
            <!--          贷->存，借->取-->
            <el-table-column
                prop="debitCreditFlag"
                label="存取"
                width="180">
              <template slot-scope="scope">
                {{scope.row.debitCreditFlag === '贷'?'存':'取'}}
              </template>
            </el-table-column>
              <el-table-column
                prop="transactionAmount"
                label="发生额"
                width="300">
            </el-table-column>
              <el-table-column
                prop="balance"
                label="本次余额"
                width="120">
            </el-table-column>
              <el-table-column
                prop="transactionDate"
                label=" 交易日期"
                width="120">
                <template slot-scope="scope">
                  {{scope.row.transactionDate}}
                </template>
            </el-table-column>
<!--          待处理-->
           <el-table-column
               prop="1"
               label="星期"
               width="120">
             <template slot-scope="scope">
               {{getDayOfWeek(scope.row.transactionDate)}}
             </template>
           </el-table-column>
           <el-table-column
             prop="note"
             label="交易类型"
             width="120">
           </el-table-column>
              <el-table-column
                prop="transactionBranch"
                label="交易机构名称"
                width="120">
            </el-table-column>
              <el-table-column
                  prop="aaa"
                  label="摘要"
                  width="120">
              </el-table-column>
          <el-table-column
              prop="currency"
              label="币种"
              width="120">
          </el-table-column>
          <el-table-column
              prop="accountNumber"
              label="账号"
              width="150">
          </el-table-column>
          <el-table-column
              prop="cardNumber"
              v-show="isEasy"
              label="卡号"
              width="120">
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </el-container>

</template>
<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
  text-align: center;
}
</style>


