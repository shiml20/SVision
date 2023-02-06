#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create database
db = SQLAlchemy(app)
class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    date = db.Column("date", db.String(100))
    name = db.Column("name", db.String(100))
    address = db.Column("address", db.Boolean)

    def __init__(self, date, name, address):
        self.date = date
        self.name = name
        self.address = address

    def jsondata(self):
        _jsondata = {
            'date': self.date,
            'name': self.name,
            'address': self.address,
        }
        return _jsondata

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/open', methods=['GET'])
def open_door():
    return jsonify(u'芝麻开门！')

RESOURCES = []

@app.route('/resources', methods=['GET', 'POST'])
def all_res():
    alldata = users.query.all()
    RESOURCES = []
    for d in alldata:
        RESOURCES.append(d.jsondata())
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        date = post_data.get('date')
        for r in RESOURCES:
            if r['date'] == date:
                response_object = {'status': 'failed'}
                response_object['message'] = 'ADD_FAILED'
                break
        else:
            RESOURCES.append({
                'date': post_data.get('date'),
                'name': post_data.get('name'),
                'address': post_data.get('address')
            })
            response_object['message'] = 'ADD_SUCCESS'
            adder = users(post_data.get('date'), post_data.get('name'), 
            post_data.get('address'))
            db.session.add(adder)
            db.session.commit()
        # for/else 结构
    else:
        response_object['resources'] = RESOURCES
    return jsonify(response_object)

def remove_res(dat):
    alldata = users.query.all()
    RESOURCES = []
    for d in alldata:
        RESOURCES.append(d.jsondata())
    for r in RESOURCES:
        if r['date'] == dat:
            RESOURCES.remove(r)
            adder = users.query.filter_by(date=dat).first()
            db.session.delete(adder)
            db.session.commit()
            return True
    return False

@app.route('/resources/<date>', methods=['PUT', "DELETE"])
def single_res(date):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        if remove_res(date):
            response_object['message'] = "UPDATE_SUCCESS"
        else:
            response_object['message'] = "ADD_SUCCESS"
        RESOURCES.append({
                'date': post_data.get('date'),
                'name': post_data.get('name'),
                'address': post_data.get('address')
            })
        adder = users(post_data.get('date'), post_data.get('name'), 
            post_data.get('address'))
        db.session.add(adder)
        db.session.commit()
    elif request.method == 'DELETE':
        if remove_res(date):
            response_object['message'] = "DELETE_SUCCESS"
            response_object['status'] = "success"
        else:
            response_object['message'] = "DELETE_FAILED"
            response_object['status'] = "failed"
    return jsonify(response_object)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run()