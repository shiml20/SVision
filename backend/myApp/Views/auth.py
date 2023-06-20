"""
auth_bp:权限管理蓝图
本模块有以下功能：
    A.用户登录
    B.用户登出
    后续按需添加：
    C.管理员权限装饰器
"""


from flask import Blueprint, g, session, request
from functools import wraps
from myApp.models import users
from ..utils import login_required
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    if 'user' in session:
        return{
            'status': 'success',
            'msg': 'USER_LOGINED'
        }
    data = request.json
    username = data.get('username')
    print(data)
    password = data.get('password')
    user = users.query.filter(users.username == username).first()
    # 未查询到
    if not user:
        print(111)
        return{
            'status': 'fail',
            'msg': 'NO_USER',
        }
    # 查询到，验证密码
    if password != user.password:
        return {
            'status': 'fail',
            'msg': 'PASSWORD_WRONG',
        }
    # 密码也正确，将用户id放入session中，并返回成功信息
    session.clear()
    session['user_id'] = user.id
    return {
        'status': 'success',
        'msg': 'LOGIN_SUCCESS'
    }


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    session.clear()
    return {
        'status': 'success',
        'msg': 'LOGOUT_SUCCESS'
    }

