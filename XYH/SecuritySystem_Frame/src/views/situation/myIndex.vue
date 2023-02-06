<template>
	<div>
    <div class="setbg">
      <el-row :gutter="0">
        <el-col :span="7">
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <span>营区基本情况</span>
                <span> | information</span>
              </div>
            </template>
            <div id="main1" style="width: 100%; height: 300px"></div>
          </el-card>
        </el-col>
        
        <!-- 中间部分 空着 -->
        <el-col :span="10">
          
        </el-col>
          
        <el-col :span="7">
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <span>营区基本情况</span>
                <span> | information</span>
              </div>
            </template>
            <div id="main2" style="width: 100%; height: 300px"></div>
            </el-card>
        </el-col>
      </el-row>
    
      <el-row :gutter="0">
        <el-col :span="7">
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <span>营区基本情况</span>
                <span> | information</span>
              </div>
            </template>
            <div id="main3" style="width: 100%; height: 300px"></div>
            </el-card>
        </el-col>
        
        <el-col :span="10">
          
        </el-col>
          
        <el-col :span="7">
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <span>营区基本情况</span>
                <span> | information</span>
              </div>
            </template>
            <div id="main4" style="width: 100%; height: 300px"></div>
            </el-card>
        </el-col>
      </el-row>
    </div>
	</div>
	
</template>

<script setup>
import { onMounted } from "vue";
//  按需引入 echarts
import * as echarts from "echarts";

onMounted(() => {
	initChart();
})

var option = {
    title: {
      text: 'ECharts 入门示例'
    },
    tooltip: {},
    legend: {
      data: ['销量']
    },
    xAxis: {
      data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [
      {
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
      }
    ]
  };

var option1 = {
  backgroundColor: '#2c343c',
  title: {
    text: 'Customized Pie',
    left: 'center',
    top: 20,
    textStyle: {
      color: '#ccc'
    }
  },
  tooltip: {
    trigger: 'item'
  },
  visualMap: {
    show: false,
    min: 80,
    max: 600,
    inRange: {
      colorLightness: [0, 1]
    }
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '55%',
      center: ['50%', '50%'],
      data: [
        { value: 335, name: 'Direct' },
        { value: 310, name: 'Email' },
        { value: 274, name: 'Union Ads' },
        { value: 235, name: 'Video Ads' },
        { value: 400, name: 'Search Engine' }
      ].sort(function (a, b) {
        return a.value - b.value;
      }),
      roseType: 'radius',
      label: {
        color: 'rgba(255, 255, 255, 0.3)'
      },
      labelLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        },
        smooth: 0.2,
        length: 10,
        length2: 20
      },
      itemStyle: {
        color: '#c23531',
        shadowBlur: 200,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
      },
      animationType: 'scale',
      animationEasing: 'elasticOut',
      animationDelay: function () {
        return Math.random() * 200;
      }
    }
  ]
};

var option2 = {
  color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
  title: {
    text: 'Customized Radar Chart'
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
      center: ['25%', '50%'],
      radius: 120,
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
    {
      indicator: [
        { text: 'Indicator1', max: 150 },
        { text: 'Indicator2', max: 150 },
        { text: 'Indicator3', max: 150 },
        { text: 'Indicator4', max: 120 },
        { text: 'Indicator5', max: 108 },
        { text: 'Indicator6', max: 72 }
      ],
      center: ['75%', '50%'],
      radius: 120,
      axisName: {
        color: '#fff',
        backgroundColor: '#666',
        borderRadius: 3,
        padding: [3, 5]
      }
    }
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
    {
      type: 'radar',
      radarIndex: 1,
      data: [
        {
          value: [120, 118, 130, 100, 99, 70],
          name: 'Data C',
          symbol: 'rect',
          symbolSize: 12,
          lineStyle: {
            type: 'dashed'
          },
          label: {
            show: true,
            formatter: function (params) {
              return params.value;
            }
          }
        },
        {
          value: [100, 93, 50, 90, 70, 60],
          name: 'Data D',
          areaStyle: {
            color: new echarts.graphic.RadialGradient(0.1, 0.6, 1, [
              {
                color: 'rgba(255, 145, 124, 0.1)',
                offset: 0
              },
              {
                color: 'rgba(255, 145, 124, 0.9)',
                offset: 1
              }
            ])
          }
        }
      ]
    }
  ]
};
  function initChart() {
	// 基于准备好的dom，初始化echarts实例
	var myChart1 = echarts.init(document.getElementById('main1'));
	var myChart2 = echarts.init(document.getElementById('main2'));
	var myChart3 = echarts.init(document.getElementById('main3'));
	var myChart4 = echarts.init(document.getElementById('main4'));
	// 使用刚指定的配置项和数据显示图表。
	myChart1.setOption(option);
	myChart2.setOption(option1);
	myChart3.setOption(option2);
	myChart4.setOption(option);
  }


</script>



<style scoped>
	.el-row {
    /* 行与行之间的间隙 */
	margin-bottom: 0px;
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

  .setbg {
    background: url(@/assets/images/猫.gif);
    /* 图片不重复 */
    background-repeat: no-repeat;  
    background-position: center;
    background-size: 100% 100%;
    height: 100%;
    width: 100%
  }
</style>