<!-- <script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <router-view></router-view>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  display: flex;
  align-items: center;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style> -->

<template>
    <div class="b-container">
      <div class="flow-info-header">
        <router-link class='logo' to="/main" style="height: 10%; width: 10%;">
          <img src="../assets/img/SVision2.svg" alt="SVision" style="zoom: 100%;">
        </router-link>
        <h2>流量信息</h2>
        <WeatherReport class="weather-report"></WeatherReport>
      </div>
      <div class="flow-info-main">
        <div class="left">
          <div class="left-top">
            <p>当前人流量</p>
            <span>一个滚动显示数字的组件 48774</span>
          </div>
          <div class="left-mid">
            <WareLine lineColor="#04e38a"></WareLine>
          </div>
          <div class="left-right">
            <WareBar :foo="20" barColor="#04e38a"></WareBar>
          </div>
        </div>
        <div class="right">
          <div class="right-top">
            <div class="right-top-left">
              <div class="rtlt">
                <div>
                  <h3>平均人流量</h3>
                </div>
                <div>6,876人</div>
              </div>
              <div class="rtlb">
                <div class="rtlbl">
                  <h4>昨日流量</h4>
                  <p>7213</p>
                </div>
                <div class="rtlbr">
                  <h4>环比变化</h4>
                  <p>-1%</p>
                </div>
              </div>
            </div>
            <div class="right-top-mid">
              <div class="rtmt">
                <h3>平均车流量</h3>
                <div>9,679台</div>
              </div>
              <div class="rtmb">
                <div class="rtmbl">
                  <h4>昨日车流量</h4>
                  <div>1,834</div>
                </div>
                <div class="rtmbr">
                  <h4>小时最大车流量</h4>
                  <div>2,919</div>
                </div>
              </div>
            </div>

            <div class="right-top-right">
              <div class="rtrl">
                <div><svg t="1676376680218" class="icon" viewBox="0 0 1024 1024" version="1.1"
                    xmlns="http://www.w3.org/2000/svg" p-id="3207" width="60" height="60">
                    <path
                      d="M265.131637 105.372106V26.007694a26.021813 26.021813 0 0 0-52.029507 0v79.364412zM394.760648 105.372106V26.007694a26.021813 26.021813 0 0 0-52.029507 0v79.364412zM524.375539 105.372106V26.007694a26.021813 26.021813 0 0 0-52.029507 0v79.364412zM654.00455 105.372106V26.007694a26.021813 26.021813 0 0 0-52.029507 0v79.364412zM783.619442 105.372106V26.007694a26.021813 26.021813 0 0 0-52.029507 0v79.364412zM731.604054 918.642013v79.350293a26.021813 26.021813 0 0 0 52.029507 0v-79.350293zM601.975043 918.642013v79.350293a26.021813 26.021813 0 0 0 52.029507 0v-79.350293zM472.346032 918.642013v79.350293a26.021813 26.021813 0 0 0 52.029507 0v-79.350293zM342.731141 918.642013v79.350293a26.021813 26.021813 0 0 0 52.029507 0v-79.350293zM213.10213 918.642013v79.350293a26.021813 26.021813 0 0 0 52.029507 0v-79.350293zM918.642013 278.756732h79.350293a26.007694 26.007694 0 0 0 0-52.015388h-79.350293zM918.642013 408.385743h79.350293a26.021813 26.021813 0 0 0 0-52.029507h-79.350293zM918.642013 538.014754h79.350293a26.021813 26.021813 0 0 0 0-52.029508h-79.350293zM918.642013 667.643764h79.350293a26.021813 26.021813 0 0 0 0-52.029507h-79.350293zM918.642013 797.272775h79.350293a26.021813 26.021813 0 0 0 0-52.029507h-79.350293zM105.372106 745.243268H26.007694a26.021813 26.021813 0 0 0 0 52.029507h79.364412zM105.372106 615.600138H26.007694a26.021813 26.021813 0 0 0 0 52.029507h79.364412zM105.372106 485.985246H26.007694a26.021813 26.021813 0 0 0 0 52.029508h79.364412zM105.372106 356.356236H26.007694a26.021813 26.021813 0 0 0 0 52.029507h79.364412zM105.372106 226.741344H26.007694a26.007694 26.007694 0 0 0 0 52.015388h79.364412zM753.079462 457.12546q-8.344488-6.720772-26.332437-6.720772h-45.817028v59.159738h45.817028q17.987949 0 26.332437-7.596167t8.344488-23.833326q0-14.331058-8.344488-21.009473z"
                      p-id="3208" fill="#1afa29"></path>
                    <path
                      d="M847.339704 121.609266h-670.665288a55.06515 55.06515 0 0 0-55.06515 55.06515v670.665288a55.06515 55.06515 0 0 0 55.06515 55.065149h670.665288a55.06515 55.06515 0 0 0 55.065149-55.065149v-670.665288a55.06515 55.06515 0 0 0-55.065149-55.06515zM593.009307 430.736546h23.070886v170.490176H593.009307z m-174.796553 0h23.085005v69.93274h88.951396v-69.93274h23.085006v170.490176h-23.070886v-80.140972h-88.951396v80.140972h-23.085006z m-157.683998 19.766977q21.757794-24.398097 58.397297-24.412217 28.888025 0 47.440745 14.853472t22.266087 40.94588h-22.251968q-3.247432-16.943123-15.714747-26.163005t-32.06486-9.219883q-25.654712 0-40.832927 18.849224T262.618407 516.101648q0 33.886246 14.11927 51.605929t40.94588 17.747921q19.766977 0 32.940255-12.227287t17.39494-34.747522h22.266088q-4.405212 31.556567-24.186308 49.417443t-50.038691 17.917352q-35.298173 0-56.194691-24.299262t-20.938876-65.471051q-0.127073-41.115312 21.616601-65.541648z m510.693967 65.132189q-13.978077 13.681572-38.799752 13.681572-32.587273-0.112954-51.507094 0.240027v71.669411h-23.056766V430.736546h74.57798q24.821675 0 38.799751 12.467315t13.963958 34.507494q0 24.228666-13.963958 37.924357z"
                      p-id="3209" fill="#1afa29"></path>
                  </svg>
                </div>
                <div>
                  <div>273</div>
                  <div>主变台数</div>
                </div>
  
              </div>
              <div class="rtrm">
                <svg t="1676377209213" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="4614" width="60" height="60">
                  <path
                    d="M512 67.331507c-279.145205 0-504.986301 225.841096-504.986301 504.986301C7.013699 716.8 70.136986 855.671233 178.147945 951.057534c14.027397 12.624658 36.471233 11.221918 49.095891-2.805479 12.624658-14.027397 11.221918-36.471233-2.80548-49.095891C130.454795 816.394521 77.150685 697.161644 77.150685 572.317808c0-239.868493 194.980822-434.849315 434.849315-434.849315s434.849315 194.980822 434.849315 434.849315c0 127.649315-56.109589 248.284932-152.89863 331.046576-15.430137 12.624658-16.832877 35.068493-4.208219 49.09589 7.013699 8.416438 16.832877 12.624658 26.652055 12.624658 8.416438 0 15.430137-2.805479 22.443835-8.416439 113.621918-96.789041 178.147945-237.063014 178.147945-384.350685 0-277.742466-225.841096-504.986301-504.986301-504.986301z"
                    fill="#1afa29" p-id="4615"></path>
                  <path
                    d="M499.375342 295.978082c11.221918 0 21.041096-9.819178 21.041096-21.041096v-71.539726c0-11.221918-9.819178-21.041096-21.041096-21.041096s-21.041096 9.819178-21.041095 21.041096v71.539726c0 11.221918 9.819178 21.041096 21.041095 21.041096zM392.767123 218.827397c-4.208219-11.221918-15.430137-16.832877-26.652055-12.624657-11.221918 4.208219-16.832877 15.430137-12.624657 26.652055l23.846575 67.331506c2.805479 8.416438 11.221918 14.027397 19.638356 14.027398 2.805479 0 4.208219 0 7.013699-1.40274 11.221918-4.208219 16.832877-15.430137 12.624658-26.652055L392.767123 218.827397zM279.145205 277.742466c-7.013699-8.416438-21.041096-9.819178-29.457534-2.80548-8.416438 7.013699-9.819178 21.041096-2.805479 29.457535l46.290411 54.706849c4.208219 5.610959 9.819178 7.013699 15.430137 7.013698 4.208219 0 9.819178-1.40274 14.027397-5.610958 8.416438-7.013699 9.819178-21.041096 2.805479-29.457535l-46.290411-53.304109zM232.854795 444.668493c2.805479 1.40274 7.013699 2.805479 9.819178 2.80548 7.013699 0 14.027397-4.208219 18.235616-11.221918 5.610959-9.819178 2.805479-22.443836-7.013699-28.054795l-61.720548-36.471233c-9.819178-5.610959-22.443836-2.805479-28.054794 7.013699-5.610959 9.819178-2.805479 22.443836 7.013699 28.054795l61.720548 37.873972zM117.830137 507.791781c-1.40274 11.221918 5.610959 22.443836 16.832877 23.846575l70.136986 12.624658h4.208219c9.819178 0 18.235616-7.013699 21.041096-16.832877 1.40274-11.221918-5.610959-22.443836-16.832877-23.846575l-70.136986-12.624658c-12.624658-1.40274-23.846575 5.610959-25.249315 16.832877zM140.273973 660.690411h4.208219l70.136986-12.624658c11.221918-1.40274 19.638356-12.624658 16.832877-23.846575-1.40274-11.221918-12.624658-19.638356-23.846576-16.832877l-70.136986 12.624658c-11.221918 1.40274-19.638356 12.624658-16.832877 23.846575 0 9.819178 8.416438 16.832877 19.638357 16.832877zM237.063014 706.980822L175.342466 743.452055c-9.819178 5.610959-14.027397 18.235616-7.013699 28.054794 4.208219 7.013699 11.221918 11.221918 18.235617 11.221918 4.208219 0 7.013699-1.40274 9.819178-2.805479l61.720548-36.471233c9.819178-5.610959 14.027397-18.235616 7.013698-28.054795-5.610959-11.221918-18.235616-15.430137-28.054794-8.416438zM824.810959 775.715068c7.013699 0 14.027397-4.208219 18.235616-11.221917 5.610959-9.819178 2.805479-22.443836-7.013698-28.054795l-61.720548-36.471233c-9.819178-5.610959-22.443836-2.805479-28.054795 7.013699-5.610959 9.819178-2.805479 22.443836 7.013699 28.054794l61.720548 36.471233c2.805479 2.805479 5.610959 4.208219 9.819178 4.208219zM800.964384 600.372603c-11.221918-1.40274-22.443836 5.610959-23.846576 16.832876-1.40274 11.221918 5.610959 22.443836 16.832877 23.846576l70.136986 12.624657h4.208219c9.819178 0 18.235616-7.013699 21.041096-16.832876 1.40274-11.221918-5.610959-22.443836-16.832876-23.846576l-71.539726-12.624657zM862.684932 483.945205l-70.136987 12.624658c-11.221918 1.40274-19.638356 12.624658-16.832877 23.846575 1.40274 9.819178 11.221918 16.832877 21.041096 16.832877h4.20822l70.136986-12.624657c11.221918-1.40274 19.638356-12.624658 16.832877-23.846576-2.805479-11.221918-14.027397-18.235616-25.249315-16.832877zM758.882192 441.863014c4.208219 0 7.013699-1.40274 9.819178-2.80548l61.720548-36.471233c9.819178-5.610959 14.027397-18.235616 7.013698-28.054794-5.610959-9.819178-18.235616-14.027397-28.054794-7.013699l-61.720548 36.471233c-9.819178 5.610959-14.027397 18.235616-7.013699 28.054795 4.208219 5.610959 11.221918 9.819178 18.235617 9.819178zM751.868493 270.728767c-8.416438-7.013699-22.443836-5.610959-29.457534 2.80548l-46.290411 54.706849c-7.013699 8.416438-5.610959 22.443836 2.805479 29.457534 4.208219 2.805479 8.416438 5.610959 14.027398 5.610959s12.624658-2.805479 15.430137-7.013699l46.290411-54.706849c7.013699-9.819178 5.610959-22.443836-2.80548-30.860274zM601.775342 312.810959c8.416438 0 16.832877-5.610959 19.638357-14.027397l23.846575-67.331507c4.208219-11.221918-1.40274-22.443836-12.624658-26.652055-11.221918-4.208219-22.443836 1.40274-26.652054 12.624658l-23.846576 67.331506c-4.208219 11.221918 1.40274 22.443836 12.624658 26.652055 1.40274 1.40274 4.208219 1.40274 7.013698 1.40274zM645.260274 415.210959c-12.624658-9.819178-30.860274-7.013699-40.679452 5.610959l-92.580822 122.038356c-16.832877 0-32.263014 7.013699-42.082192 19.638356-8.416438 11.221918-11.221918 23.846575-9.819178 36.471233 1.40274 12.624658 8.416438 25.249315 19.638356 33.665753 8.416438 7.013699 19.638356 9.819178 30.860274 9.819179h7.013699c12.624658-1.40274 25.249315-8.416438 33.665753-19.638357 9.819178-12.624658 12.624658-30.860274 8.416439-46.290411l92.580822-122.038356c4.208219-5.610959 7.013699-14.027397 5.610959-21.041096-2.805479-7.013699-7.013699-14.027397-12.624658-18.235616z"
                    fill="#1afa29" p-id="4616"></path>
                </svg>
                <div>50,170</div>
                <div>计量台数</div>
              </div>
              <div class="rtrr">
                <svg t="1676377368893" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="5810" width="60" height="60">
                  <path
                    d="M988.416 821.216l1.504-0.576-101.504-267.328A64.32 64.32 0 0 0 828.608 512h-20.608V112a32 32 0 1 0-64 0V512H544V112a32 32 0 1 0-64 0V512H272V112a32 32 0 0 0-64 0V512h-12.608a64.32 64.32 0 0 0-59.84 41.312l-101.472 267.328 1.504 0.576c-2.112 8.64-3.584 17.504-3.584 26.784C32 909.76 82.24 960 144 960h736c61.76 0 112-50.24 112-112 0-9.28-1.472-18.144-3.584-26.784zM195.392 576h633.184l61.12 160.992c-3.232-0.288-6.368-0.992-9.696-0.992h-736c-3.328 0-6.464 0.704-9.696 0.992L195.392 576zM880 896h-736c-26.464 0-48-21.536-48-48S117.536 800 144 800h736c26.464 0 48 21.536 48 48s-21.536 48-48 48z"
                    p-id="5811" fill="#1afa29"></path>
                </svg>
                <div style="font-size: larger">101</div>
                <div>网关数</div>
              </div>
            </div>
          </div>
          
          <div class="right-mid">
            <div class="right-mid-left">
              <WarePie pieColor="#04e38a"></WarePie>
            </div>
            <div class="right-mid-right">6</div>
          </div>
          <div class="right-btm">
            <div class="right-btm-1">
              <WareLine lineColor="#04e38a"></WareLine>
            </div>
            <div class="right-btm-2">
              <WareLine lineColor="#04e38a"></WareLine>
            </div>
            <div class="right-btm-3">
              <WareLine lineColor="#04e38a"></WareLine>
            </div>
            <div class="right-btm-4">
              <WareLine lineColor="#04e38a"></WareLine>
            </div>
            <div class="right-btm-5">
              <WareLine lineColor="#04e38a"></WareLine>
            </div>
            <div class="right-btm-6">
              <WareLine lineColor="#04e38a"></WareLine>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  <script lang="ts" setup>
  // import WeatherReport from './components/WeatherReport.vue';
  import WareLine from './components/WareLine.vue'
  import WareBar from './components/WareBar.vue';
  import WarePie from './components/WarePie.vue';
  
  
  </script>
  
  <style scoped lang="scss">
  .b-container {
    width: 100%;
    height: 100%;
    background: #000000;
  }
  
  .flow-info-header {
    height: 5%;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 10px;
    //border: 1px solid red;
    text-align: center;
    color: white;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  
    .weather-report {
      font-size: 50px;
      color: white;
    }
  }
  
  .flow-info-main {
    height: 90%;
    width: 100%;
    //border: 1px solid red;
    display: flex;
    flex-direction: row;
    color: rgb(4, 227, 138);
  }
  
  .flow-info-main .left {
    border: 1px solid green;
    width: 25%;
    margin-right: 3%;
    margin-left: 3%;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
  
    .left-top {
      margin-top: 3%;
      //border: 1px solid blue;
      height: 28%;
    }
  
    .left-mid {
      //border: 1px solid blue;
      height: 33%;
    }
  
    .left-right {
      //border: 1px solid blue;
      height: 28%;
      margin-bottom: 3%;
    }
  }
  
  .flow-info-main .right {
    //border: 1px solid red;
    width: 67%;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
  
    .right-top {
      //border: 1px solid blue;
      height: 33%;
      display: flex;
      justify-content: space-between;
  
      .right-top-left {
        //border: 1px solid salmon;
        width: 25%;
        color: rgb(4, 227, 138);
  
        .rtlt {
          height: 50%;
          //border: 1px solid yellow;
          display: flex;
          flex-direction: column;
        }
  
        .rtlb {
          height: 50%;
          //border: 1px solid yellow;
          display: flex;
  
          .rtlbl {
            height: 100%;
            width: 50%;
            //border: 1px solid green;
          }
  
          .rtlbr {
            height: 100%;
            width: 50%;
            //border: 1px solid green;
          }
        }
      }
  
      .right-top-mid {
        //border: 1px solid salmon;
        width: 25%;
  
        .rtmt {
          height: 50%;
          //border: 1px solid yellow;
          display: flex;
          flex-direction: column;
        }
  
        .rtmb {
          height: 50%;
          //border: 1px solid yellow;
          display: flex;
  
          .rtmbl {
            height: 100%;
            width: 50%;
            //border: 1px solid green;
            display: flex;
            flex-direction: column;
          }
  
          .rtmbr {
            height: 100%;
            width: 50%;
            //border: 1px solid green;
            display: flex;
            flex-direction: column;
          }
        }
      }
  
      .right-top-right {
        //border: 1px solid salmon;
        width: 40%;
        display: flex;
        text-align: center;
        justify-content: space-between;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.2);
  
  
        .rtrl {
          width: 33%;
          flex-direction: column;
          justify-content: space-between;
          margin-top: 5%;
          margin-bottom: 10%;
        }
  
        .rtrm {
          flex-direction: column;
          width: 33%;
          justify-content: space-between;
          margin-top: 5%;
          margin-bottom: 10%;
        }
  
        .rtrr {
          flex-direction: column;
          width: 33%;
          justify-content: space-between;
          margin-top: 5%;
          margin-bottom: 10%;
        }
      }
    }
  
    .right-mid {
      //border: 1px solid blue;
      height: 33%;
      display: flex;
      justify-content: space-between;
  
      .right-mid-left {
        //border: 1px solid salmon;
        width: 55%;
      }
  
      .right-mid-right {
        //border: 1px solid salmon;
        width: 40%;
      }
    }
  
    .right-btm {
      //border: 1px solid blue;
      height: 28%;
      display: flex;
      justify-content: space-between;
  
      .right-btm-1 {
        //border: 1px solid salmon;
        width: 15%;
      }
  
      .right-btm-2 {
        //border: 1px solid salmon;
        width: 15%;
      }
  
      .right-btm-3 {
        //border: 1px solid salmon;
        width: 15%;
      }
  
      .right-btm-4 {
        //border: 1px solid salmon;
        width: 15%;
      }
  
      .right-btm-5 {
        //border: 1px solid salmon;
        width: 15%;
      }
  
      .right-btm-6 {
        //border: 1px solid salmon;
        width: 15%;
      }
    }
  }
  </style>
  
  
  