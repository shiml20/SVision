<template>
    <div class='b-container' ref="basicplot">
    </div>

</template>

<script lang='ts' setup>
/* eslint-disable */
import { ref, onMounted, defineExpose } from 'vue';
import * as echarts from 'echarts'

const props = defineProps({
    option: {
        type: Object,
        default() {
            var option2 = {
                        backgroundColor: '#161522',
                        xAxis: {
                            type: 'category',
                            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                        },
                        yAxis: {
                            type: 'value'
                        },
                        series: [
                            {
                            data: [150, 230, 224, 218, 135, 147, 300],
                            type: 'line'
                            }
                        ],
                        color: '#fff',
                        };
            return option2
        }
    }
})

let basicplot = ref<any>('')
let myChart: any = null
// 标题大小（用于控制自适应）

var option = props.option
onMounted(() => {
    myChart = echarts.init(basicplot.value)
    myChart.setOption(option)
    // 注册窗口大小调整大小事件
    window.addEventListener('resize', () => {
        resize()
    })
})

// 统一的自适应方法
let resize = () => {
    // 调整图表大小
    myChart.resize()
    // 调整图表中的自适应部分
    adaptionChart()
}

function adaptionChart() {
}






// 暴给父组件使用的成员
defineExpose({
    resize
})
</script>



<style scoped lang="scss">
.b-container {
    width: 100%;
    height: 100%;
    position: relative;
    align-items: center;
}
</style>