<template>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">

    <div class="map-header"></div>
    <!-- <div class="map-main">     </div>-->
        <!-- <div class="map-left">111</div> -->
        <div id="container"></div>
        <!-- <div class="map-right">111</div> -->
                <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
</template>

<script setup>
/* eslint-disable */
import { onMounted, ref } from 'vue';
import { shallowRef } from '@vue/reactivity'
import AMapLoader from '@amap/amap-jsapi-loader';
import WeatherReport from './WeatherReport.vue';

let infoWindow = ref('')
let showInfoWindow = ref(false)



function setInfoWindows(map, marker,) {
        //实例化信息窗体
    var title = '<span>监控位点1</span><span style="font-size:11px;color:#F00; background: #fff">AAA</span>',
        content = [];
    content.push("基础信息");
    content.push("设备编号: A231001");
    content.push("设备点位: A231001");
    content.push("检修时间: 2023-02-10");
    content.push("设备状况: 正常");
    content.push("<a href='https://ditu.amap.com/detail/B000A8URXB?citycode=110105'>详细信息</a>");
    var infoWindow = new AMap.InfoWindow({
        isCustom: true,  //使用自定义窗体
        content: createInfoWindow(title, content.join("<br/>")),
        offset: new AMap.Pixel(16, -45)
    });

    //构建自定义信息窗体
    function createInfoWindow(title, content) {
        var info = document.createElement("div");
        info.className = "custom-info input-card content-window-card";

        //可以通过下面的方式修改自定义窗体的宽高
        info.style.width = "500px";
        // 定义顶部标题
        var top = document.createElement("div");
        var titleD = document.createElement("div");
        var closeX = document.createElement("img");
        top.className = "info-top";
        titleD.innerHTML = title;
        closeX.src = "https://webapi.amap.com/images/close2.gif";
        closeX.onclick = closeInfoWindow;
        top.style.backgroundColor = 'white';
        top.style.display = 'flex'
        top.style.width = '100%'
        top.style.justifyContent = "space-between"
        top.style.alignItems = "center"
        top.appendChild(titleD);
        top.appendChild(closeX);
        info.appendChild(top);

        // 定义中部内容
        var middle = document.createElement("div");
        middle.className = "info-middle";
        middle.style.backgroundColor = 'white';
        middle.innerHTML = content;
        info.appendChild(middle);

        // 定义底部内容
        var bottom = document.createElement("div");
        bottom.className = "info-bottom";
        bottom.style.position = 'relative';
        bottom.style.top = '0px';
        bottom.style.margin = '0 auto';
        var sharp = document.createElement("img");
        sharp.src = "https://webapi.amap.com/images/sharp.png";
        bottom.appendChild(sharp);
        info.appendChild(bottom);
        return info;
        }
        //关闭信息窗体
        function closeInfoWindow() {
        map.clearInfoWindow();
        }
            //鼠标点击marker弹出自定义的信息窗体
            marker.on('click', function () {
                infoWindow.open(map, marker.getPosition());
            });

        // var onMarkerClick = function (e) {
        //     infoWindow.open(map, e.target.getPosition());//打开信息窗体
        //     console.log(e)
        //     //e.target就是被点击的Marker
        // }
        // marker.on('click', onMarkerClick);//绑定click事件
}



function addMarker(pos, map, title='', onMarkerClick){
    var marker = new AMap.Marker({
        position: pos,
        title: title,
    })
    // marker.on('click', onMarkerClick);//绑定click事件
    setInfoWindows(map, marker)
    map.add(marker)
}

function ployGon(path, color='#1791fc'){
    return new AMap.Polygon({
        path: path,
        strokeColor: "green",
        strokeWeight: 6,
        strokeOpacity: 0.2,
        fillOpacity: 0.4,
        fillColor: color,
        zIndex: 50,
        bubble: true,
        })
}



