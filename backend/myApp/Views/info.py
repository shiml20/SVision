
from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import info  # 导入模型

info_bp = Blueprint('info', __name__, url_prefix='/info')


@info_bp.route('/', methods=['GET'])
def get_infos():
    data = request.json
    query_res = info.query.filter()
    items = [item.jsondata() for item in query_res.all()]
    return {
        'status': 'success',
        'message': 'SEARCH_SUCCESS',
        'resources': items
    }

@info_bp.route('/search', methods=['POST'])
def search_infos():
    data = request.json
    query_res = info.query.filter()
    items = [item.jsondata() for item in query_res.all()]
    return {
        'status': 'success',
        'message': 'SEARCH_SUCCESS',
        'resources': items
    }


@info_bp.route('/', methods=['DELETE'])
def delete_infos():
    data = request.json
    list_to_del = data.get('list_to_del')
    for id in list_to_del:
        item = info.query.filter_by(id=id).first()
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@info_bp.route('/', methods=['POST'])
def add_info():
    data = request.json
    warninginfo = data.get('warninginfo')
    areainfo = data.get('areainfo')
    securityinfo = data.get('securityinfo')
    otherinfo = data.get('otherinfo')

    inf = info(warninginfo=warninginfo, areainfo=areainfo,
               securityinfo=securityinfo, otherinfo=otherinfo)

    db.session.add(inf)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@info_bp.route('/<int:id>', methods=['PUT'])
def edit_info(id):
    data = request.json
    inf = info.query.get(id)
    if inf is None:
        return {
            'status': 'fail',
            'message': 'NO_INFO'
        }

    inf.warninginfo = data.get('warninginfo')
    inf.areainfo = data.get('areainfo')
    inf.securityinfo = data.get('securityinfo')
    inf.otherinfo = data.get('otherinfo')

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@info_bp.route('/<int:id>', methods=['DELETE'])
def delete_fac(id):
    inf = info.query.get(id)
    if inf is None:
        return {
            'status': 'fail',
            'message': 'NO_INFO'
        }

    db.session.delete(inf)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }
