"""
usr_bp：用户蓝图
本模块有以下功能：
    A.根据search的字段获取符合条件的所有用户 /
    B.批量删除用户信息 /
    C.新增一个用户信息 /
    D.修改一个用户信息 /<int:id>
    E.删除一个用户信息 /<int:id>
"""

from sqlalchemy import or_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import users  # 导入模型

usr_bp = Blueprint('users', __name__, url_prefix='/users')



@usr_bp.route('/', methods=['GET'])
def get_users():
    """根据search的字段获取所有用户"""
    data = request.json
    # 部门、角色类型、用户名/姓名
    department = data.get('department')
    _type = data.get('type')
    name = data.get('name')
    # 页面参数
    page_num = data.get('page_num')
    per_page = data.get('per_page')

    # query_res: query对象，支持后续的’与‘查询
    query_res = users.query.filter()

    # 逻辑判断：
    # 部门非空
    if department:
        query_res = query_res.filter(users.department == department)

    # 角色类型非空
    if _type:
        query_res = query_res.filter(users.type == _type)

    # 用户名/姓名非空
    if name:
        query_res = query_res.filter(or_(users.realname == name, users.username == name))

    query_res = query_res.order_by(desc(users.createtime))

    total = 0
    items = []
    pages = 0

    if query_res.count() > 0:
        # 根据创建时间，
        # 符合条件的条目太少了
        if query_res.count() <= (page_num - 1) * per_page:
            page_num = 1

        # 每页显示per_page条信息
        # 返回paginate对象，此对象用于分页
        pagination = query_res.paginate(page=page_num, per_page=per_page)
        print(type(pagination))
        # pagination.items 返回一个列表，列表元素为users对象
        items = [item.jsondata() for item in pagination.items]
        total = pagination.total
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


@usr_bp.route('/', methods=['DELETE'])
def delete_users():
    """批量删除用户"""
    data = request.json
    # list_to_del
    list_to_del = data.get('list_to_del')
    # 执行批量删除
    for id in list_to_del:
        item = users.query.filter_by(id=id).first()
        # 忽略所要删的用户不存在的情况
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@usr_bp.route('/', methods=['POST'])
def add_user():
    """新增一个用户信息"""
    data = request.json

    realname = data.get('realname')
    username = data.get('username')

    if users.query.filter_by(username=username).first():
        return {
            'status': 'fail',
            'message': 'USERNAME_EXIST'
        }

    password = data.get('password')
    type = data.get('type')
    department = data.get('department')
    isused = data.get('isused')
    createtime = str2time(data.get('createtime'))
    isfaceused = data.get('isfaceused')

    usr = users(realname=realname, username=username,
                password=password,
                type=type, department=department,
                isused=isused, createtime=createtime,
                isfaceused=isfaceused)

    db.session.add(usr)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@usr_bp.route('/<int:id>', methods=['PUT'])
def edit_user(id):
    """修改一个用户信息"""
    data = request.json
    usr = users.query.get(id)
    if usr is None:
        return {
            'status': 'fail',
            'message': 'NO_USER'
        }

    usr.realname = data.get('realname')

    username = data.get('username')
    if users.query.filter_by(username=username).first():
        return {
            'status': 'fail',
            'message': 'USERNAME_EXIST'
        }

    usr.username = username
    usr.password = data.get('password')
    usr.type = data.get('type')
    usr.department = data.get('department')
    usr.isused = data.get('isused')
    usr.createtime = str2time(data.get('createtime'))
    usr.isfaceused = data.get('isfaceused')

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@usr_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    """删除一个用户信息"""
    usr = users.query.get(id)
    if usr is None:
        return {
            'status': 'fail',
            'message': 'NO_USER'
        }

    db.session.delete(usr)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }
