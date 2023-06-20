<template>
    <div class="b2-container">
        <!-- <div class="area-conditions-header">
            <router-link class='logo' to="/main" style="height: 10%; width: 10%;">
                <img  src="../assets/img/SVision2.svg" 
                alt="SVision" style="zoom: 100%;">
              </router-link>
            <div class="area-conditions-nav">
                <div class="nav1">1</div>
                <div class="nav2">2</div>
                <div class="nav3">3</div>
                <div class="nav4">4</div>
                <div class="nav5">5</div>
            </div>
            <div class="weather-report">
                <WeatherReport></WeatherReport>
            </div>
        </div> -->

        <BasicHeader :title="title" style="background-color: black; margin-top: 0;"></BasicHeader>

        <div class="area-conditions-main">
            <div class="left">
                <div class="left-1" style="font-size: larger">
                    <span>营区基本情况</span>
                    <span> | Information</span>
                </div>
                <div class="left-2">
                    <div class="line"></div>
                    <div>人车底数</div>
                </div>
                <div class="left-3">
                    <div>园区人员数量</div>
                    <div>381人</div>
                    <div>营区车辆数量</div>
                </div>
                <div class="b-box">
                    <BasicPlot :option="option_bar1"></BasicPlot>
                </div>
                <div class="left-5">
                    <div class="line"></div>
                    <div>车辆进出统计</div>
                </div>
                <div class="left-6">
                    <div>当日入营车辆数</div>
                    <div>37辆</div>
                    <div>出营车辆数</div>
                </div>
                <div class="b-box">
                    <BasicPlot :option="option_bar2"></BasicPlot>
                </div>
                <div class="left-8">
                    <div class="line"></div>
                    <div>访客管理</div>
                </div>
                <div class="b-box">
                    <BasicPlot :option="option_radar"></BasicPlot>
                </div>
            </div>
            <div class="right">
                <div class="right-1" style="font-size: larger">
                    <span class="line"></span>
                    <span>营区安全</span>
                    <span> | Safety</span>
                </div>
                <div class="right-2">
                    <div class="line"></div>
                    <div>安全设施监控情况</div>
                </div>

                <div class="right-3">
                  <div class="item-1">
                    <div class="item-svg">
                      <svg t="1676518681233" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" 
                      p-id="2783" width="35" height="35">
                        <path d="M257.2 442.3h112.5v184H257.2z" fill="#0008D9" p-id="2784"></path><path d="M339.8 728.1H98.2V612h271.5v86.1c0.1 16.5-13.4 30-29.9 30z" fill="#2269F9" p-id="2785"></path><path d="M821.4 525.5c-1.2 0-2.3-0.1-3.5-0.3L217.4 420.4c-5.3-0.9-9.9-3.8-12.9-8.2s-4.3-9.7-3.3-14.9l34.1-195.1 640 111.8-34.2 195c-1.7 9.6-9.9 16.5-19.7 16.5z" fill="#F0CC37" p-id="2786"></path><path d="M243.3 213.7L863.6 322l-32.4 185.2c-0.8 4.8-5 8.3-9.8 8.3-0.6 0-1.2-0.1-1.8-0.2L219.1 410.5c-3.6-0.6-5.6-2.8-6.5-4.1-0.9-1.3-2.3-3.9-1.7-7.5l32.4-185.2M227 190.5l-35.8 204.9c-2.9 16.3 8.1 31.9 24.4 34.7L816.2 535c1.7 0.3 3.5 0.5 5.2 0.5 14.3 0 27-10.3 29.5-24.8l35.8-204.9L227 190.5z" fill="#101780" p-id="2787"></path><path d="M728.1 562.4c-1.2 0-2.3-0.1-3.5-0.3l-516.3-90.2c-5.3-0.9-9.9-3.8-12.9-8.2s-4.3-9.7-3.3-14.9l43.1-246.6 555.7 97-43.1 246.6c-1.7 9.6-10 16.6-19.7 16.6z" fill="#2269F9" p-id="2788"></path><path d="M243.3 213.7l536 93.6-41.4 236.8c-0.8 4.8-5 8.3-9.8 8.3-0.6 0-1.2-0.1-1.8-0.2L210.1 462c-5.4-0.9-9.1-6.1-8.1-11.6l41.3-236.7M227 190.5L182.2 447c-2.9 16.3 8.1 31.9 24.4 34.7l516.3 90.2c1.7 0.3 3.5 0.5 5.2 0.5 14.3 0 27-10.3 29.5-24.8L802.4 291 227 190.5z" fill="#101780" p-id="2789"></path><path d="M780.8 473.7L347.4 398c-83.9-14.7-140-94.5-125.4-178.4l5.1-29 737.3 128.8-5.1 29c-14.7 83.8-94.6 139.9-178.5 125.3z" fill="#0008D9" p-id="2790"></path><path d="M76.4 833.5h6.4c9.2 0 16.7-7.5 16.7-16.7V523.3c0-9.2-7.5-16.7-16.7-16.7h-6.4c-9.2 0-16.7 7.5-16.7 16.7v293.5c0 9.2 7.4 16.7 16.7 16.7z" fill="#101780" p-id="2791"></path><path d="M318.122 250.75l80.68 14.088-4.782 27.385-80.68-14.086z" fill="#FF8F19" p-id="2792"></path><path d="M313.5 689.6c-10.8 0-19.6-8.8-19.6-19.6s8.8-19.6 19.6-19.6 19.6 8.8 19.6 19.6-8.8 19.6-19.6 19.6z" fill="#2269F9" p-id="2793"></path><path d="M313.5 655.5c8 0 14.6 6.5 14.6 14.6s-6.5 14.6-14.6 14.6-14.6-6.5-14.6-14.6 6.6-14.6 14.6-14.6m0-10c-13.6 0-24.6 11-24.6 24.6 0 13.6 11 24.6 24.6 24.6 13.6 0 24.6-11 24.6-24.6 0-13.7-11-24.6-24.6-24.6z" fill="#101780" p-id="2794"></path></svg>
                      </div>
                      <div class="desc">
                        <div class="desc-title">监控摄像头</div>
                        <div class="num">2150</div>
                      </div>
                  </div>
                  <div class="item-2">
                    <div class="item-svg">
                      <svg t="1676520253931" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1354" 
                      width="35" height="35"><path d="M280 840h-68c-3.3 0-6-2.7-6-6v-6.6c0-3.3 2.7-6 6-6h68c3.3 0 6 2.7 6 6v6.6c0 3.3-2.7 6-6 6zM817.4 840h-68c-3.3 0-6-2.7-6-6v-6.6c0-3.3 2.7-6 6-6h68c3.3 0 6 2.7 6 6v6.6c0 3.3-2.7 6-6 6z" fill="#32378E" p-id="1355"></path><path d="M886.8 831.7H137.2c-16.6 0-30-13.4-30-30v-72.4h809.7v72.4c-0.1 16.6-13.5 30-30.1 30z" fill="#0748F2" p-id="1356"></path><path d="M832.2 511H191.8c-13.4 0-25.6 9.3-29.4 22.4l-53.9 186.8c-5.6 19.4 7.4 38 26.7 38h753.6c19.3 0 32.3-18.6 26.7-38l-53.9-186.8c-3.8-13.1-15.9-22.4-29.4-22.4z" fill="#3377FF" p-id="1357"></path><path d="M292 509h-32l8.2-317.4c0.1-4.2 3.6-7.6 7.8-7.6 4.2 0 7.7 3.4 7.8 7.6L292 509z" fill="#00DDF4" p-id="1358"></path><path d="M292 510.4h-32l8.2-248.8c0.1-3.3 3.6-6 7.8-6 4.2 0 7.7 2.6 7.8 6l8.2 248.8z" fill="#00C1D6" p-id="1359"></path><path d="M769.4 509h-32l8.2-317.4c0.1-4.2 3.6-7.6 7.8-7.6 4.2 0 7.7 3.4 7.8 7.6l8.2 317.4z" fill="#00DDF4" p-id="1360"></path><path d="M769.4 510.4h-32l8.2-248.8c0.1-3.3 3.6-6 7.8-6 4.2 0 7.7 2.6 7.8 6l8.2 248.8z" fill="#00C1D6" p-id="1361"></path><path d="M888.1 815.8H135.7c-15 0-27.4-12.2-28.5-27.7-0.1 0.7-0.1 1.5-0.1 2.3v11.5c0 16.6 12.8 30 28.6 30H888c15.8 0 28.6-13.4 28.6-30v-11.5c0-0.8 0-1.5-0.1-2.3-1.1 15.4-13.4 27.7-28.4 27.7z" fill="#04040A" p-id="1362"></path><path d="M391.2 793.3m-12 0a12 12 0 1 0 24 0 12 12 0 1 0-24 0Z" fill="#FFE164" p-id="1363"></path><path d="M471.7 793.3m-12 0a12 12 0 1 0 24 0 12 12 0 1 0-24 0Z" fill="#00DDF4" p-id="1364"></path><path d="M552.3 793.3m-12 0a12 12 0 1 0 24 0 12 12 0 1 0-24 0Z" fill="#00DDF4" p-id="1365"></path><path d="M632.8 793.3m-12 0a12 12 0 1 0 24 0 12 12 0 1 0-24 0Z" fill="#00DDF4" p-id="1366"></path><path d="M786.4 790.3h49v12h-49z" fill="#FFE164" p-id="1367"></path><path d="M693.3 269.9l-12.7 12.7c-43.5-40.3-99.7-62.4-159.4-62.4s-115.9 22.1-159.4 62.4l-12.7-12.7c46.9-43.7 107.6-67.7 172.1-67.7s125.2 24 172.1 67.7z" fill="#FFE164" p-id="1368"></path><path d="M658.7 304.5L646 317.2c-33-29.9-76.8-48.2-124.7-48.2s-91.7 18.3-124.7 48.2l-12.7-12.7C420 271.3 468.3 251 521.2 251s101.2 20.3 137.5 53.5z" fill="#FFE164" p-id="1369"></path><path d="M624.1 339.1l-12.8 12.8c-24.1-21.1-55.6-34-90.1-34-34.5 0-66 12.8-90.1 34l-12.8-12.8c27.4-24.4 63.4-39.2 102.9-39.2s75.5 14.8 102.9 39.2z" fill="#FFE164" p-id="1370"></path><path d="M355 758H215l180.7-247h140zM627 758h-96l180.7-247h96z" fill="#6DA0FF" p-id="1371"></path></svg></div>
                      <div class="desc">
                        <div class="desc-title">报警器</div>
                        <div class="num">381</div>
                      </div>
                  </div>
                  <div class="item-3">
                    <div class="item-svg">
                      <svg t="1676520195168" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" 
                      p-id="1201" width="35" height="35">
                      <path d="M388.3 726.8h246.5v120.5H388.3z" fill="#32378E" p-id="1202"></path><path d="M388.3 640.8h246.5v120.5H388.3zM695.5 883.7H327.7c-4.1 0-7.5-3.4-7.5-7.5v-11.3c0-1.5 1.2-2.7 2.7-2.7h377.5c1.5 0 2.7 1.2 2.7 2.7v11.3c-0.1 4.2-3.4 7.5-7.6 7.5z" fill="#161235" p-id="1203"></path><path d="M699 869.2H324.1c-3.8 0-5.5-4.8-2.5-7.1l66.7-53.2h246.5l66.7 53.2c3 2.3 1.3 7.1-2.5 7.1z" fill="#8875FF" p-id="1204"></path><path d="M941.6 738.4H82.4c-9.9 0-18-8.1-18-18V158.3c0-9.9 8.1-18 18-18h859.1c9.9 0 18 8.1 18 18v562.2c0.1 9.9-8 17.9-17.9 17.9z" fill="#9180FF" p-id="1205"></path><path d="M512 706.8m-21.3 0a21.3 21.3 0 1 0 42.6 0 21.3 21.3 0 1 0-42.6 0Z" fill="#FFE164" p-id="1206"></path><path d="M106.3 180.4h812.4v490.3H106.3z" fill="#161235" p-id="1207"></path><path d="M623.3 668.5l-246.7-2.6 485.7-485.4h56l-1 194z" fill="#161235" p-id="1208"></path><path d="M199.3 671.5h-45l489.5-491h45z" fill="#161235" p-id="1209"></path></svg>
                    </div>
                      <div class="desc">
                        <div class="desc-title">消防设备</div>
                        <div class="num">1987</div>
                      </div>
                  </div>

    
                </div>
                <div class="right-4">
                  <BasicPlot :option="option_hori"></BasicPlot> 
                </div>
                <div class="right-5">
                    <div class="line"></div>
                    <div>当日警情情况</div>
                </div>
                <div class="right-6">
                    <ScrollerTemplate></ScrollerTemplate>
                </div>
                <div class="right-7">
                    <div class="line"></div>
                    <div>类型统计</div>
                    <div class="line"></div>
                    <div>当月警情情况</div>
                </div>
                <div class="right-8">
                    <div class="radar">
                      <BasicPlot :option="option_radar2"></BasicPlot>
                    </div>
                    <div class="tripies">
                      <el-progress :percentage="50" />
                      <el-progress :percentage="70" status="success" />
                      <el-progress :percentage="60" status="exception" />
                      <el-progress :percentage="100" status="warning" />
                      <!-- <div>    <el-progress type="circle" :percentage="25" /></div>
                        <div><ProgressCard :button="false"></ProgressCard></div>
                        <div><ProgressCard :button="false"></ProgressCard></div>
                        <div><ProgressCard :button="false"></ProgressCard></div>                         -->
                    </div>
                </div>
            </div>   
        </div>
    </div>
