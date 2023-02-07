/** 解释说明 车辆信息
 * num->车牌号
 * type->车的类型
 * usertype->出入类型，bool型，true代表内部车辆，false代表外来拜访
 * intime->入园时间，Date类，秒未定义
 * outtime->出园时间，Date类，秒未定义，注：若为undefined则代表未出园
 * IsOut->是否出园,bool,true代表已出园，false代表未出园
 * name->车主姓名
 * phone->手机号
 * money->缴费金额，0代表未缴费
 */

var carData = {
    code: 200,//校验码
    count: 10,//每页展示的信息数量
    data: [
        {
            num: "粤A 12345",
            type: "奥迪",
            usertype: "内部",
            intime: new Date(2023, 2, 7, 14, 20),
            outtime: undefined,
            IsOut: 0,
            name: "罗先生",
            phone: "18813178619",
            money: 0,
        },
        {
            num: "粤A 12345",
            type: "丰田",
            usertype: "拜访",
            intime: new Date(2023, 2, 7, 13, 59),
            outtime: undefined,
            IsOut: 0,
            name: "张先生",
            phone: "18813178619",
            money: 0,
        },
        {
            num: "粤A 13345",
            type: "大众",
            usertype: "内部",
            intime: new Date(2023, 2, 7, 13, 20),
            outtime: new Date(2023, 2, 7, 14, 59),
            IsOut: 1,
            name: "刘先生",
            phone: "18813178611",
            money: 30,
        },
        {
            num: "粤A 12345",
            type: "尼桑",
            usertype: "拜访",
            intime: new Date(2023, 2, 7, 10, 20),
            outtime: new Date(2023, 2, 7, 12, 20),
            IsOut: 1,
            name: "张先生",
            phone: "18813178611",
            money: 30,
        },
        {
            num: "粤A 12345",
            type: "本田",
            usertype: "拜访",
            intime: new Date(2023, 2, 6, 10, 20),
            outtime: new Date(2023, 2, 6, 12, 20),
            IsOut: 1,
            name: "张先生",
            phone: "18813178611",
            money: 30,
        },
        {
            num: "粤A 12345",
            type: "宝马",
            usertype: "拜访",
            intime: new Date(2023, 2, 6, 9, 20),
            outtime: new Date(2023, 2, 6, 12, 20),
            IsOut: 1,
            name: "王女士",
            phone: "18813178611",
            money: 50,
        },
        {
            num: "粤A 12345",
            type: "尼桑",
            usertype: "内部",
            intime: new Date(2023, 2, 6, 7, 20),
            outtime: new Date(2023, 2, 6, 13, 20),
            IsOut: 1,
            name: "张先生",
            phone: "18813178611",
            money: 50,
        },
        {
            num: "粤A 12345",
            type: "尼桑",
            usertype: "拜访",
            intime: new Date(2023, 2, 6, 10, 20),
            outtime: new Date(2023, 2, 6, 12, 20),
            IsOut: 1,
            name: "张先生",
            phone: "18813178611",
            money: 30,
        },
        {
            num: "粤A 12345",
            type: "奔驰",
            usertype: "内部",
            intime: new Date(2023, 2, 5, 10, 20),
            outtime: new Date(2023, 2, 5, 12, 20),
            IsOut: 1,
            name: "史先生",
            phone: "18813178611",
            money: 30,
        },
        {
            num: "粤A 12345",
            type: "玛莎拉蒂",
            usertype: "内部",
            intime: new Date(2023, 2, 5, 9, 20),
            outtime: new Date(2023, 2, 5, 12, 20),
            IsOut: 1,
            name: "肖女士",
            phone: "18813178611",
            money: 40,
        },
        {
            num: "粤A 12345",
            type: "兰博基尼",
            usertype: "内部",
            intime: new Date(2023, 2, 4, 10, 20),
            outtime: new Date(2023, 2, 4, 12, 20),
            IsOut: 1,
            name: "杨先生",
            phone: "18813178659",
            money: 30,
        }

    ]
}