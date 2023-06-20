<template>
    <div class="login-menu">
      <div class="login-item">
        <span>账号:  </span>
        <input :value="account" @input="onInput1" placeholder="" >
      </div>
      <div class="login-item">
        <span>密码:  </span>
        <input :value="password" @input="onInput2" placeholder="" >
      </div>
      <div class="login-btn">
        <button @click="loginJudge()" class="button1">登录</button>
        <button  @click="reset()" class="button2">取消</button>
      </div>
      <div>
        <el-alert 
        title="登录信息" type="error" 
        show-icon description="用户名或密码错误"
        v-if="isSuccess == false" @close="isSuccess=true"/>
    </div>

    </div>
</template>


<script lang="ts" setup>
 /* eslint-disable */
import { ref, onMounted } from 'vue';
import axios from 'axios';
import router from '@/router';
import { rest } from 'lodash';

const isSuccess = ref(true)
const password = ref('')
const account = ref('')

function loginJudge(){
  const path = 'http://127.0.0.1:5000/auth/login'
  const payload = {
    'username': account.value,
    'password': password.value,
  }
  axios.post(path, payload)
  .then((res)=>{
    const status = res.data.status
    if(status == 'success') {
      
      console.log('SUCCESS')
      router.push('/about')
      return true
    }
    else {
      console.log('fail')
      isSuccess.value = false
      return false
    }
  })
}

function onInput1(e: any) {
  account.value = e.target.value
}

function onInput2(e: any) {
  password.value = e.target.value
}

function reset(){
  account.value = ''
  password.value = ''
}

</script>


<style scoped lang="scss">

.login-menu {
    border-radius: 6px;
    width: 400px;
    height: 200px;
    position: relative;
    padding: 20px;
    margin-top: 4%;
    text-align: center;
    backdrop-filter: blur(6px);
}
.login-item {
    color: rgb(24, 196, 252);
    margin: 15px 20px;
    display: flex;
    input {
        flex: 1;
        border:  3px solid white;
        margin: 0 10px;
    }
}
.login-btn {
  margin-left: 30px;
    .button1 {
      background-color: #18c4fc;
      border: none;
      color: white;
      margin-left: 10px;
      padding: 10px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
  }
  .button2 {
    background-color: #a19ca7;
    border: none;
    margin-left: 10px;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

.button2:hover {
  background-color: #0d001c;
  color: white;
}

}

</style>