</template>


<script lang="ts" setup>
/* eslint-disable */
import WeatherReport from '@/components/WeatherReport.vue';
import TemplateRadar from '@/components/TemplateRadar.vue';
import WareBar from '@/components/WareBar.vue';
// import TemplateRing from '@/components/TemplateRing.vue';
import BasicPlot from '@/components/BasicPlot.vue';
import * as echarts from "echarts";
import ScrollerTemplate from '@/components/ScrollerTemplate.vue';
import BasicHeader from '@/components/BasicHeader.vue';
import ACard from '@/components/ACard.vue';

const title = "营区态势"


var option_bar1 = {
  legend: {
    data: ['人员数量', '车辆数量'],
    
    textStyle: {
      color: '#000'    
    }
  },
  xAxis: {
    data: ['区域1', '区域2', '区域3', '区域4', '区域5'],
    axisLabel :{
      color: "#ffffff"
    }
  },
  yAxis: {
    axisLabel :{
      color: "#ffffff"
    }
  },
  series: [
    {
      name:"人员数量",
      type: 'bar',
      data: [230, 240, 180, 250, 270],
      color: '#62f0ff'
    },
    {
      name:"车辆数量",
      type: 'bar',
      data: [260, 240, 180, 220, 230],
      color: '#0197ff'
    }
  ]
};
var option_bar2 = {
  legend: {
    data: ['总数', '在营区'],
    textStyle: {
      color: '#000'    
    }
  },
  xAxis: {
    data: ['出口加工区', '产业园区', '对外贸易区', '仓储区','保税物流园区', '服务中心'],
    axisLabel :{
      color: "#ffffff"
    }
  },
  yAxis: {
    axisLabel :{
      color: "#ffffff"
    }},
  series: [
    {
      name:'总数',
      type: 'bar',
      data: [590, 890, 718, 825, 927, 728, 925],
      color: '#62f0ff'

    },
    {
      name:'在营区',
      type: 'bar',
      data: [260, 424, 518, 622, 723, 420, 727],
      color: '#0197ff'
    }
  ]
};


