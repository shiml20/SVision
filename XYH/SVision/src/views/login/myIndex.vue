<template>
  <div>
    <el-dialog v-model="dialogFormVisible" title="用户登陆界面">
      <el-form >
        <el-form-item label="账号" :label-width="formLabelWidth" size="large">
          <el-input v-model="user.username" autocomplete="off" size="large" clearable/>
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth" size="large" clearble>
          <el-input v-model="user.password" type="password" autocomplete="off" size="large"/>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="login">
            登陆
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import axios from 'axios'

import { useRouter } from 'vue-router'
const router = useRouter()

const dialogFormVisible = ref(true)
const formLabelWidth = '140px'

// 存储用户登陆信息
const user = reactive({
  username: '',
  password: ''
})


const login = () => {
  const url = 'http://192.168.2.23:10393/mock/4db07eef-66e8-439a-aa9a-6002e8ef972f/login';
    axios.get(url, {
      params: {
        username: user.username,
        password: user.password
      }
    })
    .then(response => {
      console.log(response);
      console.log("登陆成功！！！");
      dialogFormVisible.value = false;  // 关闭登陆窗口
      // 跳转到系统主页 Index.vue -> 路由 /index
      router.push("/index");
    })
    .catch(() => {
      // alert("登陆失败！！！");
      dialogFormVisible.value = false;  // 关闭登陆窗口
      // 跳转到系统主页 Index.vue -> 路由 /index
      router.push("/index");
    });
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
