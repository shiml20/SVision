<template>
    <div style="padding: 20px">
        <el-row :gutter="0">
            <div style="width:100%">
                <el-col>
                    <el-card shadow="always"> 
                        <div>报警规则</div>
                    </el-card>
                </el-col>
            </div>
        </el-row>


        <el-row :gutter="1">
            <el-table
                ref="multipleTableRef"
                :data="tableData"
                style="width: 100%"
                @selection-change="handleSelectionChange"
            >
                <el-table-column align="center" property="type" label="报警规则类型" width="150" />
                <el-table-column align="center" property="name" label="报警规则名称" width="150" />
                <el-table-column align="center" property="noticedrole" label="通知角色" width="150" />
                <el-table-column align="center" property="way" label="推送方式" width="150" />
                <el-table-column align="center" property="rule" label="报警规则" width="200" />
                <el-table-column align="center" property="paranow" label="当前参数" width="150" />
                <el-table-column align="center" property="parapast" label="原始参数" width="150" />
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
//“新增”对话框
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

interface User {
    type:string,
    name:string,
    noticedrole:string,
    way:string,
    rule:string,
    paranow:string,
    parapas:string
}

const multipleTableRef = ref<InstanceType<typeof ElTable>>()
const multipleSelection = ref<User[]>([])
const toggleSelection = (rows?: User[]) => {
  if (rows) {
    rows.forEach((row) => {
      // TODO: improvement typing when refactor table
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      multipleTableRef.value!.toggleRowSelection(row, false)
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
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
  },
  {
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
  },
  {
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
  },
  {
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
  },
  {
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
  },
  {
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
  },
  {
    type:"火警",
    name:"火灾预警报警提醒",
    noticedrole:"全部",
    way:"页面/短信",
    rule:"火灾传感器报警n分钟以上",
    paranow:"2",
    parapas:"5"
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