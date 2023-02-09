/** 解释说明 人员信息
 * num->姓名
 * phone->联系电话
 * type->出入类型，bool,true代表内部，false代表外来
 * com->所属公司
 * dep->若拜访，则为拜访部门
 * intime->入园时间
 * outtime->出园时间
 * IsOut->是否出园
 */

var deviceData = {
    code: 200,//校验码
    count: 4,//每页信息个数
    data: 
    {
        devicenum:{
            totalnum:200,
            monitornum:5,
            alarmnum:4,
            firefacnum:191
        },
        deviceinfo:[
            {
                basic:{
                    number:"10001",
                    age:5,
                    location:"A区1号楼B1层001",
                    repairtime:new Date(2022,5,1),
                    state:true
                },
                reporthst:
                [
                    {
                        hstnum:1,
                        reporttime:new Date(2022,6,1,11,45,15),
                        worker:"李先生",
                        res:"已全面检查"
                    },
                    {
                        hstnum:2,
                        reporttime:new Date(2022,6,9,12,15,15),
                        worker:"李先生",
                        res:"已全面检查"
                    }
                ]
            },
            {
                basic:{
                    number:"10002",
                    age:5,
                    location:"A区1号楼B1层002",
                    repairtime:new Date(2022,5,1),
                    state:true
                },
                reporthst:
                [
                    {
                        hstnum:1,
                        reporttime:new Date(2022,6,10,13,20,5),
                        worker:"李先生",
                        res:"已全面检查"
                    },
                    {
                        hstnum:2,
                        reporttime:new Date(2022,6,29,2,5,5),
                        worker:"李先生",
                        res:"已全面检查"
                    },
                    {
                        hstnum:3,
                        reporttime:new Date(2022,7,19,2,15,15),
                        worker:"李先生",
                        res:"已全面检查"
                    }
                ]
            },
            {
                basic:{
                    number:"10003",
                    age:5,
                    location:"A区1号楼F1层001",
                    repairtime:new Date(2022,5,1),
                    state:true
                },
                reporthst:
                [
                    {
                        hstnum:1,
                        reporttime:new Date(2022,8,1,1,45,15),
                        worker:"李先生",
                        res:"已全面检查"
                    }
                ]
            },
            {
                basic:{
                    number:"10004",
                    age:5,
                    location:"A区1号楼F1层002",
                    repairtime:new Date(2022,5,1),
                    state:true
                },
                reporthst:
                [
                ]
            },
            {
                basic:{
                    number:"10005",
                    age:5,
                    location:"A区1号楼F1层003",
                    repairtime:new Date(2022,5,1),
                    state:true
                },
                reporthst:
                [
                    {
                        hstnum:1,
                        reporttime:new Date(2022,6,16,8,42,15),
                        worker:"李先生",
                        res:"已全面检查"
                    }
                ]
            }
        ]
    }
}
