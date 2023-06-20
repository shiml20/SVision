<template>
  <div class="warehouses">

    <BasicHeader :title="title"></BasicHeader>
    <div class="w-main">
      <div class="left">
        <!-- 多维柱状图 -->
        <div class="trend" :class="{ fullscreen: isTrend }">
          <BasicPlot :option="option_2bar" ref="trend"></BasicPlot>
          <el-icon v-if="isTrend" class="icon" @click="isTrend = false">
            <ZoomOut />
          </el-icon>
          <el-icon v-else class="icon" @click="isTrend = true">
            <FullScreen />
          </el-icon>
        </div>
        <!-- 环形图 -->
        <div class="seller">
          <BasicPlot :option="option_ring"></BasicPlot>
        </div>
      </div>

      <div class="center">
        <!-- 三维雷达图 -->
        <div class="map">
          <BasicPlot :option="option_radar"></BasicPlot>
        </div>
        <!-- 中国地图 -->
        <div class="rank">
          <ChinaMap></ChinaMap>
        </div>
      </div>
      <div class="right">
        <!-- 柱状图 -->
        <div class="hot">
          <BasicPlot :option="option_bar"></BasicPlot>
        </div>
        <!-- 多维柱状图 -->
        <div class="stock">
          <BasicPlot :option="option_bar2"></BasicPlot>
        </div>
      </div>
    </div>
  </div>

</template>

<script lang="ts" setup>
/* eslint-disable */
import * as echarts from "echarts"
import { now } from 'lodash';
import { watch, ref, onMounted, nextTick } from 'vue';
import ChinaMap from "@/components/ChinaMap.vue";
import BasicPlot from "@/components/BasicPlot.vue";
import BasicHeader from "@/components/BasicHeader.vue";

const title = "综保区仓储状况"
const nowTime = ref<any>()

// 定义组件应用
let trend = ref<any>(null)
// 是否全屏显示
let isTrend = ref(false)

// 监视全屏变化
watch(isTrend, (nval) => {
  console.log(trend.value)
  nextTick(() => {
    trend.value.resize()
  })
})

onMounted(() => {
  getDate()
})


function getDate() {
  window.setTimeout(function () {
    window.requestAnimationFrame(getDate)
  }, 1000 / 2)
  var d = new Date();
  var year = d.getFullYear()  //获取年
  var month: any = d.getMonth() + 1;  //获取月，从 Date 对象返回月份 (0 ~ 11)，故在此处+1
  var day: any = d.getDay()    //获取日
  var days: any = d.getDate() //获取日期
  var hour: any = d.getHours()   //获取小时
  var minute: any = d.getMinutes()  //获取分钟
  var second: any = d.getSeconds()   //获取秒

  if (month < 10) month = "0" + month
  if (days < 10) days = "0" + days
  if (hour < 10) hour = "0" + hour
  if (minute < 10) minute = "0" + minute
  if (second < 10) second = "0" + second

  var week = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
  var Tools = document.getElementById("Main")
  var da = year + " 年 " + month + " 月 " + days + " 日 " + week[day] + " " + hour + " : " + minute + " :" + second
  nowTime.value = da
  // console.log(da)
}

//表格01仓储容量的数据
const temp = [
    {
        number: 1,
        capicity: 100,
        used: 40,
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
        used: 10,
    },
    {
        number: 6,
        capicity: 100,
        used: 100,
    },
]

var option_bar = {
  backgroundColor: '#272822',
    title: {
        text: '仓储情况',
        textStyle: {
           color: '#fff'
      }
    },
    tooltip: {},
    legend: {
        data: ['仓储数量'],
        left: '50%',
        top: '2%',
        textStyle: {
           color: '#fff'
      }
    },
    xAxis: {
        data: ['1仓', '2仓', '3仓', '4仓', '5仓', '6仓']
    },
    yAxis: {
        // data: [10, 20, 30, 40, 50, 60]
    },
    series: [
        {
            name: '仓储数量',
            type: 'bar',
            data: [temp[0]['used'], temp[1]['used'],temp[2]['used'],temp[3]['used'],temp[4]['used'],temp[5]['used']],
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                { offset: 0, color: '#62f0ff' },
                { offset: 0.5, color: '#30c2ff' },
                { offset: 1, color: '#0197ff' }
              ])
          }
        }
    ],
    color: '#ffffff'
};
// Schema:
// date,AQIindex,PM2.5,PM10,CO,NO2,SO2
const dataProcess = [
  [55, 90, 56, 46, 38, 60]
];
const dataDeliver = [
  [26, 37, 27, 63, 27, 13, 81],
];
const dataCommerce = [
  [91, 45, 25, 82, 34, 23, 10]
];
const lineStyle = {
  width: 1,
  opacity: 0.5
};

