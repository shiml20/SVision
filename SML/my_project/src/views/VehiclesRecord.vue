<template>
    <!-- <div class="common-layout"> -->
    <el-container>
        <el-header style="text-align: right; font-size: 12px">
            <div class="toolbar">
                <el-dropdown>
                    <el-icon style="margin-right: 8px; margin-top: 1px">
                        <setting />
                    </el-icon>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item>View</el-dropdown-item>
                            <el-dropdown-item>Add</el-dropdown-item>
                            <el-dropdown-item>Delete</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
                <span>Tom</span>
            </div>
        </el-header>
        <div class="query-box">
            <el-date-picker v-model="datevalue" type="date" placeholder="选择日期"></el-date-picker>
            <el-time-select v-model="startTime" :max-time="endTime" class="mr-4" placeholder="Start time" start="08:30"
                step="00:15" end="18:30" />
            <el-time-select v-model="endTime" :min-time="startTime" placeholder="End time" start="08:30" step="00:15"
                end="18:30" />
            <el-button type="primary" round @click="dialogAddVisible = true;">
                添加资源
            </el-button>
            <!-- 提示信息 -->
        </div>
        <el-alert title="success alert" type="success" show-icon description="success"
            v-if="showMessage == true && alertMessage == 'ADD_SUCCESS'" />
        <el-alert title="error alert" type="error" show-icon description="failed"
            v-if="showMessage == true && alertMessage == 'ADD_FAILED'" />
        <el-alert title="success alert" type="success" show-icon description="update success"
            v-if="showMessage == true && alertMessage == 'UPDATE_SUCCESS'" />
        <el-alert title="success alert" type="success" show-icon description="delete success"
            v-if="showMessage == true && alertMessage == 'DELETE_SUCCESS'" />
        <el-alert title="success alert" type="error" show-icon description="delete failed"
            v-if="showMessage == true && alertMessage == 'DELETE_FAILED'" />
        <!-- 表单 -->
        <br>
        <div id="big">
            <el-table :data="resources" border style="width: 100%">
                <el-table-column type="selection" width="55" />
                <el-table-column prop="license" label="车牌号" align="center" />
                <el-table-column prop="type" label="车辆类型" align="center" />
                <el-table-column prop="whyin" label="出入类型" align="center" />
                <el-table-column prop="intime" label="入营时间" width=160 align="center" />
                <el-table-column prop="outtime" label="出营时间" width=160 align="center" />
                <el-table-column prop="isin" label="当前状态" align="center" />
                <el-table-column prop="ownername" label="车主姓名" align="center" />
                <el-table-column prop="phone" label="联系方式" align="center" />
                <el-table-column prop="pay" label="是否缴款" align="center" />
                <el-table-column fixed="right" label="操作" align="center">
                    <template #default="scope">
                        <el-button size="small" @click="dialogUpdateVisible = true">编辑</el-button>
                        <el-button size="small" type="danger"
                            @click="tobeDeleted = scope.row.license; dialogDeleteVisible = true">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <div>
            <el-dialog v-model="dialogAddVisible" title="Add Dialog">
                <el-form :model="addResForm">
                    <el-form-item label="车牌号" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.license" autocomplete="off" placeholder="输入车牌号" />
                    </el-form-item>
                    <el-form-item label="车辆类型" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.type" autocomplete="off" placeholder="输入车辆类型" />
                    </el-form-item>
                    <el-form-item label="出入类型" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.whyin" autocomplete="off" placeholder="出入类型" />
                    </el-form-item>
                    <el-form-item label="入营时间" :label-width="formLabelWidth">
                        <!-- <el-input v-model="addResForm.intime" autocomplete="off" placeholder="入营时间" /> -->
                        <div class="block">
                            <!-- <span class="demonstration">With shortcuts</span> -->
                            <el-date-picker
                              v-model="addResForm.intime"
                              type="datetime"
                              placeholder="Select date and time"
                              :shortcuts="shortcuts"
                            />
                          </div>
                    </el-form-item>

                    <el-form-item label="出营时间" :label-width="formLabelWidth">
                        <!-- <el-input v-model="addResForm.outtime" autocomplete="off" placeholder="出营时间" /> -->
                        <div class="block">
                            <!-- <span class="demonstration">With shortcuts</span> -->
                            <el-date-picker
                              v-model="addResForm.outtime"
                              type="datetime"
                              placeholder="Select date and time"
                              :shortcuts="shortcuts"
                              format="YYYY/MM/DD HH:mm:ss"
                            />
                          </div>
                    </el-form-item>
                    <el-form-item label="当前状态" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.isin" autocomplete="off" placeholder="当前状态" />
                    </el-form-item>
                    <el-form-item label="车主姓名" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.ownername" autocomplete="off" placeholder="车主姓名" />
                    </el-form-item>
                    <el-form-item label="联系方式" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.phone" autocomplete="off" placeholder="联系方式" />
                    </el-form-item>
                    <el-form-item label="缴费记录" :label-width="formLabelWidth">
                        <el-input v-model="addResForm.pay" autocomplete="off" placeholder="缴费记录" />
                    </el-form-item>
                </el-form>
                <template #footer>
                    <span class="dialog-footer">
                        <el-button @click="dialogAddVisible = false">Cancel</el-button>
                        <el-button @click="onReset">Reset</el-button>
                        <el-button v-if="addResForm.license != ''" type="primary"
                            @click="dialogAddVisible = false; onSubmit(); showMessage = true">
                            确定
                        </el-button>
                    </span>
                </template>
            </el-dialog>
        </div>

        <div>
            <el-dialog v-model="dialogUpdateVisible" title="Update dialog">
                <el-form :model="editResForm">
                    <el-form-item label="Date" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.license" autocomplete="off" placeholder="输入车牌号" />
                    </el-form-item>
                    <el-form-item label="Name" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.type" autocomplete="off" placeholder="输入车辆类型" />
                    </el-form-item>
                    <el-form-item label="Address" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.whyin" autocomplete="off" placeholder="出入类型" />
                    </el-form-item>
                    <el-form-item label="入营时间" :label-width="formLabelWidth">
                        <!-- <el-input v-model="addResForm.intime" autocomplete="off" placeholder="入营时间" /> -->
                        <div class="block">
                            <!-- <span class="demonstration">With shortcuts</span> -->
                            <el-date-picker
                              v-model="editResForm.intime"
                              type="datetime"
                              placeholder="Select date and time"
                              :shortcuts="shortcuts"
                            />
                          </div>
                    </el-form-item>

                    <el-form-item label="出营时间" :label-width="formLabelWidth">
                        <!-- <el-input v-model="addResForm.outtime" autocomplete="off" placeholder="出营时间" /> -->
                        <div class="block">
                            <!-- <span class="demonstration">With shortcuts</span> -->
                            <el-date-picker
                              v-model="editResForm.outtime"
                              type="datetime"
                              placeholder="Select date and time"
                              :shortcuts="shortcuts"
                              format="YYYY/MM/DD HH:mm:ss"
                            />
                          </div>
                    </el-form-item>

                    <el-form-item label="Address" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.isin" autocomplete="off" placeholder="当前状态" />
                    </el-form-item>
                    <el-form-item label="Address" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.ownername" autocomplete="off" placeholder="车主姓名" />
                    </el-form-item>
                    <el-form-item label="Address" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.phone" autocomplete="off" placeholder="联系方式" />
                    </el-form-item>
                    <el-form-item label="Address" :label-width="formLabelWidth">
                        <el-input v-model="editResForm.pay" autocomplete="off" placeholder="缴费记录" />
                    </el-form-item>
                </el-form>
                <template #footer>
                    <span class="dialog-footer">
                        <el-button @click="dialogUpdateVisible = false">Cancel</el-button>
                        <el-button @click="onReset">Reset</el-button>
                        <el-button v-if="addResForm.license != ''" type="primary"
                            @click="dialogUpdateVisible = false; onSubmitUpdate(); showMessage = true">
                            确定
                        </el-button>
                    </span>
                </template>
            </el-dialog>
        </div>

        <div>
            <el-dialog v-model="dialogDeleteVisible" title="Delete Dialog" width="30%" draggable>
                <span>Want to delete?</span>
                <template #footer>
                    <span class="dialog-footer">
                        <el-button @click="dialogDeleteVisible = false">Cancel</el-button>
                        <el-button type="primary"
                            @click="dialogDeleteVisible = false; removeRes(tobeDeleted); showMessage = true">
                            Confirm
                        </el-button>
                    </span>
                </template>
            </el-dialog>
        </div>
        <el-main>

        </el-main>
    </el-container>
    <!-- </div> -->
