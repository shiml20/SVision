from myApp.extensions import db
from .utils import time2str


class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    realname = db.Column("realname", db.String(100))
    username = db.Column("username", db.String(100), unique=True)
    password = db.Column("password", db.String(100))
    type = db.Column("type", db.String(100))
    department = db.Column("department", db.String(100))
    isused = db.Column("isused", db.Boolean)
    createtime = db.Column("createtime", db.DateTime)
    isfaceused = db.Column("isfaceused", db.Boolean)

    def __init__(self, realname, username, password, type, department, isused, createtime, isfaceused):
        self.realname = realname
        self.username = username
        self.password = password
        self.type = type
        self.department = department
        self.isused = isused
        self.createtime = createtime
        self.isfaceused = isfaceused

    def jsondata(self):
        _jsondata = {
            'id': self.id,
            'realname': self.realname,
            'username': self.username,
            'type': self.type,
            'department': self.department,
            'isused': self.isused,
            'createtime': time2str(self.createtime),
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
            'id': self.id,
            'license': self.license,
            'type': self.type,
            'whyin': self.whyin,
            'isin': self.isin,
            'intime': time2str(self.intime),
            'outtime': time2str(self.outtime),
            'ownername': self.ownername,
            'phone': self.phone,
            'pay': self.pay
        }
        return _jsondata

    @staticmethod
    def get_flow_in(begin, end):
        time_begin = begin
        time_end = end
        query_res = vehicles.query.filter()
        if time_begin:
            query_res = query_res.filter(time_begin <= vehicles.intime)
        if time_end:
            query_res = query_res.filter(vehicles.intime <= time_end)

        count = query_res.count()
        return count

    @staticmethod
    def get_flow_out(begin, end):
        time_begin = begin
        time_end = end
        query_res = vehicles.query.filter(vehicles.isin == False)
        if time_begin:
            query_res = query_res.filter(time_begin <= vehicles.outtime)
        if time_end:
            query_res = query_res.filter(vehicles.outtime <= time_end)
        count = query_res.count()
        return count


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
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'whyin': self.whyin,
            'isin': self.isin,
            'intime': time2str(self.intime),
            'outtime': time2str(self.outtime),
            'visitplace': self.visitplace,
            'company': self.company,
        }
        return _jsondata

    @staticmethod
    def get_flow_in(begin, end):
        time_begin = begin
        time_end = end
        query_res = visitors.query.filter()
        if time_begin:
            query_res = query_res.filter(time_begin <= visitors.intime)
        if time_end:
            query_res = query_res.filter(visitors.intime <= time_end)

        count = query_res.count()
        return count

    @staticmethod
    def get_flow_out(begin, end):
        time_begin = begin
        time_end = end
        query_res = vehicles.query.filter(visitors.isin == False)
        if time_begin:
            query_res = query_res.filter(time_begin <= visitors.outtime)
        if time_end:
            query_res = query_res.filter(visitors.outtime <= time_end)
        count = query_res.count()
        return count


class facilities(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    number = db.Column("number", db.String(100))
    isfault = db.Column("isfault", db.Boolean)
    faulttype = db.Column("faulttype", db.String(100))
    faultplace = db.Column("faultplace", db.String(100))
    faulttime = db.Column("faulttime", db.DateTime)
    issolved = db.Column("issolved", db.Boolean)
    solvetime = db.Column("solvetime", db.DateTime)

    def __init__(self, number, isfault, faulttype, faultplace, faulttime, issolved, solvetime):
        self.number = number
        self.isfault = isfault
        self.faulttype = faulttype
        self.faultplace = faultplace
        self.faulttime = faulttime
        self.issolved = issolved
        self.solvetime = solvetime

    def jsondata(self):
        _jsondata = {
            'id': self.id,
            'number': self.number,
            'isfault': self.isfault,
            'faulttype': self.faulttype,
            'faulttime': time2str(self.faulttime),
            'issolved': self.issolved,
            'solvetime': time2str(self.solvetime),
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
            'id': self.id,
            'warntype': self.warntype,
            'iswarn': self.iswarn,
            'warnplace': self.warnplace,
            'warntime': time2str(self.warntime),
            'issolved': self.issolved,
            'solvetime': time2str(self.solvetime),
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
            'id': self.id,
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
            'id': self.id,
            'number': self.number,
            'quantity': self.quantity,
            'usedyears': self.usedyears,
            'monitorplace': self.monitorplace,
            'fixedtime': self.fixedtime
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
            'id': self.id,
            'warninginfo': self.warninginfo,
            'areainfo': self.areainfo,
            'securityinfo': self.securityinfo,
            'otherinfo': self.otherinfo,
        }
        return _jsondata



class log(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(100))
    content = db.Column("content", db.String(1000))
    author = db.Column("author", db.String(100))
    time = db.Column("time", db.DateTime)
    type = db.Column("type", db.String(100))

    def __init__(self, title, content, author, time, type):
        self.title = title
        self.content = content
        self.author = author
        self.time = time
        self.type = type

    def jsondata(self):
        _jsondata = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'time': time2str(self.time),
            'type': self.type
        }
        return _jsondata