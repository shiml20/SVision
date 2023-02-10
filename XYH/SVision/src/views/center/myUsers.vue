<template>
    <div>
        <el-row :gutter="0">
        <div style="width:100%">
            <el-col>
                <el-card shadow="always"> 
                    <div>用户管理</div>
                </el-card>
            </el-col>
        </div>
        </el-row>

        <el-row :gutter="0" >
            <div style="width:20%; padding: 10px;">
                    <el-input
                    v-model="input2"
                    class="w-50 m-2"
                    placeholder="用户名/姓名"
                    width="8px"
                    :suffix-icon="Search"
                    />
            </div>
            <div style="width:30%; padding: 10px;">
                <el-select v-model="value" clearable placeholder="所属部门">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    />
                </el-select>
                
                <el-select v-model="value" clearable placeholder="角色名称">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    />
                </el-select>
            </div>
            <div style="width:35%">
            </div>
            <div style="width:10%; padding: 10px;" >
                <el-button type="primary">新增</el-button>
                <el-button type="info">删除</el-button>
            </div>
        </el-row>

        <el-row :gutter="1">
            <el-table
                ref="multipleTableRef"
                :data="tableData"
                style="width: 100%"
                @selection-change="handleSelectionChange"
            >
                <el-table-column align="center"  type="selection" width="50" />
                <el-table-column align="center" property="realname" label="RealName" width="150" />
                <el-table-column align="center" property="username" label="UserName" width="150" />
                <el-table-column align="center" property="type" label="Type" width="150" />
                <el-table-column align="center" property="department" label="Department" width="150" />
                <el-table-column align="center" property="isused" label="IsUsed" width="150" />
                <el-table-column align="center" property="isfaceused" label="IsFaceUsed" width="150" />
                <el-table-column align="center" property="id" label="Id" width="150" />
                <el-table-column align="center" label="Date" width="150">
                <template #default="scope">{{ scope.row.date }}</template>
                </el-table-column>
                <el-table-column align="center">
                    <el-button type="primary" :icon="Edit" circletext @click="dialogFormVisible = true">
                      新增
                    </el-button>
                    <el-dialog v-model="dialogFormVisible" title="Shipping address">
                      <el-form :model="form">
                        <el-form-item label="Promotion name" :label-width="formLabelWidth">
                          <el-input v-model="form.name" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="Zones" :label-width="formLabelWidth">
                          <el-select v-model="form.region" placeholder="Please select a zone">
                            <el-option label="Zone No.1" value="shanghai" />
                            <el-option label="Zone No.2" value="beijing" />
                          </el-select>
                        </el-form-item>
                      </el-form>
                      <template #footer>
                        <span class="dialog-footer">
                          <el-button @click="dialogFormVisible = false">Cancel</el-button>
                          <el-button type="primary" @click="dialogFormVisible = false">
                            Confirm
                          </el-button>
                        </span>
                      </template>
                    </el-dialog>
                    <el-button type="info" :icon="Message" circletext @click="dialogFormVisible = true">
                      查看
                    </el-button>
                    <el-dialog v-model="dialogFormVisible" title="Shipping address">
                      <el-form :model="form">
                        <el-form-item label="Promotion name" :label-width="formLabelWidth">
                          <el-input v-model="form.name" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="Zones" :label-width="formLabelWidth">
                          <el-select v-model="form.region" placeholder="Please select a zone">
                            <el-option label="Zone No.1" value="shanghai" />
                            <el-option label="Zone No.2" value="beijing" />
                          </el-select>
                        </el-form-item>
                      </el-form>
                      <template #footer>
                        <span class="dialog-footer">
                          <el-button @click="dialogFormVisible = false">Cancel</el-button>
                          <el-button type="primary" @click="dialogFormVisible = false">
                            Confirm
                          </el-button>
                        </span>
                      </template>
                    </el-dialog>
                    <el-button type="danger" :icon="Delete" circletext @click="dialogFormVisible = true">
                      删除
                    </el-button>
                    <el-dialog v-model="dialogFormVisible" title="Shipping address">
                      <el-form :model="form">
                        <el-form-item label="Promotion name" :label-width="formLabelWidth">
                          <el-input v-model="form.name" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="Zones" :label-width="formLabelWidth">
                          <el-select v-model="form.region" placeholder="Please select a zone">
                            <el-option label="Zone No.1" value="shanghai" />
                            <el-option label="Zone No.2" value="beijing" />
                          </el-select>
                        </el-form-item>
                      </el-form>
                      <template #footer>
                        <span class="dialog-footer">
                          <el-button @click="dialogFormVisible = false">Cancel</el-button>
                          <el-button type="primary" @click="dialogFormVisible = false">
                            Confirm
                          </el-button>
                        </span>
                      </template>
                    </el-dialog>                                    
                </el-table-column>
            </el-table>
        </el-row>

        <el-row :gutter="1">
        </el-row>

        <el-row :gutter="1">
            <div class="demo-pagination-block">
                <el-pagination
                v-model:current-page="currentPage3"
                v-model:page-size="pageSize3"
                :small="small"
                :disabled="disabled"
                :background="background"
                layout="prev, pager, next, jumper"
                :total="1000"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                />
            </div>
        </el-row>
    </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { Delete, Edit, Search, Message,Share, Upload } from '@element-plus/icons-vue'
import type { ElTable } from 'element-plus'


const value = ref('')
const input2 = ref('')
//新增对话框
const dialogTableVisible = ref(false)
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'

const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

const gridData = [
  {
    date: '2016-05-02',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-04',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-01',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-03',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
]
//所属部门下拉菜单选项
const options = [
  {
    value: 'Option1',
    label: 'Option1',
  },
  {
    value: 'Option2',
    label: 'Option2',
  },
  {
    value: 'Option3',
    label: 'Option3',
  },
  {
    value: 'Option4',
    label: 'Option4',
  },
  {
    value: 'Option5',
    label: 'Option5',
  },
]


interface User {
  realname: string
  username: string
  type: string
  department: string
  isused: boolean
  isfaceused: boolean
  id: string
  date: {}
}

const multipleTableRef = ref<InstanceType<typeof ElTable>>()
const multipleSelection = ref<User[]>([])
const toggleSelection = (rows?: User[]) => {
  if (rows) {
    rows.forEach((row) => {
      // TODO: improvement typing when refactor table
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      return
    })
  } else {
    multipleTableRef.value!.clearSelection()
  }
}
const handleSelectionChange = (val: User[]) => {
  multipleSelection.value = val
}
//表格内容设置
const tableData: User[] = [
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
    date: {}
  },
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
    date: {}
  },
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
   
    date: {}
  },
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
    
    date: {}
  },
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
   
    date: {}
  },
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
   
    date: {}
  },
  {
    realname: "王管理",
    username: "admin",
    type: "超级管理员",
    department: "总部",
    isused: true,
    isfaceused: true,
    id: "100000",
   
    date: {}
  }
]

const currentPage1 = ref(5)
const currentPage2 = ref(5)
const currentPage3 = ref(5)
const currentPage4 = ref(4)
const pageSize2 = ref(100)
const pageSize3 = ref(100)
const pageSize4 = ref(100)
const small = ref(false)
const background = ref(false)
const disabled = ref(false)

const handleSizeChange = (val: number) => {
  console.log(`${val} items per page`)
}
const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
}
</script>
    
<style scoped>
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

</style>