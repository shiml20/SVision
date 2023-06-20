<template>
    <div class="demo-progress">
        <el-progress type="dashboard" :percentage="percentage" :color="colors" >
            <template #default="{ percentage }">
                <span class="percentage-value">{{ percentage }}%</span>
                <span class="percentage-label">{{props.msg}}</span>
            </template>
        </el-progress>
        <div style="margin-left:5%" v-if="props.button">
            <el-button-group>
                <el-button :icon="Minus" @click="decrease" />
                <el-button :icon="Plus" @click="increase" />
            </el-button-group>
        </div>
    </div>
</template>

<script lang="ts" setup>
/* eslint-disable */
import { onMounted, ref } from 'vue'
import { Minus, Plus } from '@element-plus/icons-vue'


const props = defineProps({
    percentage: {
        type: Number,
        default: 0
    },
    type: {
        type: String,
        default: ""
    },
    msg: {
        type: String,
        default: "Progressing"
    },
    button: {
        type: Boolean,
        default: true,
    }
})

const percentage = ref(props.percentage)

const colors = [
    { color: '#f56c6c', percentage: 20 },
    { color: '#e6a23c', percentage: 40 },
    { color: '#5cb87a', percentage: 60 },
    { color: '#1989fa', percentage: 80 },
    { color: '#6f7ad3', percentage: 100 },
]

const increase = () => {
    percentage.value += 1
    if (percentage.value > 100) {
        percentage.value = 100
    }
}
const decrease = () => {
    percentage.value -= 1
    if (percentage.value < 0) {
        percentage.value = 0
    }
}


</script>


<style scoped>

.demo-progress .el-progress--line {
    margin-bottom: 15px;
    width: 350px;
}

.demo-progress .el-progress--circle {
    margin-right: 15px;
}

.percentage-value {
    display: block;
    margin-top: 10px;
    font-size: 28px;
    color: white;
  }
  .percentage-label {
    display: block;
    margin-top: 10px;
    font-size: 12px;
    color: white;
  }
  .demo-progress .el-progress--line {
    margin-bottom: 15px;
    width: 350px;
  }
  .demo-progress .el-progress--circle {
    margin-right: 15px;
  }
</style>
