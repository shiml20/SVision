"""
fac_bp：设备蓝图
本模块有以下功能：
    A.获取全部设备信息 /
    B.批量删除设备信息 /
    C.新增一个设备信息 /
    D.修改一个设备信息 /<int:id>
    E.删除一个设备信息 /<int:id>
"""

from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import facilities  # 导入模型

fac_bp = Blueprint('facilities', __name__, url_prefix='/facilities')


@fac_bp.route('/', methods=['GET'])
def get_facilities():
    data = request.json
    query_res = facilities.query.filter()
    query_res = query_res.order_by(desc(facilities.number))
    items = [item.jsondata() for item in query_res.all()]
    return {
        'status': 'success',
        'message': 'SEARCH_SUCCESS',
        'resources': items
    }


@fac_bp.route('/search', methods=['POST'])
def search_facilities():
    data = request.json
    query_res = facilities.query.filter()
    query_res = query_res.order_by(desc(facilities.number))
    items = [item.jsondata() for item in query_res.all()]
    return {
        'status': 'success',
        'message': 'SEARCH_SUCCESS',
        'resources': items
    }

@fac_bp.route('/', methods=['DELETE'])
def delete_facilities():
    data = request.json
    list_to_del = data.get('list_to_del')

    for id in list_to_del:
        item = facilities.query.filter_by(id=id).first()
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@fac_bp.route('/', methods=['POST'])
def add_fac():
    data = request.json

    number = data.get('number')
    isfault = data.get('isfault')
    faulttype = data.get('faulttype')
    faultplace = data.get('faultplace')
    faulttime = str2time(data.get('faulttime'))
    issolved = data.get('issolved')
    solvetime = str2time(data.get('solvetime'))

    fac = facilities(number=number, isfault=isfault,
                     faulttype=faulttype, faultplace=faultplace,
                     faulttime=faulttime, issolved=issolved,
                     solvetime=solvetime)

    db.session.add(fac)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@fac_bp.route('/<int:id>', methods=['PUT'])
def edit_fac(id):
    data = request.json
    fac = facilities.query.get(id)
    if fac is None:
        return {
            'status': 'fail',
            'message': 'NO_FAC'
        }
    fac.number = data.get('number')
    fac.isfault = data.get('isfault')
    fac.faulttype = data.get('faulttype')
    fac.faultplace = data.get('faultplace')
    fac.faulttime = str2time(data.get('faulttime'))
    fac.issolved = data.get('issolved')
    fac.solvetime = str2time(data.get('solvetime'))

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@fac_bp.route('/<int:id>', methods=['DELETE'])
def delete_fac(id):
    fac = facilities.query.get(id)
    if fac is None:
        return {
            'status': 'fail',
            'message': 'NO_FAC'
        }

    db.session.delete(fac)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }
