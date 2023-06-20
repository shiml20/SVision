
<template>
    <div class="rule-container">
    <el-row :gutter="12">
    <el-col :span="8">
      <el-card shadow="always">
        <div class="header">
        <h3 class="title">——监控系统使用管理制度——</h3>
        </div>
        <h1 class="subtitle"></h1>
        <div class="content">
            <p>为保证园区监控信息系统正常运行，特制定本管理制度</p>
            <p>一、监控系统由中控室负责监控，由运行部负责监督检中控室工作</p>
            <p>二、中控人员负责作好厂区监控范围内的工作，并作好当班的资料记录，发现异常情况必须及时向上级汇报。</p>
            <p>三、严格按规定操作步骤进行操作，密切注意监控设备运行状况，保证监控设备安全有序，不得无故中断监控，删除监控资料。</p>
            <p>四、监控用的计算机不得做与监控工作无关的事情。</p>
        </div>
      </el-card>
    </el-col>
    <el-col :span="8">
        <el-card shadow="always">
        <div class="header">
        <h3 class="title">——监控指挥中心值班登记制度——</h3>
        </div>
        <h1 class="subtitle"></h1>
        <div class="content">
            <p>为保证园区监控中心工作正常推进，特制定本管理制度</p>
            <p>一、监控中心值班员负责监控中心内设备24小时运行操作、监控、记录，发现异常行为及时上报。</p>
            <p>二、如有设备故障，监控中心值班人员及时向上级报告并通知维修人员进行维修处理。</p>
            <p>三、当日值班人员要负责监控值班室的清洁工作，保持地面、墙壁、设备无积尘、水渍、油渍。</p>
            <p>四、监控系统如因维护或其他原因要暂时改变监控系统的状态，应书面通知排查组加强巡检，确保园区安全。</p>    
        </div>
      </el-card>
    </el-col>
    <el-col :span="8">
        <el-card  shadow="always">
        <div class="header">
        <h3 class="title">——监控指挥中心人员工作标准——</h3>
        </div>
        <h1 class="subtitle"></h1>
        <div class="content">
            <p>为保证园区监控指挥中心正常运行，特制定本工作标准</p>
            <p>一、闭路监控系统由安管值班员负责全面的管理运作工作。</p>
            <p>二、值班人员应随时监视系统运作情况，发现异常应进行录像跟踪，并通知楼层巡逻安管员到现场查看。</p>
            <p>三、发现本系统有故障时立即通知中控室，由中控室安排维修，并做好值班记录的登记。</p>
            <p>四、值班人员应严格按照操作程序进行操作，并按园区安全处要求对整个区域每隔30分钟巡检一遍。</p>
        </div>
      </el-card>
    </el-col>
  </el-row>
  </div>
</template>

<script lang="ts" setup>



</script>

<style scoped>

.rule-container {
    width: 100%;
    height: 100%;
    position: relative;
}

.title{
    padding-top: 5%;
    text-align: center;
    color:aliceblue;
    font-size:20px
}

.subtitle{
    font-size: medium;
    font-weight: bold;
    text-align: center;
}
.header{
    background-color:#409EFF;
    height:70px;
    line-height: 70px;
}
.el-card{
    width:450px;
    height:450px
}

.content {
    font-size: 17px;
}

</style>
