from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import warnings  # 导入模型

warn_bp = Blueprint('warnings', __name__, url_prefix='/warnings')


@warn_bp.route('/', methods=['GET'])
def get_warnings():
    data = request.json

    query_res = warnings.query.filter()

    query_res = query_res.order_by(desc(warnings.warntime))
    items = [item.jsondata() for item in query_res.all()]
    total = query_res.count()
    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'resources': items
    }


@warn_bp.route('/', methods=['DELETE'])
def delete_warnings():
    data = request.json

    list_to_del = data.get('list_to_del')
    # 执行批量删除
    for id in list_to_del:
        item = warnings.query.filter_by(id=id).first()

        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@warn_bp.route('/', methods=['POST'])
def add_warning():
    """新增一个车辆信息"""
    data = request.json

    warntype = data.get('warntype')
    iswarn = data.get('iswarn')
    warnplace = data.get('warnplace')
    warntime = str2time(data.get('warntime'))
    issolved = data.get('issolved')
    solvetime = str2time(data.get('solvetime'))

    warning = warnings(warntype=warntype, iswarn=iswarn,
                       warnplace=warnplace, warntime=warntime,
                       issolved=issolved, solvetime=solvetime)

    db.session.add(warning)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@warn_bp.route('/<int:id>', methods=['PUT'])
def edit_warning(id):

    data = request.json
    warn = warnings.query.get(id)
    if warn is None:
        return {
            'status': 'fail',
            'message': 'NO_WARNING'
        }

    warn.warntype = data.get('warntype')
    warn.iswarn = data.get('iswarn')
    warn.warnplace = data.get('warnplace')
    warn.warntime = str2time(data.get('warntime'))
    warn.issolved = data.get('issolved')
    warn.solvetime = str2time(data.get('solvetime'))

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@warn_bp.route('/<int:id>', methods=['DELETE'])
def delete_warning(id):
    warn = warnings.query.get(id)
    if warn is None:
        return {
            'status': 'fail',
            'message': 'NO_WARNING'
        }

    db.session.delete(warn)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }
