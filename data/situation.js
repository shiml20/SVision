/**解释说明：营区态势
*basenumber：人车底数
    *zone1：区域1
    *peoplenum：人员数量
    *vehiclenum：车辆数量
*storage：仓储情况
    *factory1：厂房1
    *in：今日进仓量
    *out：今日出仓量
    *total：仓储总量
    *level：货物安防等级（用数字衡量）
*vistors：访客管理
    *process/product/commerce/store/deliver/serve：加工区/厂区/贸易区/仓储区/物流区/服务中心
    *total：总数
    *inside：在营区
*/

var situation=
{
    "basenumber":{
        "zone1":{
            "peoplenum":230,
            "vehiclenum":260
        },
        "zone2":{
            "peoplenum":240,
            "vehiclenum":240
        },
        "zone3":{
            "peoplenum":180,
            "vehiclenum":180
        },
        "zone4":{
            "peoplenum":250,
            "vehiclenum":220
        },
        "zone5":{
            "peoplenum":270,
            "vehiclenum":230
        }
    },

    "storage":{
        "factory1":{
            "in":605,
            "out":900,
            "total":520,
            "level":1000
        },
        "factory2":{
            "in":500,
            "out":880,
            "total":718,
            "level":930
        },
        "factory3":{
            "in":630,
            "out":480,
            "total":430,
            "level":500
        },
        "factory4":{
            "in":400,
            "out":800,
            "total":800,
            "level":690
        },
        "factory5":{
            "in":150,
            "out":200,
            "total":799,
            "level":770
        },
        "factory6":{
            "in":500,
            "out":500,
            "total":700,
            "level":690
        }  
    },
    "vistors":{
        "process":{
            "total":590,
            "inside":260
        },
        "product":{
            "total；":890,
            "inside":424
        },
        "commerce":{
            "total；":718,
            "inside":518
        },
        "store":{
            "total；": 825,
            "inside":622
        },
        "deliver":{
            "total；":927,
            "inside":723
        },
        "serve":{
            "total；":728,
            "inside":420
        }
    }
}