var option_radar = {
  backgroundColor: '#272822',
  title: {
    text: '仓库安防等级',
    left: 'center',
    textStyle: {
      color: '#eee'
    }
  },
  legend: {
    bottom: 5,
    data: ['出口加工区', '物流中转区', '商业贸易区'],
    itemGap: 20,
    textStyle: {
      color: '#fff',
      fontSize: 14
    },
    selectedMode: 'single'
  },
  radar: {
    indicator: [
      { name: '原材料仓', max: 100 },
      { name: '半成品仓', max: 100 },
      { name: '成品仓', max: 100 },
      { name: '设备仓', max: 100 },
      { name: '物流中转仓', max: 100 },
    ],
    shape: 'circle',
    splitNumber: 5,
    axisName: {
      color: '#ffffff'
    },
    splitLine: {
      lineStyle: {
        color: [
          'rgba(0, 157, 255, 0.2)',
          'rgba(0, 157, 255, 0.4)',
          'rgba(0, 157, 255, 0.6)',
          'rgba(0, 157, 255, 0.8)',
          'rgba(0, 157, 255, 1)',
          'rgba(0, 157, 255, 1.2)'
        ].reverse()
      }
    },
    splitArea: {
      show: false
    },
    axisLine: {
      lineStyle: {
        color: 'rgba(255, 255, 255, 5)'
      }
    }
  },
  series: [
    {
      name: '出口加工区',
      type: 'radar',
      lineStyle: lineStyle,
      data: dataProcess,
      symbol: 'none',
      itemStyle: {
        color: '#009dff'
      },
      areaStyle: {
        opacity: 0.3
      }
    },
    {
      name: '物流中转区',
      type: 'radar',
      lineStyle: lineStyle,
      data: dataDeliver,
      symbol: 'none',
      itemStyle: {
        color: '#22e4ff'
      },
      areaStyle: {
        opacity: 0.3
      }
    },
    {
      name: '商业贸易区',
      type: 'radar',
      lineStyle: lineStyle,
      data: dataCommerce,
      symbol: 'none',
      itemStyle: {
        color: '#3bffd0'
      },
      areaStyle: {
        opacity: 0.3
      }
    }
  ]
};

var option_ring = {
  backgroundColor: '#272822',
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '5%',
      left: 'center',
      textStyle: {
           color: '#fff'
      }
    },
    series: [
      {
        name: '已启用仓库数量',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#3bffd0',
          borderWidth: 2,

        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [
          { value: 1048, name: '原材料仓' },
          { value: 735, name: '半成品仓库' },
          { value: 580, name: '成品仓' },
          { value: 484, name: '设备仓' },
          { value: 300, name: '物流中转仓' }
        ],
        
      }
    ]
  };
  
var option_2bar2 = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    data: ['Profit', 'Expenses', 'Income']
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: [
    {
      type: 'value'
    }
  ],
  yAxis: [
    {
      type: 'category',
      axisTick: {
        show: false
      },
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    }
  ],
  series: [
    {
      name: 'Profit',
      type: 'bar',
      label: {
        show: true,
        position: 'inside'
      },
      emphasis: {
        focus: 'series'
      },
      data: [200, 170, 240, 244, 200, 220, 210]
    },
    {
      name: 'Income',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: [320, 302, 341, 374, 390, 450, 420]
    },
    {
      name: 'Expenses',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true,
        position: 'left'
      },
      emphasis: {
        focus: 'series'
      },
      data: [-120, -132, -101, -134, -190, -230, -210]
    }
  ]
};

