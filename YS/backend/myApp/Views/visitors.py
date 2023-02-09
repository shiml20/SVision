"""
vis_bp：访客蓝图
本模块有以下功能：
    A.根据search的字段获取符合条件的所有访客/
    B.批量删除访客信息 /
    C.新增一个访客信息 /
    D.修改一个访客信息 /<int:id>
    E.删除一个访客信息 /<int:id>
    F.获取访客流量 /flow
    G.获取入营访客流量 /flow/in
    H.获取出营访客流量 /flow/out
"""

from sqlalchemy import and_, desc
from flask import Blueprint, request, jsonify

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import visitors  # 导入模型

vis_bp = Blueprint('visitors', __name__, url_prefix='/visitors')


@vis_bp.route('/', methods=['GET'])
def get_visitors():
    """根据search的字段获取符合条件的所有访客"""

    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))

    name = data.get('name')
    phone = data.get('phone')

    type = data.get('type')

    page_num = data.get('page_num')
    per_page = data.get('per_page')

    # query_res: query对象，支持后续的’与‘查询
    query_res = visitors.query.filter()

    # 逻辑判断：
    # 开始时间非空
    if time_begin:
        query_res = query_res.filter(time_begin <= visitors.intime)
    # 结束时间非空
    if time_end:
        query_res = query_res.filter(visitors.intime <= time_end)
    # 访客类型
    if type:
        query_res = query_res.filter(visitors.type == type)
    # 访客姓名
    if name:
        query_res = query_res.filter(visitors.name == name)
    # 访客手机号
    if phone:
        query_res = query_res.filter(visitors.phone == phone)

    # 根据入营时间降序排列，
    query_res = query_res.order_by(desc(visitors.intime))

    total = 0
    items = []
    pages = 0

    if query_res.count() > 0:
        # 符合条件的条目太少了
        while query_res.count() <= (page_num - 1) * per_page:
            page_num = page_num - 1

        # 每页显示per_page条信息
        # 返回paginate对象，此对象用于分页
        pagination = query_res.paginate(page=page_num, per_page=per_page)

        # pagination.items 返回一个列表，列表元素为vehicles对象
        items = [item.jsondata() for item in pagination.items]
        # 总页数
        pages = pagination.pages

    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'resources': {
            'items': items,
            'total': total,
            'pages': pages,
            'current_page': page_num
        }
    }


@vis_bp.route('/', methods=['DELETE'])
def delete_visitors():
    data = request.json
    # vehicles_to_del: list of vehicle ids
    list_to_del = data.get('list_to_del')
    # 执行批量删除
    for id in list_to_del:
        item = visitors.query.filter_by(id=id).first()
        # 忽略所要删的车辆不存在的情况
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@vis_bp.route('/', methods=['POST'])
def add_visitor():
    """新增一个访客信息"""
    data = request.json

    name = data.get('name')
    type = data.get('type')
    whyin = data.get('whyin')
    isin = data.get('isin')
    intime = str2time(data.get('intime'))
    outtime = str2time(data.get('outtime'))
    visitplace = data.get('visitplace')
    phone = data.get('phone')
    company = data.get('company')

    vehicle = visitors(name=name, type=type,
                       whyin=whyin, isin=isin,
                       intime=intime, outtime=outtime,
                       visitplace=visitplace, phone=phone,
                       company=company)

    db.session.add(vehicle)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@vis_bp.route('/<int:id>', methods=['PUT'])
def edit_visitor(id):
    """修改一个访客信息"""
    data = request.json
    visitor = visitors.query.filter_by(id=id).first()
    if visitor is None:
        return {
            'status': 'fail',
            'message': 'NO_VISITOR'
        }

    visitor.name = data.get('license')
    visitor.type = data.get('type')
    visitor.whyin = data.get('whyin')
    visitor.isin = data.get('isin')
    visitor.intime = data.get('intime')
    visitor.outtime = str2time(data.get('outtime'))
    visitor.visitplace = str2time(data.get('visitplace'))
    visitor.phone = data.get('phone')
    visitor.company = data.get('company')

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@vis_bp.route('/<int:id>', methods=['DELETE'])
def delete_visitor(id):
    """删除一个车辆信息"""
    visitor = visitors.query.get(id)
    if visitor is None:
        return {
            'status': 'fail',
            'message': 'NO_VISITOR'
        }

    db.session.delete(visitor)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@vis_bp.route('/flow', methods=['GET'])
def visitor_flow():
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    count1 = visitors.get_flow_in(begin=time_begin, end=time_end)
    count2 = visitors.get_flow_out(begin=time_begin, end=time_end)
    count = count1 + count2
    return {
        'status': 'success',
        'message': 'GET_FLOW_SUCCESS',
        'data': count
    }


@vis_bp.route('/flow/in', methods=['GET'])
def visitor_flow_in():
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    count = visitors.get_flow_in(begin=time_begin, end=time_end)
    return {
        'status': 'success',
        'message': 'GET_FLOW_SUCCESS',
        'data': count
    }


@vis_bp.route('/flow/out', methods=['GET'])
def visitor_flow_out():
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    count = visitors.get_flow_out(begin=time_begin, end=time_end)
    return {
        'status': 'success',
        'message': 'GET_FLOW_SUCCESS',
        'data': count
    }
