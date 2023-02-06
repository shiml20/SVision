<template>

    <h1 class="h1-text"><img src="/assets/logo.png" alt="学习资源" style="zoom:25%" > SVison - Smart Security System</h1>
    <router-link to="/resources">aaa</router-link>
    
   

</template>

<script setup>
/* eslint-disable */
import { reactive, ref } from 'vue'
import axios from 'axios'

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
editResForm.address =false;
}


const path = 'http://localhost:5000/resources'
const resources = ref([])


function addRes(payload) {
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
    res.data.resources.forEach(element => {
      resources.value.push(element)
    })
  })
  .catch((error) => {
    // eslint-disable-next-line
    console.error(error)
  })
}

function onSubmit(evt) {
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

function onSubmitUpdate(evt) {
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

function updateRes(payload, date) {
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


function removeRes(date) {
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

function onReset(evt) {
// evt.preventDefault();
initForm()
}

getResources()

</script>

<style scoped>
.h1-text {
  color: #337ecc;
  margin: auto;
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
  width: 80%;
  margin: auto;
}
</style>