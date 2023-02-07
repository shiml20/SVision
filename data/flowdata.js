/** 解释说明 流量信息
 * todaypeo->今日人流量
 * todaycar->今日车流量
 * yesterpeo->昨日人流量
 * yestercar->昨日车流量    
 * onedaypeo->从此时算起，到之前的23个小时共计24小时每小时分别的人流量，数组
 * site->按照地点分类,其中IsKey代表是否重点关注,其中onday为每6小时的人流量组成的数组
 */

var flowData = {
    code: 200,
    data: {
        todaypeo: 12410,
        todaycar: 4280,
        yesterpeo: 14190,
        yestercar: 3290,
        onedaypeo: [123, 130, 410, 130, 13, 31, 410, 130, 540, 123, 590, 310, 213, 123, 543, 132, 132, 432, 10, 234, 123, 543, 654, 123],
        site: {
            "车间a": {
                max: 100,
                min: 50,
                ave: 70,
                IsKey: false,
                oneday: [25, 31, 24, 12],
            },
            "车间b": {
                max: 200,
                min: 90,
                ave: 120,
                IsKey: true,
                oneday: [25, 31, 24, 12],
            },
            "车间c": {
                max: 100,
                min: 50,
                ave: 70,
                IsKey: false,
                oneday: [25, 31, 24, 12],
            },
            "食堂": {
                max: 831,
                min: 230,
                ave: 627,
                IsKey: true,
                oneday: [25, 31, 24, 12],
            },
            "保安处": {
                max: 100,
                min: 50,
                ave: 70,
                IsKey: false,
                oneday: [25, 31, 24, 12],
            },
            "住宿区": {
                max: 900,
                min: 213,
                ave: 520,
                IsKey: false,
                oneday: [25, 31, 24, 12],
            }
        }
    }
}