</template>

<script lang="ts" setup>
/* eslint-disable */
import { reactive, ref } from 'vue'
import axios from 'axios'
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'
import { ElTable } from 'element-plus'

const intime = ref('')
const outtime = ref('')
const datevalue = ref('')
const startTime = ref('')
const endTime = ref('')
const goBack = () => {
    console.log('go back')
}

const defaultTime = new Date(2000, 1, 1, 12, 0, 0)

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


const dialogAddVisible = ref(false)
const dialogUpdateVisible = ref(false)
const dialogDeleteVisible = ref(false)
const formLabelWidth = '140px'
const showMessage = ref(false)
const alertMessage = ref('')
let tobeDeleted = ref('')

const addResForm = reactive({
    license: '',
    type: '',
    whyin: '',
    isin: '',
    intime: '',
    outtime: '',
    ownername: '',
    phone: '',
    pay: 0,
})



const editResForm = reactive({
    license: '',
    type: '',
    whyin: '',
    isin: '',
    intime: defaultTime,
    outtime: defaultTime,
    ownername: '',
    phone: '',
    pay: 0,
})

function initF(Form: any) {
    Form.license = '';
    Form.type = '';
    Form.whyin = '';
    Form.isin = '';
    Form.intime = defaultTime;
    Form.outtime = defaultTime;
    Form.ownername = '';
    Form.phone = '';
    Form.pay = 0;
}

function initForm() {
    initF(addResForm)
    initF(editResForm)
}


const path = 'http://localhost:5000/vehicles'
const resources = ref<any>([])

const moment = require('moment')



function getResources() {
    console.log(addResForm)
    axios.get(path)
        .then((res) => {
            console.log(res.data)
            res.data.resources.forEach((element: any) => {
                resources.value.push(element)
                // console.log(element)
            })
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
        })
}

function addRes(payload: {}) {
    axios.post(path, payload)
        .then((res) => {
            resources.value = [] // 如果不加这句的话就会重复渲染！！！！！！ 202301290226
            console.log(resources)
            getResources()
            alertMessage.value = res.data.message
            var success = res.data.status
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
            getResources()
        })
}

function onSubmit() {
    // evt.preventDefault();
    let isin = false;
    if (addResForm.isin == '1') isin = true;
    // console.log(address)
    
    const intimestr = moment(addResForm.intime).format('YYYY-MM-DD HH:mm:ss')
    const outtimestr = moment(addResForm.outtime).format('YYYY-MM-DD HH:mm:ss')
    const payload = {
        license: addResForm.license,
        type: addResForm.type,
        whyin: addResForm.whyin,
        isin: isin,
        intime: intimestr,
        outtime: outtimestr,
        ownername: addResForm.ownername,
        phone: addResForm.phone,
        pay: addResForm.pay
    };
    console.log(payload)

    addRes(payload)
    initForm()
}

function onSubmitUpdate() {
    let isin = false;
    if (editResForm.isin == '1') isin = true;
    const intimestr = moment(addResForm.intime).format('YYYY-MM-DD HH:mm:ss')
    const outtimestr = moment(addResForm.outtime).format('YYYY-MM-DD HH:mm:ss')
    const payload = {
        license: addResForm.license,
        type: addResForm.type,
        whyin: addResForm.whyin,
        isin: isin,
        intime: intimestr,
        outtime: outtimestr,
        ownername: addResForm.ownername,
        phone: addResForm.phone,
        pay: addResForm.pay
    };
    console.log(payload)
    updateRes(payload, editResForm.license)
    initForm()
}

function updateRes(payload: {}, license: string) {
    const _path = `http://localhost:5000/vehicles/${license}`
    axios.put(_path, payload)
        .then((res) => {
            resources.value = [] // 如果不加这句的话就会重复渲染！！！！！！ 202301290226
            console.log(resources)
            alertMessage.value = res.data.message
            getResources()
            console.log(alertMessage)
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
            getResources()
        })
}


function removeRes(license: string) {
    console.log(license)
    const _path = `http://localhost:5000/vehicles/${license}`;
    axios.delete(_path)
        .then((res) => {
            resources.value = [] // 如果不加这句的话就会重复渲染！！！！！！ 202301290226
            alertMessage.value = res.data.message
            getResources();
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            getResources();
        });
}

function onReset() {
    // evt.preventDefault();
    initForm()
}

getResources()
</script>


<style scoped>
.query-box {
    display: flex;
    margin: 10px;

}

.h1-text {
    margin: 1%;
    color: #337ecc;
}

.el-button--text {
    margin-right: 15px;
}

.el-select {
    width: 300px;
}

.el-input {
    width: 300px;
}

.dialog-footer button:first-child {
    margin-right: 10px;
}

#big {
    width: 100%;
    margin: auto;
}

.common-layout .el-header {
    position: relative;
    background-color: var(--el-color-primary-light-7);
    color: var(--el-text-color-primary);
}

.layout-container-demo .el-aside {
    color: var(--el-text-color-primary);
    background: var(--el-color-primary-light-8);
}

.layout-container-demo .el-menu {
    border-right: none;
}

.layout-container-demo .el-main {
    padding: 0;
}

.common-layout .toolbar {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    right: 20px;
    font-size: larger;
}
</style>