var option_2bar = {
  backgroundColor: '#272822',
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    },
    textStyle: {
           color: '#000000'
      }
  },
  legend: {
    data: ['货物净增量/单位', '出口量/单位', '进口量/单位'],
    textStyle: {
           color: '#fff'
      }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: [
    {
      type: 'value'
    }
  ],
  yAxis: [
    {
      type: 'category',
      axisTick: {
        show: false
      },
      data: ['星期一2.13', '星期二2.14', '星期三2.15', '星期四2.16', '星期五2.17', '星期六2.18', '星期天2.19']
    }
  ],
  series: [
    {
      name: '货物净增量/单位',
      type: 'bar',
      label: {
        show: true,
        position: 'inside',
        textStyle: {
           color: '#000000'
      }
      },
      emphasis: {
        focus: 'series',
        textStyle: {
           color: '#000000'
      }
      },
      data: [200, 170, 240, 244, 200, 220, 210],
      itemStyle: {
          borderRadius: 10,
          color: '#009dff'
        },
    },
    {
      name: '进口量/单位',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true
      },
      emphasis: {
        focus: 'series'
      },
      data: [320, 302, 341, 374, 390, 450, 420],
      itemStyle: {
          borderRadius: 10,
          color: '#04e38a'
        },
    },
    {
      name: '出口量/单位',
      type: 'bar',
      stack: 'Total',
      label: {
        show: true,
        position: 'left'
      },
      emphasis: {
        focus: 'series'
      },
      data: [-120, -132, -101, -134, -190, -230, -210],
      itemStyle: {
          borderRadius: 10,
          // borderColor: '#fff',
          // borderWidth: 2,
          color: '#3bffd0'
        },
    }
  ]
};

var option_bar2 = {
    backgroundColor: '#272822',
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ['总数','已巡检数量','待巡检数量',],
      textStyle: {
           color: '#eee'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: [
      {
        type: 'value'
      }
    ],
    yAxis: [
      {
        type: 'category',
        axisTick: {
          show: false
        },
        data: ['消防设施', '监控设施', '配套设备','环境指标', '总量清算', '安防等级确认', '损坏情况排查', '潜在危险排查']
      }
    ],
    series: [
      {
        name: '总数',
        type: 'bar',
        stack: 'Total',
        label: {
          show: true
        },
        emphasis: {
          focus: 'series'
        },
        data: [320, 302, 341, 374, 390, 450, 420],
        itemStyle: {
          borderRadius: 10,
          color: '#fee588'
        },
      },
      {
        name: '已巡检数量',
        type: 'bar',
        stack: 'Total',
        label: {
          show: true,
          position: 'left'
        },
        emphasis: {
          focus: 'series'
        },
        data: [-120, -132, -101, -134, -190, -230, -210],
        itemStyle: {
          borderRadius: 10,
          color: '#9dff86'
        },
      },
      {
        name: '待巡检数量',
        type: 'bar',
        label: {
          show: true,
          position: 'inside'
        },
        emphasis: {
          focus: 'series'
        },
        data: [200, 170, 240, 244, 200, 220, 210],
        itemStyle: {
          borderRadius: 10,
          color: '#0197ff'
        },
      }
    ]
  };

</script>

<style scoped lang="scss">
.warehouses {
  width: 100vw;
  height: 100vh;
  background-color: black;
  color: white;
  padding: 0 20px 20px 20px;
  display: flex;
  flex-direction: column;
}

.w-main {
  flex: 1;
  display: flex;
  justify-content: space-between;
  margin-top: 10px;

  div {
    border-radius: 10px;
  }

  .left {
    width: 27%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .trend {
      height: 58%;
      position: relative;

      .icon {
        position: absolute;
        top: 10px;
        right: 10px;
      }
    }

    .seller {
      height: 38%;
    }
  }

  .center {
    width: 43%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    .map {
      height: 64%;
    }

    .rank {
      height: 33%;
    }
  }

  .right {
    width: 27%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .hot {
      height: 58%;
    }

    .stock {
      height: 38%;
    }
  }
}

.fullscreen { 
  width: 100vw !important;
  height: 100vh !important;
  position: absolute !important;
  z-index: 1000;
  left: 0 !important;
  top: 0 !important;
}
</style>
