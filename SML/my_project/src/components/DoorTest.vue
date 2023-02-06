<template>
  <el-row :gutter="20">
      <el-page-header @back="goBack">
          <template #content>
              <span class="text-large font-600 mr-3"> 车辆进出记录 </span>
          </template>
      </el-page-header>  
  </el-row>

  <el-row :gutter="100">
      <el-date-picker v-model="datevalue" type="date" placeholder="选择日期">

      </el-date-picker>
      <div class="demo-time-range">
          <el-time-select v-model="startTime" :max-time="endTime" class="mr-4" placeholder="Start time" start="08:30"
              step="00:15" end="18:30" />
          <el-time-select v-model="endTime" :min-time="startTime" placeholder="End time" start="08:30" step="00:15"
              end="18:30" />
      </div> 
  </el-row>
  <el-row :gutter="20">
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

  <div>
      <el-button type="primary" round @click="dialogFormVisible = true;">
          添加资源
      </el-button>
      <!-- Form -->
  </div>

  <br>
  <div id="big">
      <el-table :data="resources" border style="width: 100%">
          <el-table-column prop="date" label="Date" width="180" align="center" />
          <el-table-column prop="name" label="Name" align="center" />
          <el-table-column prop="address" label="Address" align="center" />
          <el-table-column fixed="right" label="Operations" align="center">
              <template #default="scope">
                  <el-button size="small" @click="dialogUpdateVisible = true">Edit</el-button>
                  <el-button size="small" type="danger"
                      @click="tobeDeleted = scope.row.date; dialogDeleteVisible = true">Delete</el-button>
              </template>
          </el-table-column>
      </el-table>
  </div>

  <div>
      <el-dialog v-model="dialogFormVisible" title="Add Dialog">
          <el-form :model="addResForm">
              <el-form-item label="Date" :label-width="formLabelWidth">
                  <el-input v-model="addResForm.date" autocomplete="off" placeholder="输入日期" />
              </el-form-item>
              <el-form-item label="Name" :label-width="formLabelWidth">
                  <el-input v-model="addResForm.name" autocomplete="off" placeholder="输入姓名" />
              </el-form-item>
              <el-form-item label="Address" :label-width="formLabelWidth">
                  <el-input v-model="addResForm.address" autocomplete="off" placeholder="是否学习" />
              </el-form-item>
          </el-form>
          <template #footer>
              <span class="dialog-footer">
                  <el-button @click="dialogFormVisible = false">Cancel</el-button>
                  <el-button @click="onReset">Reset</el-button>
                  <el-button type="primary" @click="dialogFormVisible = false; onSubmit(); showMessage = true">
                      Confirm
                  </el-button>
              </span>
          </template>
      </el-dialog>
  </div>

  <div>
      <el-dialog v-model="dialogUpdateVisible" title="Update dialog">
          <el-form :model="editResForm">
              <el-form-item label="Date" :label-width="formLabelWidth">
                  <el-input v-model="editResForm.date" autocomplete="off" placeholder="更新日期" />
              </el-form-item>
              <el-form-item label="Name" :label-width="formLabelWidth">
                  <el-input v-model="editResForm.name" autocomplete="off" placeholder="更新姓名" />
              </el-form-item>
              <el-form-item label="Address" :label-width="formLabelWidth">
                  <el-input v-model="editResForm.address" autocomplete="off" placeholder="是否学习" />
              </el-form-item>
          </el-form>
          <template #footer>
              <span class="dialog-footer">
                  <el-button @click="dialogUpdateVisible = false">Cancel</el-button>
                  <el-button @click="onReset">Reset</el-button>
                  <el-button type="primary"
                      @click="dialogUpdateVisible = false; onSubmitUpdate(); showMessage = true">
                      Confirm
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
  </el-row>
</template>



<script lang="ts" setup>
/* eslint-disable */
import { reactive, ref } from 'vue'
import axios from 'axios'

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


const dialogFormVisible = ref(false)
const dialogUpdateVisible = ref(false)
const dialogDeleteVisible = ref(false)
const formLabelWidth = '140px'
const showMessage = ref(false)
const alertMessage = ref('')
let tobeDeleted = ref('')

const addResForm = reactive({
    date: '',
    name: '',
    address: false,
})

const editResForm = reactive({
    date: '',
    name: '',
    address: false,
})

function initForm() {
    addResForm.date = '';
    addResForm.name = '';
    addResForm.address = false;
    editResForm.date = '';
    editResForm.name = '';
    editResForm.address = false;
}


const path = 'http://localhost:5000/resources'
const resources = ref<any>([])


function addRes(payload: {}) {
    axios.post(path, payload)
        .then((res) => {
            resources.value = [] // 如果不加这句的话就会重复渲染！！！！！！ 202301290226
            console.log(resources)
            getResources()
            alertMessage.value = res.data.message
            var success = res.data.status
            console.log(success)
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
            getResources()
        })
}

function getResources() {
    axios.get(path)
        .then((res) => {
            console.log(res.data)
            res.data.resources.forEach((element: {}) => {
                resources.value.push(element)
            })
        })
        .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
        })
}

function onSubmit() {
    // evt.preventDefault();
    let address = false;
    if (addResForm.address) address = true;
    console.log(address)
    const payload = {
        date: addResForm.date,
        name: addResForm.name,
        address,
    };
    console.log(payload)

    addRes(payload)
    initForm()
}

function onSubmitUpdate() {
    // evt.preventDefault();
    let address = false;
    if (editResForm.address) address = true;
    console.log(address)
    const payload = {
        date: editResForm.date,
        name: editResForm.name,
        address,
    };
    console.log(payload)
    updateRes(payload, editResForm.date)
    initForm()
}

function updateRes(payload: {}, date: string) {
    const _path = `http://localhost:5000/resources/${date}`
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


function removeRes(date: string) {
    console.log(date)
    const _path = `http://localhost:5000/resources/${date}`;
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

<style>
.el-row {
  margin-bottom: 20px;
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
</style>