onMounted(() => {

    var satellite = new AMap.TileLayer.Satellite();
        var roadNet = new AMap.TileLayer.RoadNet();
        var map = new AMap.Map('container', {
            center: [120.661213,30.061025], // 中心点
            zoom: 15, // 3-17 缩放比例
            viewMode: '3D',
            layers: [
                satellite,
                roadNet
            ]
        });
        //实时路况图层

        var traffic = new AMap.TileLayer.Traffic({
        'autoRefresh': true,     //是否自动刷新，默认为false
        'interval': 180,         //刷新间隔，默认180s
        });

             // map.remove(marker)
             var lineArr1 = [
            [120.670824,30.067162],
            [120.66664,30.054199],
            [120.650804,30.059548],
            [120.652049,30.060773],
            [120.654924,30.059699],
            [120.660589,30.069502], 
            [120.67076,30.066753], 
        ];
        var lineArr2 = [
            [120.657198,30.063132],
            [120.668764,30.060532]
        ];

        var polyline1 = new AMap.Polyline({
            path: lineArr1,          //设置线覆盖物路径
            strokeColor: "#3366FF", //线颜色
            strokeWeight: 5,        //线宽
            strokeStyle: "solid",   //线样式
        });
        var polyline2 = new AMap.Polyline({
            path: lineArr2,          //设置线覆盖物路径
            strokeColor: "#f0dd65", //线颜色
            strokeWeight: 5,        //线宽
            strokeStyle: "solid",   //线样式
        });

        map.add(traffic); //通过add方法添加图层
   
        map.add(polyline1);
        map.add(polyline2)
    
        AMap.plugin('AMap.ToolBar', function () {//异步加载插件
            var toolbar = new AMap.ToolBar();
            map.addControl(toolbar);
        });

        AMap.plugin('AMap.Scale', function () {//异步加载插件
            var scale = new AMap.Scale();
            map.addControl(scale);
        });
    
    
        var infoWindow = new AMap.InfoWindow({ //创建信息窗体
            isCustom: true,  //使用自定义窗体
            content: 'sss', //信息窗体的内容可以是任意html片段
            offset: new AMap.Pixel(16, -45)
        });
        var onMarkerClick = function (e) {
            infoWindow.open(map, e.target.getPosition());//打开信息窗体
            console.log(e)
            //e.target就是被点击的Marker
        }


        addMarker([120.667849,30.060779] ,map, "绍兴综保区")
        addMarker([120.582886,30.051549] ,map, "绍兴市政府")
        addMarker([120.749189,30.133992] ,map, "绍兴滨海新区")
        addMarker([120.494008,30.32757] ,map, "钱塘新区")
        addMarker([120.656986,30.060041] ,map, "点位1", onMarkerClick)
        addMarker([120.661213,30.061025] ,map, "点位2")
        addMarker([120.667779,30.064832] ,map, "点位3")


        var path = [
            [120.651857,30.060649],
            [120.653294,30.0605],
            [120.652929,30.058476],
            [120.650912,30.059144]
            ]
        var path1 = [
            [120.653423,30.060389],
            [120.659689,30.056563],
            [120.659667,30.056396],
            [120.653123,30.05842]
        ]
        var path2 = [
            [120.65574,30.061334],
            [120.658626,30.060127],
            [120.657628,30.058604],
            [120.655483,30.060182]
        ]
        var path3 = [
            [120.658841,30.060052],
            [120.661523,30.059351],
            [120.660096,30.057448],
            [120.657843,30.058488]
        ]
        var path4 = [
            [120.657038,30.062843],
            [120.660021,30.062425],
            [120.65868,30.060326],
            [120.655965,30.061561]
        ]
        var path5 = [
            [120.660193,30.062341],
            [120.663347,30.061728],
            [120.66163,30.059565],
            [120.658969,30.060308]
        ]
        var path6 = [
            [120.662392,30.058531],
            [120.666158,30.057464],
            [120.665621,30.056479],
            [120.66163,30.057399]
        ]
        var path7 = [
            [120.663529,30.06042],
            [120.668185,30.059492],
            [120.66752,30.057932],
            [120.662713,30.059343]
        ]
        var path8 = [
            [120.664151,30.061404],
            [120.667386,30.060722],
            [120.667075,30.059868],
            [120.663641,30.060648]
        ]
        var path9 = [
            [120.667482,30.060648],
            [120.668384,30.060481],
            [120.66819,30.059645],
            [120.667193,30.059914]
        ]
        var path10 = [
            [120.657584,30.063902],
            [120.658593,30.066318],
            [120.66139,30.065737],
            [120.660556,30.063503]
        ]
        var path11 = [
            [120.658579,30.06636],
            [120.660725,30.069349],
            [120.662179,30.06902],
            [120.660527,30.065863]
        ]
        var path12 = [
            [120.662329,30.069075],
            [120.663423,30.068853],
            [120.661657,30.065491],
            [120.660677,30.065788]
        ]
        var path13 = [
            [120.666038,30.064776],
            [120.66812,30.067599],
            [120.663614,30.068806],
            [120.662026,30.065705]
        ]
        var path14 = [
            [120.660695,30.063384],
            [120.6643,30.062604],
            [120.665867,30.064572],
            [120.661747,30.065649]
        ]         
        var path15 = [
            [120.668699,30.067543],
            [120.670802,30.066986],
            [120.669751,30.063625],
            [120.666446,30.064591]
        ] 
        var path16 = [
            [120.666532,30.064609],
            [120.669793,30.063718],
            [120.668871,30.060895],
            [120.664515,30.061824]
        ]
        var path17 = [
            [120.660655,30.056233],
            [120.661728,30.056661],
            [120.662951,30.056029],
            [120.664711,30.055546],
            [120.664797,30.055026]
        ]    
        var path18 = [
            [120.667372,30.056512],
            [120.665955,30.054803],
            [120.666814,30.054506],
            [120.667522,30.056475]
        ]                                            
        var polygon = ployGon(path);
        var polygon1 = ployGon(path1, '#fc011a');
        var polygon2 = ployGon(path2, '#f9bf1a');
        var polygon3 = ployGon(path3, '#fc011a');
        var polygon4 = ployGon(path4, '#5ede56');
        var polygon5 = ployGon(path5, '#fc011a');
        var polygon6 = ployGon(path6, '#f9bf1a');
        var polygon7 = ployGon(path7, '#fc011a');
        var polygon8 = ployGon(path8, '#f9bf1a');
        var polygon9 = ployGon(path9, '#fc011a');
        var polygon10 = ployGon(path10, '#5ede56');
        var polygon11 = ployGon(path11, '#fc011a');
        var polygon12 = ployGon(path12, '#f9bf1a');
        var polygon13 = ployGon(path13, '#fc011a');
        var polygon14 = ployGon(path14, '#f9bf1a');
        var polygon15 = ployGon(path15, '#fc011a');
        var polygon16 = ployGon(path16, '#5ede56');
        var polygon17 = ployGon(path17, '#fc011a');
        var polygon18 = ployGon(path18, '#f9bf1a');
         map.add([
            polygon, polygon1, polygon2,
            polygon3, polygon4, polygon5,
            polygon6, polygon7, polygon8, 
            polygon9, polygon10, polygon11, 
            polygon12, polygon13, polygon14, 
            polygon15, polygon16, polygon17, 
            polygon18
        ])
    
    });
        
