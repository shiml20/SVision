<template>
    <div class="b-container">
        <BasicHeader :title="title" style="background-color: black; margin-top: 0;"></BasicHeader>
        <div class="card-container">
            <div class="left">
                <div class="item-1">
                    <el-carousel :interval="4000" type="card" height="500px">
                        <el-carousel-item v-for="item in 6" :key="item">
                            <AlarmCard></AlarmCard>
                        </el-carousel-item>
                    </el-carousel>
                </div>

                <div class="item-2">
                    <span>处理进度</span>
                    <el-progress :percentage="50" />
                    <el-progress :percentage="70" status="success" />
                    <el-progress :percentage="60" status="exception" />
                    <el-progress :percentage="100" status="warning" />
                </div>
            </div>
            <div class="right">
                <div class="item-1">
                        <div class="card-header" style="color: #ffffff; font-size: larger">
                            <span>预情处理</span>
                            <span> | 人员调度情况</span>
                        </div>
                        <BasicPlot :option="option_bar_hori"></BasicPlot>
                </div>
                <div class="bottom">
                    <div class="b-left">
                        <BasicPlot :option="option_pie"></BasicPlot>
                    </div>
                    <div class="b-right">
                        <el-table :data="tableData" style="width: 100%;" max-height="250" 
                            row-style="background-color:black; font-size: small;"
                            header-row-style="background-color:black; color:black; font-size: small;"
                            >
                                <el-table-column prop="date" label="调度时间" width="100" />
                                <el-table-column prop="desc" label="警情描述" width="60"/>
                                <el-table-column prop="name" label="处理人员" width="60" />
                                <el-table-column prop="type" label="人员身份" width="60" />
                                <el-table-column prop="status" label="处理状态" width="60" />
                                <el-table-column prop="place" label="处理地点" width="120" />
                                <el-table-column fixed="right" label="操作" width="50" style="background-color:black;">
                                  <template #default="scope">
                                    <el-button
                                      link
                                      type="primary"
                                      size="small"
                                      @click.prevent="deleteRow(scope.$index)"
                                    >
                                      删除
                                    </el-button>
                                  </template>
                                </el-table-column>
                              </el-table>
                              <el-button class="mt-4" style="width: 100%; font-size: large; font-weight:1000" @click="onAddItem"
                                >增加调度人员</el-button
                              >
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<script lang="ts" setup>
/* eslint-disable */
import { onMounted } from "vue";
import * as echarts from "echarts";
import { reactive, ref } from 'vue'
import { ElMessageBox } from 'element-plus'
import BasicPlot from "@/components/BasicPlot.vue";
import AlarmCard from "@/components/AlarmCard.vue";
import BasicHeader from '@/components/BasicHeader.vue';
import dayjs from 'dayjs'

const title = "警情处理"

const dialogFormPost = ref(false)
const formLabelWidth = '140px'

const user = reactive({
    realname: '',
    type: '',
    department: ''
})

var option_pie = {
    backgroundColor: '#272822',
    tooltip: {
        formatter: "",
        trigger: 'item',
    },
    legend: {
    top: '5%',
    left: 'center',
    textStyle: {
           color: '#fff'
      }
    },
    series: [
        {
            type: 'pie',
            center: ['50%', '60%'],
            data: [
                {
                    value: 100,
                    name: '区域1'
                },
                {
                    value: 200,
                    name: '区域2'
                },
                {
                    value: 300,
                    name: '区域3'
                },
                {
                    value: 400,
                    name: '区域4'
                },
                {
                    value: 500,
                    name: '区域5'
                }
            ],
            roseType: 'area',
            label: {
                show: false
            },
        }
    ]
};

var option_bar_hori = {
    backgroundColor: '#272822',
    legend: {
        orient: 'vertical',
        right: 10,
        top: 'center',
        data: ['已调度总数', '已调度消防员', '已调度恶劣天气预警人员', '已调度温度调控人员', '已调度设备检修人员', '已调度人员货物排查人员'],
        textStyle: {
            color: "#ffffff"
        }
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        },

    },
    dataset: {
        source: [
            ['product', '已调度总数', '已调度消防员', '已调度恶劣天气预警人员', '已调度温度调控人员', '已调度设备检修人员', '已调度人员货物排查人员'],
            ['区域1', 20, 10, 10, 5, 5, 9, 1],
            ['区域2', 20, 10, 10, 5, 5, 9, 1],
            ['区域3', 20, 10, 10, 5, 5, 9, 1],
            ['区域4', 20, 10, 10, 5, 5, 9, 1],
            ['区域5', 20, 10, 10, 5, 5, 9, 1]
        ]
    },
    xAxis: {
        axisLabel: {
            textStyle: {
                color: "#ffffff"
            }
        }
    },
    yAxis: {
        inverse: true,
        type: 'category',
        data: ['区域1', '区域2', '区域3', '区域4', '区域5'],
        axisLabel: {
            color: "#ffffff"
        }
    },
    series: [{ type: 'bar', data: [20, 20, 20, 20, 20, 20], name: "已调度总数" }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: "已调度消防员" }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: '已调度恶劣天气预警人员' }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: '已调度温度调控人员' }, { type: 'bar', data: [5, 5, 5, 5, 5, 5], name: '已调度设备检修人员' }, { type: 'bar', data: [5, 5, 5, 5, 5, 5], name: '已调度人员货物排查人员' }]
};

const dialogprocess = ref(false)

const handleClose = (done:any) => {
    ElMessageBox.confirm('Are you sure to close this dialog?')
        .then(() => {
            done()
        })
        .catch(() => {
            // catch error
        })
}


const tableData = ref([
  {
        "date":"2023-02-19 17:30",
        "desc":"监控损坏",
        "name":"王大明",
        "type":"设备检修人员",
        "status":"正在检修",
        "place":"区域1厂房A监控室",
  },
  {
        "date":"2023-02-20 14:30",
        "desc":"消防设施损坏",
        "name":"陈大明",
        "type":"设备检修人员",
        "status":"待处理",
        "place":"区域2消防站",
  },
  {
        "date":"2023-02-21 9:30",
        "desc":"厂房温度异常",
        "name":"王小明",
        "type":"温度调控人员",
        "status":"处理完毕",
        "place":"区域5货仓B",
  },
])

const deleteRow = (index: number) => {
  tableData.value.splice(index, 1)
}
const now = new Date()
const onAddItem = () => {
  now.setDate(now.getDate() + 1)
  tableData.value.push({
    date: dayjs(now).format('YYYY-MM-DD'),
    desc: '消防设施损坏',
    name: '王大壮',
    type: '维修人员',
    status: '待处理',
    place: "X区域6号仓库",
  })
}

</script>

<style scoped lang="scss">
.b-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    .card-container {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: space-between;
        margin-bottom: 4%;

        .left {
            margin-right: 3%;
            padding-left: 1%;
            width: 50%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            .item-1 {
                height: 70%;
                background-color: #272822;
                border-radius: 20px;
            }

            .item-2 {
                height: 25%;
                div {
                    padding: 10px 0;
                }
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                color: white;
                padding: 0 10%;
                align-content: center;
                font-size: large;
                background-color: #272822;
                border-radius: 20px;
            }
        }

        .right {
            width: 47%;
            display: flex;
            flex-direction: column;

            .item-1 {
                height: 60%;
                width: 100%;
                background-color: #272822;
                border-radius: 20px;
            }
            .bottom {
                width: 100%;
                height: 40%;
                display: flex;
                justify-content: space-between;                
                .b-left {
                    margin-top: 3%;
                    width: 40%;
                    height: 100%;
                    border-radius: 20px;
                    background-color: #272822;
                }

                .b-right {
                    margin-top: 3%;
                    width: 55%;
                    height: 100%;
                    border-radius: 20px;
                    background-color: #272822;
                }
            }
        }

        //div {
        //
         //   border: 1px solid red;
        //}
    }



}
    
.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

.alarm-header {
    height: 5%;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
    border: 1px solid red;

    color: black;
    display: flex;
    justify-content: space-between;

    .weather-report {
        font-size: 50px;
        color: black;
    }
}

.el-row {
    /* 行与行之间的间隙 */
    margin-bottom: 0px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.dialog-footer button:first-child {
    margin-right: 10px;
}


.el-table .warning-row {
    --el-table-tr-bg-color: var(--el-color-warning-light-9);
}

.el-table .success-row {
    --el-table-tr-bg-color: var(--el-color-success-light-9);
}
</style>
