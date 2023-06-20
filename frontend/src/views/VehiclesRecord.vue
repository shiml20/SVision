<template>
    <div class="vehicles-container">
            <!-- 页眉 -->
            <el-header>
            <!-- 搜索栏 -->
            <div class="query-box">
                <div class="start-time">
                    <span class="demonstration"></span>
                    <el-date-picker v-model="startTime" type="datetime" placeholder="输入开始时间" :shortcuts="shortcuts" />
                </div>
                <div class="end-time">
                    <span class="demonstration"></span>
                    <el-date-picker v-model="endTime" type="datetime" placeholder="输入结束时间" :shortcuts="shortcuts" />
                </div>
                <div class="icon-search">
                    <el-icon @click="isSearch = !isSearch">
                        <Search />
                    </el-icon>
                </div>
                <div class="button-add" >
                    <el-button type="primary" round @click="dialogAddVisible = true;">
                        添加资源
                    </el-button>
                </div>
            </div>
            </el-header>
            <!-- 数据信息栏 -->
            <div class="vehicles-info">
                <div class="info-left">
                    <span>当日入营车辆</span>
                    <span class="num-left">349辆</span>
                </div>
                <div class="info-mid">
                    <span>当日出营车辆</span>
                    <span class="num-mid-1">300辆</span>
                </div>
                <div class="info-mid">
                    <span>重点关注车辆</span>
                    <span class="num-mid-2">65辆</span>
                </div>
                <div class="info-right">
                    <span>车费缴纳总额</span>
                    <span class="num-right">1090元</span>
                </div>
            </div>
            <!-- 信息提示栏 -->
            <div>
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
            </div>
            <!-- <br> 这个标签可以加一个空白行 -->
            <!-- 数据表格 -->
            <div id="big">
                <el-scrollbar height="700px">
                    <el-table 
                    :data="resources" 
                    :default-sort="{ prop: 'id', order: 'descending' }"
                    border style="width: 100%;">
                        <el-table-column type="selection" width="55" />
                        <el-table-column prop="id" label="序号" width=55 sortable align="center" />
                        <el-table-column prop="license" label="车牌号" align="center" />
                        <el-table-column prop="type" label="车辆类型" align="center" />
                        <el-table-column prop="whyin" label="出入类型" align="center" />
                        <el-table-column prop="intime" label="入营时间" width=165 align="center" />
                        <el-table-column prop="outtime" label="出营时间" width=165 align="center" />
                        <el-table-column prop="isin" label="当前状态" align="center" />
                        <el-table-column prop="ownername" label="车主姓名" align="center" />
                        <el-table-column prop="phone" label="联系方式" align="center" />
                        <el-table-column prop="pay" label="是否缴款" align="center" />
                        <el-table-column fixed="right" label="操作" align="center">
                            <template #default="scope">
                                <el-button size="small" 
                                @click="dialogUpdateVisible = true; editResForm.license = scope.row.license ">编辑</el-button>
                                <el-button size="small" type="danger"
                                    @click="tobeDeleted = scope.row.id; dialogDeleteVisible = true">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-scrollbar>
            </div>
            <!-- 分页栏 -->
            <div class="demo-pagination-block">
                <div class="demonstration"></div>
                <el-pagination
                  v-model:current-page="currentPage"
                  v-model:page-size="pageSize"
                  :small="small"
                  :disabled="disabled"
                  :background="background"
                  layout="prev, pager, next, jumper"
                  :total="totalPage"
                  @size-change="handleSizeChange"
                  @current-change="handleCurrentChange"
                />
              </div>
            <!-- 增加数据的模态框 -->
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
            <!-- 更新数据的模态框 -->
            <div>
                <el-dialog v-model="dialogUpdateVisible" title="Update dialog">
                    <el-form :model="editResForm">
                        <el-form-item label="车牌号" :label-width="formLabelWidth">
                            <el-input v-model="editResForm.license" autocomplete="off" placeholder="输入车牌号" />
                        </el-form-item>
                        <el-form-item label="车辆类型" :label-width="formLabelWidth">
                            <el-input v-model="editResForm.type" autocomplete="off" placeholder="输入车辆类型" />
                        </el-form-item>
                        <el-form-item label="出入类型" :label-width="formLabelWidth">
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
    
                        <el-form-item label="当前状态" :label-width="formLabelWidth">
                            <el-input v-model="editResForm.isin" autocomplete="off" placeholder="当前状态" />
                        </el-form-item>
                        <el-form-item label="车主姓名" :label-width="formLabelWidth">
                            <el-input v-model="editResForm.ownername" autocomplete="off" placeholder="车主姓名" />
                        </el-form-item>
                        <el-form-item label="联系方式" :label-width="formLabelWidth">
                            <el-input v-model="editResForm.phone" autocomplete="off" placeholder="联系方式" />
                        </el-form-item>
                        <el-form-item label="缴费记录" :label-width="formLabelWidth">
                            <el-input v-model="editResForm.pay" autocomplete="off" placeholder="缴费记录" />
                        </el-form-item>
                    </el-form>
                    <template #footer>
                        <span class="dialog-footer">
                            <el-button @click="dialogUpdateVisible = false">Cancel</el-button>
                            <el-button @click="onReset">Reset</el-button>
                            <el-button v-if="editResForm.license != ''" type="primary"
                                @click="dialogUpdateVisible = false; onSubmitUpdate(); showMessage = true">
                                确定
                            </el-button>
                        </span>
                    </template>
                </el-dialog>
            </div>
            <!-- 删除数据的模态框 -->
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
    </div>

</template>

<script lang="ts" setup>
/* eslint-disable */
import { reactive, ref, watch, onMounted } from 'vue'
import axios from 'axios'
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'
import { ElTable } from 'element-plus'


// 对话框数据区
const dialogAddVisible = ref(false)
const dialogUpdateVisible = ref(false)
const dialogDeleteVisible = ref(false)
const formLabelWidth = '140px'
const showMessage = ref(false)
const alertMessage = ref('')
let tobeDeleted = ref('')

// 该单组件页面获取后端数据的路径
const path = 'http://127.0.0.1:5000/vehicles/'
const resources = ref<any>([])
const moment = require('moment')
// 分页数据表
const currentPage = ref(1)
const pageSize = ref(10)
const totalPage = ref(1)
const small = ref(false)
const background = ref(false)
const disabled = ref(false)
// 点击数据表
const isSearch = ref(false)
// 时间数据区
const startTime = ref('')
const endTime = ref('')
const defaultTime = new Date(2000, 1, 1, 12, 0, 0)

const addResForm = reactive({
    id: 0,
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
    id: 0,
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

// 初始化函数
function initF(Form: any) {
    Form.id = 0
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

function onReset() {
    initForm()
}



// 挂载函数
onMounted(() => {
    getResources()
})


// 将时间格式的数据转换成字符串
function time2str(dateTime: any){
    if (dateTime)
        return moment(dateTime).format('YYYY-MM-DD HH:mm:ss')
    else return "" 
}

// 查找处理函数
// search请求的参数
const args = ref({})
function getResources(){
    args.value = {
        "time_begin": time2str(startTime.value),
        "time_end": time2str(endTime.value),
        "type": "",
        "isin": null,
        "license": "",
        "page_num":  currentPage.value,
        "per_page": pageSize.value
    }
    // console.log("string is", typeof(""))
    // console.log("2 is", typeof(startTime.value)) 
    // console.log("3 is",typeof(time2str(startTime.value)), time2str(startTime.value))  
    console.log("4 is", startTime.value)
    time2str(startTime.value)
    const _path = 'http://127.0.0.1:5000/vehicles/search'
    axios.post(_path, args.value)
        .then((res) => {
            // console.log(res.data)
            resources.value = []
            // console.log(res.data.data.items)
            res.data.data.items.forEach((element: any) => {
                resources.value.push(element)
                // console.log(element)
            })

            // 返回的全部数量
            totalPage.value =  res.data.data.total
            // console.log(resources)
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
        })
}

// 监听currentPage的值改变，从而能够更新数据渲染
watch(currentPage, getResources)
watch(isSearch, getResources)

// 增删改处理函数

function addRes(payload: {}) {
    const _path = 'http://127.0.0.1:5000/vehicles/'
    axios.post(_path, payload)
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

function updateRes(payload: {}, id: any) {
    const _path = `http://localhost:5000/vehicles/${id}`
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

function removeRes(id: any) {
    console.log(id)
    const _path = `http://localhost:5000/vehicles/${id}`;
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

const handleSizeChange = (val: number) => {
  console.log(`${val} items per page`)
}
const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
}




</script>


<style scoped lang="scss">

.vehicles-container {
    background: #e6e6e6;
    height: 100%;
    width: 100%;
}
.vehicles-info {
    display: flex;
    justify-content: space-between;

    div{
        //border: 1px solid red;
        border-radius: 5px;
    }
    .info-left {
        margin: 5px 5px;
        padding: 5px 5px;
        font-size: medium;
        background: #fff;
        width: 20%;
        display: flex;
        justify-content: space-between;
        //span {
           // border:1px solid #337ecc;
        //}
        .num-left {
            width:50%;
            text-align: right;
            margin-right: 10px;
            color: #337ecc;
            font-size: larger;
        }
    }

    .info-mid {
        margin: 5px 5px;
        padding: 5px 5px;
        width: 20%;
        font-size: medium;
        background: #fff;
        display: flex;
        justify-content: space-between;
        //span {
            //border:1px solid #337ecc;
        //}
        .num-mid-1 {
            width:50%;
            text-align: right;
            margin-right: 10px;
            color: green;
            font-size: larger;
        }
        .num-mid-2 {
            width:50%;
            text-align: right;
            margin-right: 10px;
            color: orange;
            font-size: larger;
        }
    }
    .info-right {
        margin: 5px 5px;
        padding: 5px 5px;
        width: 20%;
        font-size: medium;
        background: #fff;
        display: flex;
        justify-content: space-between;
        //span {
        //   border:1px solid #337ecc;
        //}
        .num-right {
            width:50%;
            text-align: right;
            margin-right: 10px;
            color: red;
            font-size: larger;
        }

    }
}

.query-box {
    display: flex;
    margin: 10px;
    //border: 1px solid red;
    //div {
    //    border: 2px solid green;
    //}
    .start-time {
        width: 16%;
    }

    .end-time {
        width: 16%;
        left: 0%;
    }

    .icon-search {
        width: 2%;
        font-size: 30px;
        display: left;
    }

    .button-add {
        width: 7%;
        align-items: center;
    }

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

.demo-pagination-block + .demo-pagination-block {
  margin-top: 10px;
}
.demo-pagination-block .demonstration {
  margin-bottom: 16px;
}


</style>