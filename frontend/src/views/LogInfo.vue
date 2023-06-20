<template>
    <div class="b-container">
        <div class="log-info-main">
              <!-- 数据信息栏 -->
              <div class="log-info">
                <div class="info-left">
                    <span>当日登记人数</span>
                    <span class="num-left">179人</span>
                </div>
                <div class="info-mid">
                    <span>当日值班人数</span>
                    <span class="num-mid-1">8人</span>
                </div>
                <div class="info-mid">
                    <span>重点关注人员</span>
                    <span class="num-mid-2">3人</span>
                </div>
                <div class="info-right">
                    <span>今日职工登记情况</span>
                    <span class="num-right">已登记</span>
                </div>
            </div>
            <div class="mid">
              <WorkRule></WorkRule>
            </div>
            <div class="bottom">

              <div class="log-form">
                <el-form
                ref="ruleFormRef"
                :model="ruleForm"
                :rules="rules"
                label-width="120px"
                class="demo-ruleForm"
                :size="formSize"
                status-icon
              >
                <el-form-item label="工作人员姓名" prop="name">
                  <el-input v-model="ruleForm.name" placeholder="请输入您的姓名"/>
                </el-form-item>
                <el-form-item label="工作部门" prop="region">
                  <el-select v-model="ruleForm.region" placeholder="请输入您的部门">
                    <el-option label="部门1" value="shanghai" />
                    <el-option label="部门2" value="beijing" />
                    <el-option label="部门1" value="shanghai" />
                    <el-option label="部门2" value="beijing" />
                  </el-select>
                </el-form-item>
                <!-- <el-form-item label="Activity count" prop="count">
                  <el-select-v2
                    v-model="ruleForm.count"
                    placeholder="Activity count"
                    :options="options"
                  />
                </el-form-item> -->
                <el-form-item label="工作记录时间" required>
                  <el-col :span="11">
                    <el-form-item prop="date1">
                      <el-date-picker
                        v-model="ruleForm.date1"
                        type="date"
                        label="Pick a date"
                        placeholder="Pick a date"
                        style="width: 100%"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col class="text-center" :span="2">
                    <span class="text-gray-500">-</span>
                  </el-col>
                  <el-col :span="11">
                    <el-form-item prop="date2">
                      <el-time-picker
                        v-model="ruleForm.date2"
                        label="Pick a time"
                        placeholder="Pick a time"
                        style="width: 100%"
                      />
                    </el-form-item>
                  </el-col>
                </el-form-item>
                <!-- <el-form-item label="Instant delivery" prop="delivery">
                  <el-switch v-model="ruleForm.delivery" />
                </el-form-item> -->
                <el-form-item label="日志类型" prop="type">
                  <el-checkbox-group v-model="ruleForm.type">
                    <el-checkbox label="日常工作日志" name="type" />
                    <el-checkbox label="拜访活动日志" name="type" />
                    <el-checkbox label="会议活动日志" name="type" />
                  </el-checkbox-group>
                </el-form-item>
                <el-form-item label="标记重要日志" prop="resource">
                  <el-radio-group v-model="ruleForm.resource">
                    <el-radio label="非重要日志" />
                    <el-radio label="重要日志" />
                  </el-radio-group>
                </el-form-item>
                <el-form-item label="日志内容" prop="desc">
                  <el-input v-model="ruleForm.desc" type="textarea" />
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="submitForm(ruleFormRef)">
                    创建
                  </el-button>
                  <el-button @click="resetForm(ruleFormRef)">重置</el-button>
                </el-form-item>
              </el-form>
            </div>
            </div>   
        </div>
    </div>
    
</template>


<script lang="ts" setup>
/* eslint-disable */ 
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import BasicHeader from'@/components/BasicHeader.vue'
import ACard from '@/components/ACard.vue';
import WorkRule from '@/components/WorkRule.vue';

const title = '工作日志'

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  name: '',
  region: '',
  count: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})
const rules = reactive<FormRules>({
  name: [
    { required: true, message: 'Please input Activity name', trigger: 'blur' },
    { min: 3, max: 5, message: 'Length should be 3 to 5', trigger: 'blur' },
  ],
  region: [
    {
      required: true,
      message: 'Please select Activity zone',
      trigger: 'change',
    },
  ],
  count: [
    {
      required: true,
      message: 'Please select Activity count',
      trigger: 'change',
    },
  ],
  date1: [
    {
      type: 'date',
      required: true,
      message: 'Please pick a date',
      trigger: 'change',
    },
  ],
  date2: [
    {
      type: 'date',
      required: true,
      message: 'Please pick a time',
      trigger: 'change',
    },
  ],
  type: [
    {
      type: 'array',
      required: true,
      message: 'Please select at least one activity type',
      trigger: 'change',
    },
  ],
  resource: [
    {
      required: true,
      message: 'Please select activity resource',
      trigger: 'change',
    },
  ],
  desc: [
    { required: true, message: 'Please input activity form', trigger: 'blur' },
  ],
})
const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!', fields)
    }
  })
}
const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}
const options = Array.from({ length: 10000 }).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `${idx + 1}`,
}))
</script>

<style scoped lang="scss">

.b-container {
    background: #ffffff;
}


.log-info-header {
    height: 5%;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    color: white;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    .weather-report{
        font-size: 50px;
        color: white;
    }
}

.log-info-main {
    height: 90%;
    width: 100%;
    //border: 1px solid red;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    div{
        margin-left: 2px;
        //border: 1px solid green;
    }
    .log-info {
      height:5%;
    }
    .mid {
      height: 55%;
    }
    .bottom {
      height: 45%;
      display: flex;
      flex-direction: row;
      div {
        flex:1;
      }
    }
}

.log-info {
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
      //   border:1px solid #337ecc;
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
      //    border:1px solid #337ecc;
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
      //    border:1px solid #337ecc;
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


</style>


