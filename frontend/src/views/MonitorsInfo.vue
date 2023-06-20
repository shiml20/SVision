<template>
    <div class="b-container">
        <BasicHeader :title="title"></BasicHeader>
        <div class="monitors-info-main">
            <div class="lm-bg">

                <div class="left">                
                    <div class="left-1">
                        <div class="title">
                            <h4>设备</h4>
                            <h4>数量</h4>
                        </div>
                        <div class="bit">1</div>
                        <div class="bit">6</div>
                        <div class="bit">8</div>
                        <div class="bit">2</div>
                        <div class="bit0">个</div>
                    </div>
                    <div class="left-2">
                        <div class="left-2-1">
                            <span style="color: #7f9dbf">监控摄像：</span>
                            <span class="num">
                                <span class="num-one">0</span>
                                <span class="num-one">3</span>
                                <span class="num-one">0</span>
                                <span class="num-one">1</span>
                                <span style="color: #7f9dbf">个</span>
                            </span>
                        </div>
                        <div class="left-2-2">
                            <span style="color: #7f9dbf">报警系统：</span>
                            <span class="num">
                                <span class="num-one">0</span>
                                <span class="num-one">5</span>
                                <span class="num-one">7</span>
                                <span class="num-one">7</span>
                                <span style="color: #7f9dbf">个</span>
                            </span>
                            
                        </div>
                        <div class="left-2-3">
                            <span style="color: #7f9dbf">消防设施：</span>
                            <span class="num">
                                <span class="num-one">1</span>
                                <span class="num-one">0</span>
                                <span class="num-one">5</span>
                                <span class="num-one">4</span>
                                <span style="color: #7f9dbf">个</span>
                            </span>
                        </div>
                    </div>
                    <div class="left-3"></div>
                   
                </div>
                <div class="mid">
                    <MonitorsPos></MonitorsPos>
                </div>
            </div>


            <div class="right">
                <div class="right-1">设备详情</div>
                <div class="right-2">
                    <ScrollerTemplate></ScrollerTemplate>
                </div>
                <div class="right-3">实时监控画面</div>
                <div class="right-4">
                    <div class="camera-1">
                        
                        <img src="..\..\public\monitors\realmonitor1.png" alt="pic1">
                        <img src="..\..\public\monitors\realmonitor2.png" alt="pic2">
                    </div>
                    <div class="camera-2">
                        <img src="..\..\public\monitors\realmonitor3.png" alt="pic3">
                        <img src="..\..\public\monitors\realmonitor4.png" alt="pic4">
                    </div>
                </div>
            </div>   

        </div>
    </div>
</template>


<script lang="ts" setup>
 /* eslint-disable */ 
import ScrollerTemplate from '@/components/ScrollerTemplate.vue';
import MonitorsPos from '@/components/MonitorsPos.vue';
import BasicHeader from '@/components/BasicHeader.vue';

const title = '监控点位信息'

</script>

<style scoped lang="scss">

.b-container {
    background-color: #010013;
}
.monitors-info-main {
    height: 90%;
    width: 100%;
    //border: 1px solid red;
    display: flex;
    justify-content: space-between;
    
    div{
        margin-left: 2px;
        //border: 1px solid green;
    }
    .left {
        padding: 1% 1%;
        width: 22%;
        height: 40%;
        background-color: rgba(0, 29, 113, 0.6);
        .left-1 {
            height: 40%;
            color: #ffffff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            .bit {
                width: 15%;
                height: 62%;
                //border: 3px solid #0096ff;
                font-size: 40px;
                color: #0096ff;
                background-color: #011144;
                padding-top: 2%;
                text-align: center;
            }
            .bit0 {
                margin-top: 10%;
                width: 5%;
            }
        }
        .left-2{
            height: 50%;
            display: flex;
            justify-content: space-between;
            flex-direction: column;
            color: white;
            .left-2-1 {
                height: 33%;
                padding-top: 3%;
                padding-bottom: 2%;
                display: flex;

            }
            .left-2-2 {
                height: 33%;
                padding-top: 3%;
                padding-bottom: 2%;
                display: flex;


            }
            .left-2-3 {
                height: 33%;
                padding-top: 3%;
                padding-bottom: 2%;
                display: flex;

            }
        }
    }

    .mid {
        width: 78%;
    }
    .num{
        display: flex;
        //border: 1px solid red;
        width: 55%;
        text-align: center;
        justify-content: space-between;
        .num-one {
            background-color: rgba(0, 60, 149, 0.7);
            width: 21%;
            //border: 1px solid green;
            margin-left: 3%;
            margin-right: 1%;
        }
    }

    
    .lm-bg {
        width: 100%;
        height: 100%;
        background: url(../assets/img/factory.png);
        background-size: cover;
        display: flex;
        justify-content: space-between;
    }
    .right {
        width: 25%;
        display: flex;
        flex-direction: column;
        color: #fff;
        background-color: rgba(0, 29, 113, 0.2);
        //div {
        //    border: 1px solid green;
        //}
        .right-1 {
            height: 5%;
            padding-top: 0 1%;
            font-size: x-large;
        }
        .right-2 {
            height: 50%;
        }
        .right-3 {
            height: 5%;
        }
        .right-4 {
            height: 40%;
            display: flex;
            justify-content: space-between;
            flex-direction: column;
            //div {
            //    border: 10px solid red;
            //}
            .camera-1 {
                height: 50%;
                display: flex;
                img {
                    height: 100%;
                    width: 50%;
                    margin: 4px 4px;
                }
            }
            .camera-2 {
                height: 50%;
                display: flex;
                img {
                    height: 100%;
                    width: 50%;
                    margin: 4px 4px;
                }
                //border: 10px solid yellow;
            }
        }
    }
}


</style>


