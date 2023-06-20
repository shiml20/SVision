from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import warehouses  # 导入模型

warehouse_bp = Blueprint('warehouse', __name__, url_prefix='/warehouse')


@warehouse_bp.route('/', methods=['GET'])
def get_warehouses():
    data = request.json

    query_res = warehouses.query.filter()

    query_res = query_res.order_by(desc(warehouses.number))
    items = [item.jsondata() for item in query_res.all()]
    total = query_res.count()
    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'resources': items
    }

@warehouse_bp.route('/', methods=['POST'])
def search_warehouses():
    data = request.json

    query_res = warehouses.query.filter()

    query_res = query_res.order_by(desc(warehouses.number))
    items = [item.jsondata() for item in query_res.all()]
    total = query_res.count()
    return {
        'status': 'success',
        'msg': 'SEARCH_SUCCESS',
        'resources': items
    }

@warehouse_bp.route('/', methods=['DELETE'])
def delete_warehouses():
    data = request.json
    list_to_del = data.get('list_to_del')
    # 执行批量删除
    for id in list_to_del:
        item = warehouses.query.filter_by(id=id).first()
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@warehouse_bp.route('/', methods=['POST'])
def add_warehouse():
    data = request.json

    number = data.get('number')
    capicity = data.get('capicity')
    used = data.get('used')

    warehouse = warehouses(number=number, capicity=capicity,
                           used=used)

    db.session.add(warehouse)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@warehouse_bp.route('/<int:id>', methods=['PUT'])
def edit_warehouse(id):
    data = request.json
    warehouse = warehouses.query.get(id)
    if warehouse is None:
        return {
            'status': 'fail',
            'message': 'NO_WAREHOUSE'
        }

    warehouse.number = data.get('number')
    warehouse.capicity = data.get('capicity')
    warehouse.used = data.get('used')

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@warehouse_bp.route('/<int:id>', methods=['DELETE'])
def delete_warehouse(id):

    warehouse = warehouses.query.get(id)
    if warehouse is None:
        return {
            'status': 'fail',
            'message': 'NO_WAREHOUSE'
        }

    db.session.delete(warehouse)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }
