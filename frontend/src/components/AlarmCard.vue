<template>
    <div class="b-container">
        <el-card class="box-card">
            <template #header>
                <div class="card-header">
                    <span>警情通报</span>
                    <span> | 处理情况</span>
                </div>
            </template>
            <div style="width: 100%; height: 400px; width: 300px;">
                <b>警情类型：</b>火警
                <hr>
                <b>发生地点：</b>厂房1加工间A
                <hr>
                <b>预估发生时间：</b>14:00:00
                <hr>
                <b>警情报告时间：</b>15:00:00
                <hr>
                <b>警情解决时间：</b>待解决
                <hr>
                <b>警情描述：</b>粉尘爆炸波及整个加工间
                <hr>
                <el-button type="success" @click="dialogFormPost = true">处理</el-button>
                <el-dialog v-model="dialogFormPost" title="警情处理人员调度">
                    <el-form :model="user">
                        <el-form-item label="人员姓名" prop="realname">
                            <el-input v-model="user.realname"></el-input>
                        </el-form-item>
                        <el-form-item label="人员角色" prop="type">
                            <el-input autocomplete="off" v-model="user.type"></el-input>
                        </el-form-item>
                        <el-form-item label="所属部门" prop="department">
                            <el-input autocomplete="off" v-model="user.department"></el-input>
                        </el-form-item>
                    </el-form>
                    <template #footer>
                        <span class="dialog-footer">
                            <el-button @click="dialogFormPost = false">取消</el-button>
                            <el-button type="primary" @click="dialogFormPost = false">
                                确认
                            </el-button>
                        </span>
                    </template>
                </el-dialog>
                <el-button type="danger" @click="dialogprocess = true">删除</el-button>
                <el-dialog v-model="dialogprocess" title="警情处理反馈" width="30%" :before-close="handleClose">
                    <span>警情是否解决？</span>
                    <template #footer>
                        <span class="dialog-footer">
                            <el-button @click="dialogprocess = false">未解决</el-button>
                            <el-button type="primary" @click="dialogprocess = false">
                                确认解决
                            </el-button>
                        </span>
                    </template>
                </el-dialog>
            </div>
        </el-card>
    </div>
</template>

<script lang="ts" setup>
/* eslint-disable */
import { onMounted } from "vue";
import * as echarts from "echarts";
import { reactive, ref } from 'vue'
import { ElMessageBox } from 'element-plus'
import BasicPlot from "@/components/BasicPlot.vue";

const dialogFormPost = ref(false)
const formLabelWidth = '140px'

const user = reactive({
    realname: '',
    type: '',
    department: ''
})

var option7 = {
    tooltip: {
        formatter: ""
    },
    series: [
        {
            type: 'pie',
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
            roseType: 'area'
        }
    ]
};

var option8 = {
    legend: {
        orient: 'vertical',
        right: 10,
        top: 'center',
        data: ['已调度总数', '已调度消防员', '已调度恶劣天气预警人员', '已调度温度调控人员', '已调度设备检修人员', '已调度人员货物排查人员'],
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
            ['区域1', 40, 10, 10, 5, 5, 9, 1],
            ['区域2', 40, 10, 10, 5, 5, 9, 1],
            ['区域3', 40, 10, 10, 5, 5, 9, 1],
            ['区域4', 40, 10, 10, 5, 5, 9, 1],
            ['区域5', 40, 10, 10, 5, 5, 9, 1]
        ]
    },
    xAxis: {},
    yAxis: {
        inverse: true,
        type: 'category',
        data: ['区域1', '区域2', '区域3', '区域4', '区域5']
    },
    series: [{ type: 'bar', data: [40, 40, 40, 40, 40, 40], name: "已调度总数" }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: "已调度消防员" }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: '已调度恶劣天气预警人员' }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: '已调度温度调控人员' }, { type: 'bar', data: [5, 5, 5, 5, 5, 5], name: '已调度设备检修人员' }, { type: 'bar', data: [5, 5, 5, 5, 5, 5], name: '已调度人员货物排查人员' }]
};
var option9 = {
    legend: {
        orient: 'vertical',
        right: 10,
        top: 'center',
        data: ['已调度总数', '已调度消防员', '已调度恶劣天气预警人员', '已调度温度调控人员', '已调度设备检修人员', '已调度人员货物排查人员'],
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
            ['区域1', 40, 10, 10, 5, 5, 9, 1],
            ['区域2', 40, 10, 10, 5, 5, 9, 1],
            ['区域3', 40, 10, 10, 5, 5, 9, 1],
            ['区域4', 40, 10, 10, 5, 5, 9, 1],
            ['区域5', 40, 10, 10, 5, 5, 9, 1]
        ]
    },
    xAxis: {},
    yAxis: {
        inverse: true,
        type: 'category',
        data: ['区域1', '区域2', '区域3', '区域4', '区域5']
    },
    series: [{ type: 'bar', data: [40, 40, 40, 40, 40, 40], name: "已调度总数" }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: "已调度消防员" }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: '已调度恶劣天气预警人员' }, { type: 'bar', data: [10, 10, 10, 10, 10, 10], name: '已调度温度调控人员' }, { type: 'bar', data: [5, 5, 5, 5, 5, 5], name: '已调度设备检修人员' }, { type: 'bar', data: [5, 5, 5, 5, 5, 5], name: '已调度人员货物排查人员' }]
};



const dialogprocess = ref(false)

const handleClose = (done: () => void) => {
    ElMessageBox.confirm('Are you sure to close this dialog?')
        .then(() => {
            done()
        })
        .catch(() => {
            // catch error
        })
}
</script>

<style scoped lang="scss">
.b-container {
    background-color: black;

}

.box-carder {
    background-color: black;
}

.alarm-header {
    height: 5%;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
    //border: 1px solid red;

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

.card-container {
    height: 48%;
    width: 100%;
    display: flex;
    justify-content: space-between;

    div {
        //border: 1px solid red;
        width: 100%;
        align-items: center;
    }
}
</style>