</script>

<style scoped lang="scss">

html, body, #container {
    height: 100%;
    width: 100%;
}

.content-window-card {
    position: relative;
    box-shadow: none;
    bottom: 0;
    left: 0;
    width: auto;
    padding: 0;
}

.content-window-card p {
    height: 2rem;
}

.custom-info {
    border: solid 1px silver;
}

div.info-top {
    position: relative;
    background: none repeat scroll 0 0 #F9F9F9;
    border-bottom: 1px solid #CCC;
    border-radius: 5px 5px 0 0;
}

div.info-top div {
    display: inline-block;
    color: #333333;
    font-size: 14px;
    font-weight: bold;
    line-height: 31px;
    padding: 0 10px;
}

div.info-top img {
    position: absolute;
    top: 10px;
    right: 10px;
    transition-duration: 0.25s;
}

div.info-top img:hover {
    box-shadow: 0px 0px 5px #000;
}

div.info-middle {
    font-size: 12px;
    padding: 10px 6px;
    line-height: 20px;
}

div.info-bottom {
    height: 0px;
    width: 100%;
    clear: both;
    text-align: center;
}

div.info-bottom img {
    position: relative;
    z-index: 104;
}

span {
    margin-left: 5px;
    font-size: 11px;
}

.info-middle img {
    float: left;
    margin-right: 6px;
}


    .map-main {
        display: flex;
  
    }

    #container{
        padding:0px;
        margin: 0px;
        width: 100%;
        height: 100%;
        align-items: center;
    }
    .map-left{
        width: 200px;
        background-color: aqua;
        opacity: 100%;
        color: white;
    }
    .map-right{
        width: 200px;
        background-color: aqua;
        opacity: 100%;
        color: white;
    }
</style>