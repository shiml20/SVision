"""
veh_bp：车辆蓝图
本模块有以下功能：
    A.根据search的字段获取符合条件的所有车辆信息 /
    B.批量删除车辆信息 /
    C.新增一个车辆信息 /
    D.修改一个车辆信息 /<int:id>
    E.删除一个车辆信息 /<int:id>
    F.获取车流量 /flow
    G.获取入营车流量 /flow/in
    H.获取出营车流量 /flow/out
"""

from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..untils import str2time
from ..extensions import db  # 导入数据库
from ..models import vehicles  # 导入模型

veh_bp = Blueprint('vehicles', __name__, url_prefix='/vehicles')


@veh_bp.route('/', methods=['GET'])
def get_vehicles():
    """根据search的字段获取符合条件的所有车辆信息"""
    alldata = vehicles.query.all()
    RESOURCES = []
    for d in alldata:
        RESOURCES.append(d.jsondata())


    data = request.json
    # 开始时间，结束时间，车辆类型，是否在营，车牌号
    time_begin = ''
    time_end = ''
    if data.get('time_begin'):
        time_begin = str2time(data.get('time_begin'))
    if data.get('time_begin'):
        time_end = str2time(data.get('time_end'))
    type = data.get('type')

    """这点有问题，待商讨"""
    isin = data.get('isin')

    license = data.get('license')
    # 页面参数
    page_num = data.get('page_num')
    per_page = data.get('per_page')

    # query_res: query对象，支持后续的’与‘查询
    query_res = vehicles.query.filter()

    # 逻辑判断：
    # 开始时间非空
    if time_begin:
        query_res = query_res.filter(time_begin <= vehicles.intime)
    # 结束时间非空
    if time_end:
        query_res = query_res.filter(vehicles.intime <= time_end)
    # 车辆类型非空
    if type:
        query_res = query_res.filter(vehicles.type == type)
    # 车辆状态非空
    if isin:
        query_res = query_res.filter(vehicles.isin == isin)
    # 访客手机号码非空
    if license:
        query_res = query_res.filter(vehicles.license == license)

    # 根据入营时间降序排列，
    query_res = query_res.order_by(desc(vehicles.intime))

    total = 0
    items = []
    pages = 0
    print(query_res.count())
    if query_res.count() > 0:
        print(111)
        # 符合条件的条目太少了
        if query_res.count() <= (page_num - 1) * per_page:
            page_num = 1

        # 每页显示per_page条信息
        # 返回paginate对象，此对象用于分页
        pagination = query_res.paginate(page=page_num, per_page=per_page)

        # pagination.items 返回一个列表，列表元素为vehicles对象
        items = [item.jsondata() for item in pagination.items]
        total = pagination.total
        # 总页数
        pages = pagination.pages
    print(items)

    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'data': {
            'items': items,
            'total': total,
            'pages': pages,
            'current_page': page_num
        },
        'resources': RESOURCES
    }


@veh_bp.route('/search', methods=['POST'])
def search_vehicles():
    """根据search的字段获取符合条件的所有车辆信息"""
    alldata = vehicles.query.all()
    RESOURCES = []
    for d in alldata:
        RESOURCES.append(d.jsondata())


    data = request.json
    # 开始时间，结束时间，车辆类型，是否在营，车牌号
    time_begin = ''
    time_end = ''
    if data.get('time_begin'):
 
        time_begin = str2time(data.get('time_begin'))
    if data.get('time_end'):
        print(data.get('time_end'))
        time_end = str2time(data.get('time_end'))
    type = data.get('type')


    """这点有问题，待商讨"""
    isin = data.get('isin')

    license = data.get('license')
    # 页面参数
    page_num = data.get('page_num')
    per_page = data.get('per_page')

    # query_res: query对象，支持后续的’与‘查询
    query_res = vehicles.query.filter()

    # 逻辑判断：
    # 开始时间非空
    if time_begin:
        query_res = query_res.filter(time_begin <= vehicles.intime)
    # 结束时间非空
    if time_end:
        print(time_end)
        query_res = query_res.filter(vehicles.intime <= time_end)
    # 车辆类型非空
    if type:
        query_res = query_res.filter(vehicles.type == type)
    # 车辆状态非空
    if isin:
        query_res = query_res.filter(vehicles.isin == isin)
    # 访客手机号码非空
    if license:
        query_res = query_res.filter(vehicles.license == license)

    # 根据入营时间降序排列，
    query_res = query_res.order_by(desc(vehicles.intime))

    total = 0
    items = []
    pages = 0
    print(query_res.count())
    if query_res.count() > 0:
        # 符合条件的条目太少了
        if query_res.count() <= (page_num - 1) * per_page:
            page_num = 1

        # 每页显示per_page条信息
        # 返回paginate对象，此对象用于分页
        pagination = query_res.paginate(page=page_num, per_page=per_page)

        # pagination.items 返回一个列表，列表元素为vehicles对象
        items = [item.jsondata() for item in pagination.items]
        total = pagination.total
        # 总页数
        pages = pagination.pages
    print(items)
    print(pages)
    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'data': {
            'items': items,
            'total': total,
            'pages': pages,
            'current_page': page_num
        },
        'resources': RESOURCES
    }




