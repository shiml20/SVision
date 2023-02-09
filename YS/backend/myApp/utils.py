from datetime import *
from functools import wraps
from flask import session


def str2time(_str):
    try:
        return datetime.strptime(_str, '%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        # _str字符串和给定的转换格式不匹配
        # 或者_str为NoneType
        # 则返回None
        # print(1)
        return None


def time2str(_time):
    try:
        return _time.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        # datetime格式不符合给定的格式，返回空字符串
        return ""


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 判断session是否保存了用户名，保存了即该用户已登录
        user = session.get('user')
        if user:
            return func(*args, **kwargs)
        else:
            # 未登录重定向到登录页面
            return {
                'status': 'fail',
                'msg': 'LOGIN_REQUIRED'
            }

    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 判断session是否保存了用户名，保存了即该用户已登录
        user = session.get('user')
        if user.type == 'admin':
            return func(*args, **kwargs)
        else:
            # 未登录重定向到登录页面
            return {
                'status': 'fail',
                'msg': 'ADMIN_REQUIRED'
            }

    return wrapper
