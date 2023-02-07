#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from manage import app, db, users, info, facilities, monitors, vehicles, warehouses, warnings, visitors



#  
# 
# 
#  
# 


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/open', methods=['GET'])
def open_door():
    return jsonify(u'芝麻开门！')

RESOURCES = []

@app.route('/vehicles', methods=['GET', 'POST'])
def all_res():
    alldata = vehicles.query.all()
    RESOURCES = []
    for d in alldata:
        d.intime = d.intime.strftime('%Y-%m-%d %H:%M:%S')
        d.outtime = d.outtime.strftime('%Y-%m-%d %H:%M:%S')
        RESOURCES.append(d.jsondata())

    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        dt = datetime.strptime(post_data.get('intime'),'%Y-%m-%d %H:%M:%S')

        license = post_data.get('license')
        for r in RESOURCES:
            if r['license'] == license:
                response_object = {'status': 'failed'}
                response_object['message'] = 'ADD_FAILED'
                break
        else:
            temp = {
                'license': post_data.get('license'),
                'type': post_data.get('type'),
                'whyin': post_data.get('whyin'),
                'isin': post_data.get('isin'),
                'intime': dt,
                'outtime': dt,
                'ownername': post_data.get('ownername'),
                'phone': post_data.get('phome'),
                'pay': post_data.get('pay')
            }
            RESOURCES.append(temp)
            response_object['message'] = 'ADD_SUCCESS'
            adder = vehicles(
                temp['license'],
                temp['type'],
                temp['whyin'],
                temp['isin'],
                temp['intime'],
                temp['outtime'],
                temp['ownername'],
                temp['phone'],
                temp['pay'])
            db.session.add(adder)
            db.session.commit()
        # for/else 结构
    else:
        response_object['resources'] = RESOURCES
    return jsonify(response_object)


def remove_res(lin):
    alldata = vehicles.query.all()
    RESOURCES = []
    for d in alldata:
        RESOURCES.append(d.jsondata())
    print("sss")
    for r in RESOURCES:
        if r['license'] == lin:
            RESOURCES.remove(r)
            adder = vehicles.query.filter_by(license=lin).first()
            db.session.delete(adder)
            db.session.commit()
            return True
    return False

@app.route('/vehicles/<license>', methods=['PUT', "DELETE"])
def single_res(license):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        if remove_res(license):
            response_object['message'] = "UPDATE_SUCCESS"
        else:
            response_object['message'] = "ADD_SUCCESS"
        temp = {
            'license': post_data.get('license'),
            'type': post_data.get('type'),
            'whyin': post_data.get('whyin'),
            'isin': post_data.get('isin'),
            'intime': post_data.get('intime'),
            'outtime': post_data.get('outtime'),
            'ownername': post_data.get('ownername'),
            'phone': post_data.get('phome'),
            'pay': post_data.get('pay')
        }
        RESOURCES.append(temp)        
        adder = vehicles(
            temp['license'],
            temp['type'],
            temp['whyin'],
            temp['isin'],
            temp['intime'],
            temp['outtime'],
            temp['ownername'],
            temp['phone'],
            temp['pay'])
        db.session.add(adder)
        db.session.commit()
    elif request.method == 'DELETE':
        if remove_res(license):
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