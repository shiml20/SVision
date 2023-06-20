<template>
    <div class='b-container' ref="warepie">
    </div>
 
</template>

<script lang='ts' setup>
/* eslint-disable */
import { ref,onMounted, defineExpose } from 'vue';
import * as echarts from 'echarts'

const props = defineProps({
    foo: {
    type: Number,
    default: 100
  },
  backgroundColor: {
    type: String,
    default: '#161522'
  },
  barColor: {
    type: String,
    default: '#5470c6'
  }
})

let warepie = ref<any>('')
let myChart:any = null
// 标题大小（用于控制自适应）
let titleSize = ref('50px')


onMounted(() => {
    myChart = echarts.init(warepie.value)
    myChart.setOption(option)
    // 注册窗口大小调整大小事件
    window.addEventListener('resize', ()=>{
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

function adaptionChart(){
}


const temp = [
    {
        number: 1,
        capicity: 100,
        used: props.foo,
    },
    {
        number: 2,
        capicity: 100,
        used: 40,
    },
    {
        number: 3,
        capicity: 100,
        used: 60,
    },
    {
        number: 4,
        capicity: 100,
        used: 80,
    },
    {
        number: 5,
        capicity: 100,
        used: 0,
    },
    {
        number: 6,
        capicity: 100,
        used: 100,
    },
]

var option = {
  color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
  title: {
    text: 'Customized Radar Chart',
  },
  legend: {},
  radar: [
    {
      indicator: [
        { text: 'Indicator1' },
        { text: 'Indicator2' },
        { text: 'Indicator3' },
        { text: 'Indicator4' },
        { text: 'Indicator5' }
      ],
      center: ['50%', '50%'],
      radius: 60,
      startAngle: 90,
      splitNumber: 4,
      shape: 'circle',
      axisName: {
        formatter: '【{value}】',
        color: '#428BD4'
      },
      splitArea: {
        areaStyle: {
          color: ['#77EADF', '#26C3BE', '#64AFE9', '#428BD4'],
          shadowColor: 'rgba(0, 0, 0, 0.2)',
          shadowBlur: 10
        }
      },
      axisLine: {
        lineStyle: {
          color: 'rgba(211, 253, 250, 0.8)'
        }
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(211, 253, 250, 0.8)'
        }
      }
    },
    
  ],
  series: [
    {
      type: 'radar',
      emphasis: {
        lineStyle: {
          width: 4
        }
      },
      data: [
        {
          value: [100, 8, 0.4, -80, 2000],
          name: 'Data A'
        },
        {
          value: [60, 5, 0.3, -100, 1500],
          name: 'Data B',
          areaStyle: {
            color: 'rgba(255, 228, 52, 0.6)'
          }
        }
      ]
    },
  ]
};


// 暴给父组件使用的成员
defineExpose({
  resize
})
</script>



<style scoped lang="scss">

.b-container {
    position: relative;
}

</style>