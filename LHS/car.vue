<template>
  <el-row>
    <el-col :span="24" style="margin-bottom:20px">
      <el-card shadow="always">
        <div class="title"> 车辆进出记录</div>
      </el-card>
    </el-col>
  </el-row>
  <el-row :gutter="20" style="margin-bottom:20px">
    <el-col :span="6">
      <el-card shadow="always">
        <div>当日入营车辆 {{ todayIn }} 辆</div>
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card shadow="always">
        <div>当日出营车辆 {{ todayOut }} 辆</div>
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card shadow="always">
        <div>当日重点关注车辆 {{ todayCar }} 辆</div>
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card shadow="always">
        <div>车辆缴费总额 {{ todaymoney }} 元</div>
      </el-card>
    </el-col>
  </el-row>
  <!-- <el-row class="search-row">
    <el-col>
      <el-card class="search-card" shadow="always ">
        <el-row>
          <el-card class="time-search-card" shadow="hover">
            <template #header>
              <div class="card-header">
                <span>查询时间</span>
                <el-button class="button" text>查询</el-button>
              </div>
            </template>

            <div class="demo-date-picker">
              <div class="block" style="text-align:center">
                <el-date-picker type="date" placeholder="请选择日期" />
              </div>
            </div>
            <div style="text-align: center;margin: 10px;">入营时间范围</div>
            <div class="demo-range">
              <el-time-picker is-range range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间" />
            </div>
            <div style="text-align: center;margin: 10px;">出营时间范围</div>
            <div class="demo-range">
              <el-time-picker is-range range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间" />
            </div>
          </el-card>
        </el-row>
      </el-card>
    </el-col>
  </el-row> -->
  <el-table :data="tableData" style="width: 100%" height="500">
    <!-- <el-table-column type="selection" width="50" :selectable="checkSelectable" /> -->
    <el-table-column fixed="left" type="selection" width="40" />
    <el-table-column v-for="(val, key) in tableLabel" :key="key" :prop="key" :label="val"
      :width="150"></el-table-column>
    <!-- <el-table-column fixed="right" width="180">
      <template #header>
        <el-input v-model="search" size="small" placeholder="Type to search" />
      </template>
      <template #default="scope">
        <el-button size="small" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
      </template>
    </el-table-column> -->
    <el-table-column fixed="right" label="操作" width="60">
      <template #default>
        <el-button link type="primary" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-pagination small background layout="prev, pager, next" :total="config.total" @current-change="changePage"
    class="mt-4" />
</template>
<!-- 
<script lang="ts" setup>
import { ref } from 'vue'

const size = ref<'default' | 'large' | 'small'>('default')

const value1 = ref('')
const value2 = ref('')

const shortcuts = [
  {
    text: 'Today',
    value: new Date(),
  },
  {
    text: 'Yesterday',
    value: () => {
      const date = new Date()
      date.setTime(date.getTime() - 3600 * 1000 * 24)
      return date
    },
  },
  {
    text: 'A week ago',
    value: () => {
      const date = new Date()
      date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
      return date
    },
  },
]

const disabledDate = (time: Date) => {
  return time.getTime() > Date.now()
}
</script> -->

<script>
import { defineComponent, getCurrentInstance, onMounted, ref, reactive } from 'vue';
import axios from "axios";
export default defineComponent({
  setup() {
    // const { proxy } = getCurrentInstance();
    const config = reactive({
      total: 0,
      page: 1,
    })
    // const { proxy } = getCurrentInstance();
    let todayIn = ref();
    let todayOut = ref();
    let todaymoney = ref();
    let todayCar = ref();
    let tableData = ref([]);
    const getCarData = async () => {

      //let res = await proxy.$api.getCarData();
      // console.log(res)
      await axios.get("/car/getData").then((res) => {
        console.log(res);
        if (res.data.code == 200) {
          tableData.value = res.data.data.tableData;
        }
      });
      // console.log(res);
      tableData.value = res;
      todayIn.value = 0;
      todayOut.value = 0;
      todaymoney.value = 0;
      todayCar.value = 0;
      //获取当前日期 格式为 2023/02/06
      var date = new Date().toISOString().substring(0, 10);
      // console.log(tableData.value);
      // console.log(tableData.value[0].intime);
      for (var i = 0; i < tableData.value.length; i++) {
        var Intime = tableData.value[i].intime.substring(0, 10);
        var Outtime = tableData.value[i].outtime.substring(0, 10);
        var Money = tableData.value[i].money;
        if (Intime == date) todayIn.value++;
        if (Outtime == date) todayOut.value++;
        if (Money != NaN) todaymoney.value += Money;
      };
      // tableData.value = res.tabledata;
      // console.log(tableData);
    }
    const tableLabel = {
      num: "车牌号",
      type: "种类",
      usertype: "类型",
      intime: "入营时间",
      outtime: "出营时间",
      outstatus: "当前状态",
      name: "车主姓名",
      phone: "联系方式",
      money: "缴费情况",
    }
    onMounted(() => {
      getCarData();
    })
    const changePage = (page) => {
      // console.log(page);
      config.page = page;
    }
    return { tableData, tableLabel, todayIn, todayOut, todaymoney, todayCar, config, changePage }
  }
})
</script>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}
</style>