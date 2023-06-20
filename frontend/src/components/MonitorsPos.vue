<template>
    <div class="set_bg">
        <span class="point1">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point2">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point3">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point4">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point5">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point6">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point7">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        <span class="point8">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span>

        <span class="point9">
            <el-button type="info" @click="dialogTableVisible = true" circle > 
                <LocationInformation style="width: 8em; height: 8em; margin-right: 8px" />
            </el-button>
            <el-dialog v-model="dialogTableVisible" title="监控详情｜Monitor Information" style="width:900px">
                <hr>
                <el-row>
                <el-col style="width:400px">
                            <h1>|基础信息</h1>
                            <p>设备编号：231001</p>
                            <p>设备点位：主区1号楼B1层001拐角：</p>
                            <p>上次检修时间：2022-01-01</p>
                            <p>设备状况：正常</p>
                </el-col>
                <el-col style="width:500px">
                            <img src="../assets/img/pointInfo.png" alt="" width="850" height="400" >   
                </el-col>
                </el-row>
                <hr>
                <div>
                    <h1>|报警历史</h1>
                    <el-table :data="pi">
                    <el-table-column property="rank" label="序号" width="70" />
                    <el-table-column property="createtime" label="报警时间" width="180" />
                    <el-table-column property="organizer" label="负责人" width="100" />
                    <el-table-column property="solver" label="处理人员" width="100" />
                    <el-table-column property="result" label="处理结果" width="250" />
                    <el-table-column property="endtime" label="解决时间" width="150" />
                    </el-table>
                </div>
            </el-dialog>
        </span> 

        
    </div>
</template>

<script lang="ts" setup>
 /* eslint-disable */ 
import { reactive, ref } from 'vue'
import {LocationInformation} from '@element-plus/icons-vue'

const dialogTableVisible = ref(false)
const dialogFormVisible = ref(false)

const pi = [
  {
    rank: '1',
    createtime: '2022-1-01 11:39:30',
    organizer: '李主任',
    solver:'王专家',
    result:'系统错误报警，已全面排查',
    endtime:'2022-1-01 13:40:30'
  },
  {
    rank: '1',
    createtime: '2022-1-01 11:39:30',
    organizer: '李主任',
    solver:'王专家',
    result:'系统错误报警，已全面排查',
    endtime:'2022-1-01 13:40:30'
  },
  {
    rank: '1',
    createtime: '2022-1-01 11:39:30',
    organizer: '李主任',
    solver:'王专家',
    result:'系统错误报警，已全面排查',
    endtime:'2022-1-01 13:40:30'
  }
]
</script>

<style scoped>
  .set_bg {
    height: 100%;
    width: 100%;

    position: relative
}


.point1 {
    position: absolute;
    left: 5%;
    top: 10%;
}
.point2 {
    position: absolute;
    left: 20%;
    top: 10%;
}
.point3 {
    position: absolute;
    left: 20%;
    top: 30%;
}
.point4 {
    position: absolute;
    left: 30%;
    top: 60%;
}
.point5 {
    position: absolute;
    left: 40%;
    top: 40%;
}
.point6 {
    position: absolute;
    left: 50%;
    top: 60%;
}
.point7 {
    position: absolute;
    left: 60%;
    top: 10%;
}
.point8 {
    position: absolute;
    left: 70%;
    top: 35%;
}
.point9 {
    position: absolute;
    left: 80%;
    top: 65%;
}
.el-button{
    background: rgba(0, 0, 0, 0);
    border: none;
    width: 150px;
    height: 150px;
}

</style>



