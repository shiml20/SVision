<template>
    <div class="mainContainer">
        <video id="videoElement" class="centeredVideo" controls width="1024" height="576">Your browser is too old which
            doesn't support HTML5 video.</video>
    </div>
    <div class="mainContainer">
        <video id="videoElement2" class="centeredVideo" controls width="1024" height="576">Your browser is too old which
            doesn't support HTML5 video.</video>
    </div>
    <br>
</template>

<script setup>

/* eslint-disable */ 
import flvjs from 'flv.js'
import { ref, onMounted } from 'vue';

onMounted(() => {
    play()
    setInterval(function () {
            vElement.playbackRate = 1
            console.log("时延校正判断");
            if (!vElement.buffered.length) {
                return
            }
            var end = vElement.buffered.end(0)
            var diff = end - vElement.currentTime
            console.log(diff)
            if (5 <= diff && diff <= 60) {
                console.log("二倍速")
                vElement.playbackRate = 2
            }
            if (diff > 60) {
                console.log("跳帧")
                vElement.currentTime = end
            }
        }, 2500)
})

    function play(){
        var vElement = document.getElementById('videoElement');
        var vElement2 = document.getElementById('videoElement2');
        if (flvjs.isSupported()) {
            var flvPlayer = flvjs.createPlayer({
                type: 'flv',
                enableWorker: true,     //浏览器端开启flv.js的worker,多进程运行flv.js
                isLive: true,           //直播模式
                hasAudio: false,        //关闭音频             
                hasVideo: true,
                stashInitialSize: 128,
                enableStashBuffer: true, //播放flv时，设置是否启用播放缓存，只在直播起作用。
                url: 'http://localhost:8088/live?app=live&stream=a'
            });
            var flvPlayer2 = flvjs.createPlayer({
                type: 'flv',
                enableWorker: true,     //浏览器端开启flv.js的worker,多进程运行flv.js
                isLive: true,           //直播模式
                hasAudio: false,        //关闭音频             
                hasVideo: true,
                stashInitialSize: 128,
                enableStashBuffer: true, //播放flv时，设置是否启用播放缓存，只在直播起作用。
                url: 'http://localhost:8088/live?app=live&stream=b'
            });
            
            flvPlayer.attachMediaElement(vElement)
            flvPlayer2.attachMediaElement(vElement2)
            flvPlayer.load() //加载
            flvPlayer2.load() //加载
        }
    }
 
</script>


<style scoped>
.mainContainer {
    display: block;
    width: 1024px;
    margin-left: auto;
    margin-right: auto;
}

.urlInput {
    display: block;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 8px;
    margin-bottom: 8px;
}

.centeredVideo {
    display: block;
    width: 100%;
    height: 576px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: auto;
}

.controls {
    display: block;
    width: 100%;
    text-align: left;
    margin-left: auto;
    margin-right: auto;
}
</style>