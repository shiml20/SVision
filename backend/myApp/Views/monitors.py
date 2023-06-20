
from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import monitors  # 导入模型

monitor_bp = Blueprint('monitors', __name__, url_prefix='/monitors')


@monitor_bp.route('/', methods=['GET'])
def get_monitors():
    data = request.json
    query_res = monitors.query.filter()
    query_res = query_res.order_by(desc(monitors.number))
    items = [item.jsondata() for item in query_res.all()]
    total = query_res.count()
    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'resources': items
    }


@monitor_bp.route('/search', methods=['POST'])
def search_monitors():
    data = request.json
    query_res = monitors.query.filter()
    query_res = query_res.order_by(desc(monitors.number))
    items = [item.jsondata() for item in query_res.all()]
    total = query_res.count()
    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'resources': items
    }

@monitor_bp.route('/', methods=['DELETE'])
def delete_monitors():
    data = request.json
    list_to_del = data.get('list_to_del')
    for id in list_to_del:
        item = monitors.query.filter_by(id=id).first()
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@monitor_bp.route('/', methods=['POST'])
def add_monitor():
    data = request.json

    number = data.get('number')
    quantity = data.get('quantity')
    usedyears = data.get('usedyears')
    monitorplace = data.get('monitorplace')
    fixedtime = str2time(data.get('fixedtime'))

    mon = monitors(number=number, quantity=quantity,
                   usedyears=usedyears, monitorplace=monitorplace,
                   fixedtime=fixedtime)
    db.session.add(mon)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@monitor_bp.route('/<int:id>', methods=['PUT'])
def edit_monitor(id):
    data = request.json
    mon = monitors.query.get(id)
    if mon is None:
        return {
            'status': 'fail',
            'message': 'NO_MONITOR'
        }

    mon.number = data.get('number')
    mon.quantity = data.get('quantity')
    mon.usedyears = data.get('usedyears')
    mon.monitorplace = data.get('monitorplace')
    mon.fixedtime = str2time(data.get('fixedtime'))

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@monitor_bp.route('/<int:id>', methods=['DELETE'])
def delete_monitor(id):
    mon = monitors.query.get(id)
    if mon is None:
        return {
            'status': 'fail',
            'message': 'NO_MONITOR'
        }

    db.session.delete(mon)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }
