<template>
    <div class="weather-datetime">
        <i :class="weathericon" class="weather-icon"></i>
        <div class="datetime">
            <p>{{ datetime }}</p>
        </div>
    </div>
</template>


<script setup>
/* eslint-disable */ 
import axios from 'axios';
import { ref } from 'vue'

// const path = 'https://devapi.qweather.com/v7/weather/now?location=101010100&key=436954781b124ce293bd699ff89311b2'
const path = ''
const weatherdata = ref([])
const weathericon = ref('')
const datetime = ref('')
weathericon.value = 'qi-' + '100'//res.data.now['icon']
const weatherinfo = ref('')



function getWeatherData(){
    axios.get(path)
    .then((res)=>{
        weatherdata.value = res.data
        weathericon.value = 'qi-' + '100'//res.data.now['icon']
        console.log(weathericon)
        console.log((res.data.now['text']))
        weatherinfo = res.data.now['']
    })
}


function getDate(){
				window.setTimeout(function(){
					window.requestAnimationFrame(getDate)
				},1000/2)
				var d=new Date();   
				var year=d.getFullYear()  //获取年
				var month=d.getMonth()+1;  //获取月，从 Date 对象返回月份 (0 ~ 11)，故在此处+1
				var day=d.getDay()    //获取日
				var days=d.getDate() //获取日期
				var hour=d.getHours()   //获取小时
				var minute=d.getMinutes()  //获取分钟
				var second=d.getSeconds()   //获取秒
				
				if(month<10) month="0"+month
				if(days<10) days="0"+days
				if(hour<10) hour="0"+hour
				if(minute<10) minute="0"+minute
				if(second<10) second="0"+second
				
				var week=new Array("星期日","星期一","星期二","星期三","星期四","星期五","星期六")
				var Tools=document.getElementById("Main")
				var da=year+" 年 "+month+" 月 "+days+" 日 "+week[day]+" "+hour+" : "+minute+" :"+second
				datetime.value=da
                // console.log(da)
            }
getDate()

// getWeatherData()

</script>


<style scoped lang="scss">


.weather-datetime {
    float: right;
    color: white;
    display: flex;
    position: relative;
    align-items: center;
    .weather-icon {
        color: white;
        padding-right: 5px;
    }

    .datetime {
        margin-top: 6%;
        font-size: 30%;
    }


}

</style>