var option_radar = {
  color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
  title: {
    //text: 'Customized Radar Chart'
  },
  legend: {
    textStyle:{
      color: '#ffffff'
    }  
  },
  radar: [
    {
      indicator: [
        { text: '厂房1', max: 1000 },
        { text: '厂房2', max: 1000 },
        { text: '厂房3', max: 1000 },
        { text: '厂房4', max: 1000 },
        { text: '厂房5', max: 1000 },
        { text: '厂房6', max: 1000}
      ],
      center: ['25%', '60%'],
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
    {
      indicator: [
        { text: '厂房1', max: 1000 },
        { text: '厂房2', max: 1000 },
        { text: '厂房3', max: 1000 },
        { text: '厂房4', max: 1000 },
        { text: '厂房5', max: 1000 },
        { text: '厂房6', max: 1000 }
      ],
      center: ['75%', '60%'],
      radius: 60,
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
          value: [900, 880, 480, 800, 200],
          name: '今日出厂量',
          symbol: 'rect',
          symbolSize: 10,
          label: {
            show: true,
            formatter: function (params: { value: any; }) {
              return params.value;
            }
          }
        },
        {
          value: [605, 500, 630, 400, 150],
          name: '今日进厂量',
          symbol: 'rect',
          symbolSize: 10,
          label: {
            show: true,
            formatter: function (params: { value: any; }) {
              return params.value;
            }
          },
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
          value: [520, 718, 430, 800, 799, 700],
          name: '仓储总数',
          symbol: 'rect',
          symbolSize: 1,
          lineStyle: {
            type: 'dashed'
          },
          label: {
            show: true,
            formatter: function (params: { value: any; }) {
              return params.value;
            }
          }
        },
        {
          value: [1000, 930, 500, 690, 770, 690],
          name: '仓储安防等级',
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


var option_hori = {
  title: {
    text: '设备数量',
    textStyle: {
      color: '#ffffff',
      fontSize: '15px'
    }
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {},
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'value',
    boundaryGap: [0, 0.01],
    axisLabel: {
            color: '#ffffff',
        }
  },
  yAxis: {
    type: 'category',
    data: ['红绿灯', '监控摄像头', '电子锁', '安全门', '消防栓'],
    axisLabel: {
            color: '#ffffff',
        },
  },
  series: [
    {
      name: '当前',
      type: 'bar',
      data: [18, 234, 34, 104, 50],
      showBackground: true,
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
          { offset: 0, color: '#62f0ff' },
          { offset: 0.5, color: '#30c2ff' },
          { offset: 1, color: '#0197ff' }
        ])
      },
    }
  ]
};

var option_radar2 = {
  color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
  title: {
    text: '警情类别',
    textStyle:{
      fontSize : '10px',
      color: '#ffffff'
    }
  },
  legend: {
    show: false
  },
  radar: [
    {
      indicator: [
        { text: '火警类' },
        { text: '冲禁类' },
        { text: '群体性' },
        { text: '交通类' },
        { text: '行政性' }
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
          value: [100, 8, 0.4, 80],
          name: 'Data A'
        },
        {
          value: [60, 5, 0.3, 50],
          name: 'Data B',
          areaStyle: {
            color: 'rgba(255, 228, 52, 0.6)'
          }
        }
      ]
    },
  ]
};

</script>

<style scoped lang="scss">

.b2-container {
    background-image: url("../assets/img/areacondibg.png");
    background-size: cover;
    background-position: center;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-color: black;

}

.area-conditions-main {
    height: 92%;
    width: 100%;
    //border: 1px solid red;
    display: flex;
    justify-content: space-between;
    color: #fff;    

    div{
        margin-left: 2px;
        //border: 1px solid green;
    }
    .left {
        width: 25%;
        background-color: #000000;
        opacity: 85%;
        margin-left: 2%;
        padding: 0 5px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        div {
            //border: 1px solid green;
            margin-top: 1px;

        }
        .left-1 {
            height: 3%;
            justify-content: space-between;
            margin-bottom: 2%;
        }
        .left-2 {
            height: 3%;
            display: flex;
            align-items: center;
        }
        .left-3 {
            height: 3%;
            display: flex;
            justify-content: space-between;

        }
        .left-4 {
          padding: 3px 3px;
        }
        .left-5 {
            height: 3%;
            display: flex;
            align-items: center;
        }
        .left-6 {
            height: 3%;
            display: flex;
            justify-content: space-between;
        }
        .left-7 {
            height: 26%;
        }
        .left-8 {
            height: 3%;
            display: flex;
            align-items: center;
        }
        .left-9 {
            height: 26%;
        }
    }

    .line{
        height: 70%;
        width: 2%;
        background-color:#0096ff;
        margin-right: 10px;
    }

    .right {
        width: 25%;
        background-color: #000000;
        opacity: 85%;
        margin-right: 2%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        div {

            margin-top: 3px;
        }
        .right-1 {
            height: 3%;
            justify-content: space-between;
        }
        .right-2 {
            height: 3%;
            display: flex;
            align-items: center;
            .line{
                height: 70%;
                width: 2%;
                background-color:#0096ff;
                margin-right: 10px;
            }
        }
        .right-3 {
            height: 10%;
            display: flex;
            justify-content: space-between;
            div {
              display: flex;
              .item-svg { 
                padding-top: 14%;
                //border: 1px solid red;
                color: #0096ff;
              }
              .desc {
                display: flex;
                flex-direction: column;
                //border: 1px solid red;
              }
            }
            .item-1 {
              .num {
                color: #0096ff;
              }
            }
            .item-2 {
              .num {
                color: #37eae9;
              }
            }
            .item-3 {
              .num {
                color: #06d280;
              }
            }
        }
        .right-4 {
            height: 23%;
        }
        .right-5{
            height: 3%;
            align-items: center;
            display: flex;
        }
        .right-6 {
            height: 23%;
        }
        .right-7 {
            height: 3%;
            display: flex;
            justify-content: space-between;
        }
        .right-8 {
            width: 100%;
            height: 23%;
            display: flex;
            justify-content: space-between;
            .radar {
                width: 70%;
                height: 100%;
            }
            .tripies {
                height: 100%;
                width: 30%;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                div {
                    height: 30%;
                    width: 100%;
                }
            }
        }


    }
}


</style>


