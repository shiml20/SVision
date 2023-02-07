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

var peopleData = {
    code: 200,//校验码
    count: 10,//每页信息个数
    data: [
        {
            num: "王先生",
            phone: "12345678901",
            type: 1,
            com: "Svision",
            dep: "",
            intime: new Date(2023, 2, 7, 14, 23),
            outtime: undefined,
            IsOut: 0,
        },
        {
            num: "赵先生",
            phone: "10987654321",
            type: 0,
            com: "Acom",
            dep: "保安部",
            intime: new Date(2023, 2, 7, 10, 23),
            outtime: new Date(2023, 2, 7, 11, 10),
            IsOut: 1,
        },
        {
            num: "肖女士",
            phone: "12345609871",
            type: 1,
            com: "Svision",
            dep: "",
            intime: new Date(2023, 2, 7, 9, 23),
            outtime: undefined,
            IsOut: 0,
        },
        {
            num: "刘先生",
            phone: "18813178610",
            type: 1,
            com: "Svison",
            dep: "",
            intime: new Date(2023, 2, 7, 9, 10),
            outtime: undefined,
            IsOut: 0,
        },
        {
            num: "张先生",
            phone: "19032132103",
            type: 0,
            com: "Bcom",
            dep: "人事部",
            intime: new Date(2023, 2, 7, 10, 23),
            outtime: undefined,
            IsOut: 0,
        },
        {
            num: "罗先生",
            phone: "13141314123",
            type: 1,
            com: "Svision",
            dep: "",
            intime: new Date(2023, 2, 7, 8, 23),
            outtime: new Date(2023, 2, 7, 10, 23),
            IsOut: 1,
        },
        {
            num: "杨先生",
            phone: "12391031290",
            type: 1,
            com: "Svision",
            dep: "",
            intime: new Date(2023, 2, 7, 8, 23),
            outtime: undefined,
            IsOut: 0,
        },
        {
            num: "张先生",
            phone: "1231293011",
            type: 0,
            com: "Ccom",
            dep: "财务部",
            intime: new Date(2023, 2, 6, 10, 23),
            outtime: new Date(203, 2, 6, 11, 10),
            IsOut: 1,
        },
        {
            num: "吴先生",
            phone: "12345678901",
            type: 0,
            com: "Dcom",
            dep: "宣传部",
            intime: new Date(2023, 2, 6, 9, 23),
            outtime: new Date(2023, 2, 6, 14, 20),
            IsOut: 1,
        },
        {
            num: "胡女士",
            phone: "12309302141",
            type: 0,
            com: "Svision",
            dep: "",
            intime: new Date(2023, 2, 6, 8, 23),
            outtime: new Date(2023, 2, 6, 15, 30),
            IsOut: 1,
        },
        {
            num: "王先生",
            phone: "1132190391",
            type: 1,
            com: "Evision",
            dep: "研发部",
            intime: new Date(2023, 2, 5, 14, 23),
            outtime: new Date(2023, 2, 5, 21, 59),
            IsOut: 1,
        },
        {
            num: "许先生",
            phone: "12345678901",
            type: 1,
            com: "Pcom",
            dep: "环卫部",
            intime: new Date(2023, 2, 4, 10, 23),
            outtime: new Date(2023, 2, 4, 11, 25),
            IsOut: 1,
        }
    ]
}