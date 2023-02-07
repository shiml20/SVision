from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config_map

# 建立数据库
db = SQLAlchemy()

# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str 配置模式的名字 ("develop", "product")
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    return app

# instantiate the app
app = create_app("develop")

class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    realname = db.Column("realname", db.String(100))
    username = db.Column("username", db.String(100))
    type = db.Column("type", db.String(100))
    department = db.Column("department", db.String(100))
    isused = db.Column("isused", db.Boolean)
    createtime = db.Column("createtime", db.DateTime)
    isfaceused = db.Column("isfaceused", db.Boolean)

    def __init__(self, realname, username, type, department, isused, createtime, isfaceused):
        self.realname = realname
        self.username = username
        self.type = type
        self.department = department
        self.isused = isused
        self.createtime = createtime
        self.isfaceused = isfaceused

    def jsondata(self):
        _jsondata = {
            'realname': self.realname,
            'username': self.username,
            'type': self.type,
            'department': self.department,
            'isused': self.isused,
            'createtime': self.createtime,
            'isfaceused': self.isfaceused
        }
        return _jsondata


class vehicles(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    license = db.Column("license", db.String(100))
    type = db.Column("type", db.String(100))
    whyin = db.Column("whyin", db.String(100))
    isin = db.Column("isin", db.Boolean)
    intime = db.Column("intime", db.DateTime)
    outtime = db.Column("outtime", db.DateTime)
    ownername = db.Column("ownername", db.String(100))
    phone = db.Column("phone", db.String(100))
    pay = db.Column("pay", db.Integer)

    def __init__(self, license, type, whyin, isin, intime, outtime, ownername, phone, pay):
        self.license = license
        self.type = type
        self.whyin = whyin
        self.isin = isin
        self.intime = intime
        self.outtime = outtime
        self.ownername = ownername
        self.phone = phone
        self.pay = pay
    def jsondata(self):
        _jsondata = {
            'license': self.license,
            'type': self.type,
            'whyin': self.whyin,
            'isin': self.isin,
            'intime': self.intime,
            'outtime': self.outtime,
            'ownername': self.ownername,
            'phone': self.phone,
            'pay': self.pay
        }
        return _jsondata


class visitors(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    type = db.Column("type", db.String(100))
    whyin = db.Column("whyin", db.String(100))
    isin = db.Column("isin", db.Boolean)
    intime = db.Column("intime", db.DateTime)
    outtime = db.Column("outtime", db.DateTime)
    visitplace = db.Column("visitplace", db.String(100))
    phone = db.Column("phone", db.String(100))
    company = db.Column("company", db.String(100))

    def __init__(self, name, type, whyin, isin, intime, outtime, visitplace, phone, company):
        self.name = name
        self.type = type
        self.whyin = whyin
        self.isin = isin
        self.intime = intime
        self.outtime = outtime
        self.visitplace = visitplace
        self.company = company 
    def jsondata(self):
        _jsondata = {
            'name': self.name,
            'type': self.type,
            'whyin': self.whyin,
            'isin': self.isin,
            'intime': self.intime,
            'outtime': self.outtime,
            'visitplace': self.visitplace,
            'company': self.company,
        }
        return _jsondata

class facilities(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.String(100))
    isfault = db.Column("isfault", db.Boolean)
    faulttype = db.Column("faulttype", db.String(100))
    faultplace = db.Column("faultplace", db.String(100))
    faulttime = db.Column("faulttime", db.DateTime)
    issolved = db.Column("issolved", db.Boolean)
    solvetime = db.Column("solvetime", db.DateTime)

    def __init__(self, number, isfault, faulttype, faulttime, issolved, solvetime):
        self.number = number
        self.isfault = isfault
        self.faulttype = faulttype
        self.faulttime = faulttime
        self.issolved = issolved
        self.solvetime = solvetime

    def jsondata(self):
        _jsondata = {
        'number' : self.number,
        'isfault' : self.isfault,
        'faulttype' : self.faulttype,
        'faulttime' : self.faulttime,
        'issolved' : self.issolved,
        'solvetime' : self.solvetime,
        }
        return _jsondata

class warnings(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    warntype = db.Column("warningtype", db.String(100))
    iswarn = db.Column("iswarn", db.String(100))
    warnplace = db.Column("warnplace", db.String(100))
    warntime = db.Column("warntime", db.DateTime)
    issolved = db.Column("issolved", db.Boolean)
    solvetime = db.Column("solvetime", db.DateTime)

    def __init__(self, warntype, iswarn, warnplace, warntime, issolved, solvetime):
        self.warntype = warntype
        self.iswarn = iswarn
        self.warnplace = warnplace
        self.warntime = warntime
        self.issolved = issolved
        self.solvetime = solvetime

    def jsondata(self):
        _jsondata = {
        'warntype' : self.warntype,
        'iswarn' : self.iswarn,
        'warnplace' : self.warnplace,
        'warntime' : self.warntime,
        'issolved' : self.issolved,
        'solvetime' : self.solvetime,
        }
        return _jsondata


class warehouses(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.String(100))
    capicity = db.Column("capicity", db.Integer)
    used = db.Column("used", db.Integer)

    def __init__(self, number, capicity, used):
        self.number = number
        self.capicity = capicity
        self.used = used

    def jsondata(self):
        _jsondata = {
            'number': self.number,
            'capicity': self.capicity,
            'used': self.used,
        }
        return _jsondata



class monitors(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.String(100))
    quantity = db.Column("quantity", db.Integer)
    usedyears = db.Column("usedyears", db.Integer)
    monitorplace = db.Column("monitorplace", db.String(100))
    fixedtime = db.Column("fixedtime", db.DateTime)

    def __init__(self, number, quantity, usedyears, monitorplace, fixedtime):
        self.number = number
        self.quantity = quantity
        self.usedyears = usedyears
        self.monitorplace = monitorplace
        self.fixedtime = fixedtime

    def jsondata(self):
        _jsondata = {
            'number': self.date,
            'quantity': self.name,
            'usedyears': self.address,
            'monitorplace': self.monitorplace,
            'fixedtime' : self.fixedtime
        }
        return _jsondata



class info(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    warninginfo = db.Column("warninginfo", db.String(1000))
    areainfo = db.Column("areainfo", db.String(1000))
    securityinfo = db.Column("securityinfo", db.String(1000))
    otherinfo = db.Column("otherinfo", db.String(1000))

    def __init__(self, warninginfo, areainfo, securityinfo, otherinfo):
        self.warninginfo = warninginfo
        self.areainfo = areainfo
        self.securityinfo = securityinfo
        self.otherinfo = otherinfo

    def jsondata(self):
        _jsondata = {
            'warninginfo': self.warninginfo,
            'areainfo': self.areainfo,
            'securityinfo': self.securityinfo,
            'otherinfo': self.otherinfo,
        }
        return _jsondata




