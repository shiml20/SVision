from sqlalchemy import and_, desc
from flask import Blueprint, request

from ..utils import str2time
from ..extensions import db  # 导入数据库
from ..models import log  # 导入模型

log_bp = Blueprint('log', __name__, url_prefix='/log')


@log_bp.route('/search', methods=['POST'])
def search_logs():
    # begin end 起始时间
    # type 紧急程度
    # author 作者
    # title 标题
    # content 内容
    data = request.json
    time_begin = str2time(data.get('time_begin'))
    time_end = str2time(data.get('time_end'))
    type = data.get('type')
    author = data.get('author')
    title = data.get('title')
    content = data.get('content')

    page_num = data.get('page_num')
    per_page = data.get('per_page')

    if not page_num:
        page_num = 1
    if not per_page:
        per_page = 5
    # query_res: query对象，支持后续的’与‘查询
    query_res = log.query.filter()

    # 逻辑判断：
    # 开始时间非空
    if time_begin:
        query_res = query_res.filter(time_begin <= log.time)
    # 结束时间非空
    if time_end:
        query_res = query_res.filter(log.time <= time_end)
    # log类别
    if type:
        query_res = query_res.filter(log.type == type)
    # 作者
    if author:
        query_res = query_res.filter(log.author == author)
    #
    if title:
        query_res = query_res.filter(log.title == title)
    # 内容
    if content:
        query_res = query_res.filter(log.content.contains(content))

    query_res = query_res.order_by(desc(log.time))

    total = 0
    items = []
    pages = 0

    if query_res.count() > 0:
        # 符合条件的条目太少了
        if query_res.count() <= (page_num - 1) * per_page:
            page_num = 1

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



@log_bp.route('/', methods=['DELETE'])
def delete_logs():
    data = request.json
    list_to_del = data.get('list_to_del')
    for id in list_to_del:
        item = log.query.filter_by(id=id).first()
        if item is None:
            continue
        db.session.delete(item)
        db.session.commit()
    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }


@log_bp.route('/', methods=['POST'])
def add_log():
    data = request.json

    title = data.get('title')
    content = data.get('content')
    author = data.get('author')
    time = str2time(data.get('time'))
    type = data.get('type')

    alog = log(title=title, content=content,
               author=author, time=time,
               type=type)

    db.session.add(alog)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'ADD_SUCCESS'
    }


@log_bp.route('/<int:id>', methods=['PUT'])
def edit_log(id):
    data = request.json
    alog = log.query.get(id)
    if alog is None:
        return {
            'status': 'fail',
            'message': 'NO_LOG'
        }

    alog.title = data.get('title')
    alog.content = data.get('content')
    alog.author = data.get('author')
    alog.time = str2time(data.get('time'))
    alog.type = data.get('type')

    db.session.commit()
    return {
        'status': 'success',
        'message': 'UPDATE_SUCCESS'
    }


@log_bp.route('/<int:id>', methods=['DELETE'])
def delete_fac(id):
    alog = log.query.get(id)
    if alog is None:
        return {
            'status': 'fail',
            'message': 'NO_LOG'
        }

    db.session.delete(alog)
    db.session.commit()

    return {
        'status': 'success',
        'message': 'DELETE_SUCCESS'
    }

