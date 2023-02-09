<template>
    <el-row class="title">
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
    <div class="addvehicles">
        <!-- <el-button @click="dialogvisible = true">新增</el-button> -->
        <el-dialog v-model="dialogvisible" title="新增车辆进出记录" width="70%" center>
            <div class="input">
                <el-row :gutter="20">
                    <el-col :span="4"><span class="ml-3 w-35 text-gray-600 inline-flex items-center">车牌号</span></el-col>
                    <el-col :span="20"><el-input v-model="_license" class="w-50 m-2" placeholder="请输入车牌号" /></el-col>
                </el-row>
                <!-- <el-row :gutter="20">
                    <el-col :span="4"><span class="ml-3 w-35 text-gray-600 inline-flex items-center">车型</span></el-col>
                    <el-col :span="20"><el-input v-model="_type" class="w-50 m-2" placeholder="请输入车的种类" /></el-col>
                </el-row> -->
                <el-row :gutter="20">
                    <el-col :span="4"><span class="ml-3 w-35 text-gray-600 inline-flex items-center">车型</span></el-col>
                    <el-col :span="20"><el-input v-model="_type" class="w-50 m-2" placeholder="请输入车的种类" /></el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="4"><span
                            class="ml-3 w-35 text-gray-600 inline-flex items-center">进出类型</span></el-col>
                    <el-col :span="20">
                        <el-select v-model="_whyin" filterable placeholder="请选择" style="width:320px">
                            <el-option v-for="item in options" :key="item.value" :label="item.label"
                                :value="item.value" />
                        </el-select>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="4"><span
                            class="ml-3 w-35 text-gray-600 inline-flex items-center">入园时间</span></el-col>
                    <el-col :span="20">
                        <el-date-picker v-model="_intime" type="datetime" placeholder="请选择入园时间" style="width:320px" />
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="4"><span
                            class="ml-3 w-35 text-gray-600 inline-flex items-center">出园时间</span></el-col>
                    <el-col :span="20">
                        <el-date-picker v-model="_outtime" type="datetime" placeholder="请选择出园时间，若未出园则不写"
                            style="width:320px" />
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="4"><span
                            class="ml-3 w-35 text-gray-600 inline-flex items-center">车主姓名</span></el-col>
                    <el-col :span="20">
                        <el-input v-model="_ownername" class="w-50 m-2" placeholder="请输入车主姓名" />
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="4"><span
                            class="ml-3 w-35 text-gray-600 inline-flex items-center">是否出园</span></el-col>
                    <el-col :span="20">
                        <el-radio-group v-model="_isin">
                            <el-radio :label="true">未出园</el-radio>
                            <el-radio :label="false">已出园</el-radio>
                        </el-radio-group>
                    </el-col>
                </el-row>
                <el-row :gutter="20">
                    <el-col :span="4"><span
                            class="ml-3 w-35 text-gray-600 inline-flex items-center">缴费金额</span></el-col>
                    <el-col :span="20">
                        <el-input-number v-model="_pay"></el-input-number>
                    </el-col>
                </el-row>
            </div>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogvisible = false">取消</el-button>
                    <el-button type="primary" @click="confirmclick">
                        确认
                    </el-button>
                </span>
            </template>
        </el-dialog>
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
            <el-table-column align="right">
                <template #header>
                    <el-button @click="dialogvisible = true">新增</el-button>
                </template>
                <template #default>
                    <el-button link type="primary" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>

</template>
<script>
import { onMounted, ref, defineComponent } from 'vue'
import axios from 'axios'
import { Calendar, Search } from '@element-plus/icons-vue'
export default defineComponent({
    setup() {
        const dialogvisible = ref(false);
        const _license = ref('');
        const _type = ref('');
        const _whyin = ref();
        const _isin = ref(true);
        const _intime = ref();
        const _outtime = ref();
        const _ownername = ref('');
        const _phone = ref('');
        const _pay = ref(0);
        let todayIn = ref(0);
        let todayOut = ref(0);
        let todaymoney = ref(0);
        let todayCar = ref(0);
        const options = [{ value: true, label: '内部车辆' }, { value: false, label: '外来车辆' }];
        const tableData = ref();
        const tableLabel = {
            license: "车牌号",
            type: "种类",
            type: "出入类型",
            intime: "入营时间",
            outtime: "出营时间",
            isin: "当前状态",
            ownername: "车主姓名",
            phone: "联系方式",
            pay: "缴费情况",
        }
        const confirmclick = () => {
            dialogvisible.value = false;
            postData({ _license, _type, _whyin, _isin, _intime, _outtime, _ownername, _phone, _pay });
        }
        // const { _type, _whyin, _isin, _intime, _outtime, _ownername, _phone, _pay } = ref('')
        // 获取数据
        const getData = () => {
            axios({
                method: 'GET',
                url: '/vehicles/',
            }).then((response) => {
                Data.value = response;
            }, error => {
                console.log('错误', error.message)
            })
        }
        //传递数据

        const postData = ({ _license, _type, _whyin, _isin, _intime, _outtime, _ownername, _phone, _pay }) => {
            axios({
                method: 'POST',
                url: '/vehicles/',
                data: {
                    'license': _license,
                    'type': _type,
                    'whyin': _whyin,
                    'isin': _isin,
                    'intime': _intime,
                    'outtime': _outtime,
                    'ownername': _ownername,
                    'phone': _phone,
                    'pay': _pay
                }
            }).then(error => { console.log('错误', error.message) })
        }
        onMounted(() => { getData(); })
        return {
            tableData, dialogvisible, Search, _license, _type, _whyin, _isin, _intime, _outtime, _ownername, _phone, _pay, options, confirmclick, todayIn, todayOut, todaymoney, todayCar,
        }
    }
})
</script>