@veh_bp.route('/', methods=['DELETE'])
def delete_vehicles():
    """批量删除车辆"""
    data = request.json
    # vehicles_to_del: list of vehicle ids
    list_to_del = data.get('list_to_del')
    # 执行批量删除
    for id in list_to_del:
        item = vehicles.query.filter_by(id=id).first()
        # 忽略所要删的车辆不存在的情况
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@veh_bp.route('/', methods=['POST'])
def add_vehicle():
    """新增一个车辆信息"""
    data = request.json
    
    license = data.get('license')
    type = data.get('type')
    whyin = data.get('whyin')
    isin = data.get('isin')
    intime = str2time(data.get('intime'))
    outtime = str2time(data.get('outtime'))
    ownername = data.get('ownername')
    phone = data.get('phone')
    pay = data.get('pay')

    vehicle = vehicles(license=license, type=type,
                       whyin=whyin, isin=isin,
                       intime=intime, outtime=outtime,
                       ownername=ownername, phone=phone,
                       pay=pay)

    db.session.add(vehicle)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@veh_bp.route('/<int:id>', methods=['PUT'])
def edit_vehicle(id):
    """修改一个车辆信息"""
    data = request.json
    vehicle = vehicles.query.get(id)
    if vehicle is None:
        return {
            'status': 'fail',
            'message': 'NO_VEHICLE'
        }

    vehicle.license = data.get('license')
    vehicle.type = data.get('type')
    vehicle.whyin = data.get('whyin')
    vehicle.isin = data.get('isin')
    vehicle.intime = str2time(data.get('intime'))
    vehicle.outtime = str2time(data.get('outtime'))
    vehicle.ownername = data.get('ownername')
    vehicle.phone = data.get('phone')
    vehicle.pay = data.get('pay')

    db.session.commit()
    return {
        'status': 'success',
        'message': 'EDIT_SUCCESS'
    }


@veh_bp.route('/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    """删除一个车辆信息"""
    vehicle = vehicles.query.get(id)
    if vehicle is None:
        return {
            'status': 'fail',
            'message': 'NO_VEHICLE'
        }

    db.session.delete(vehicle)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@veh_bp.route('/flow', methods=['GET'])
def vehicle_flow():
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    count1 = vehicles.get_flow_in(begin=time_begin, end=time_end)
    count2 = vehicles.get_flow_out(begin=time_begin, end=time_end)
    count = count1 + count2
    return {
        'status': 'success',
        'message': 'GET_FLOW_SUCCESS',
        'data': count
    }

@veh_bp.route('/flow/in', methods=['GET'])
def vehicle_flow_in():
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    count = vehicles.get_flow_in(begin=time_begin, end=time_end)
    return {
        'status': 'success',
        'message': 'GET_FLOW_SUCCESS',
        'data': count
    }


@veh_bp.route('/flow/out', methods=['GET'])
def vehicle_flow_out():
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    count = vehicles.get_flow_out(begin=time_begin, end=time_end)
    return {
        'status': 'success',
        'message': 'GET_FLOW_SUCCESS',
        'data': count
    }
