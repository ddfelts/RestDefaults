import json
from flask import Blueprint, request, jsonify
from lib.utils.defaults import rtSuccess,rtError

cmdbapi = Blueprint('cmdbapi',__name__)
#updatedata
schema = ["id","group","hname","ipadd","stype","os","os_version","sn","owner"]

@cmdbapi.route('/',methods=['GET'])
def cmdball():
    d = rtSuccess("Tester")
    return jsonify(d)

@cmdbapi.route('/<int:id>',methods=['GET'])
def cmdbget(id):
    if isinstance(id,int):
        return jsonify(rtSuccess("ID added"))
    else:            
        return jsonify(rtError("ID not in database"))

@cmdbapi.route('/add',methods=['POST'])
def cmdbadd():
    d = request.json
    for i in d.keys():
        if i not in schema:
            return jsonify(rtError("Wrong Keys in json post request"))        
    f = rtSuccess(d)
    return jsonify(f)

@cmdbapi.route('/delete/<int:id>',methods=['DELETE'])
def cmdbdelete(id):
    return jsonify(rtSuccess(""))

@cmdbapi.route('/update',methods=['POST'])
def cmdbupdate():
    d = request.json
    for i in d.keys():
        if i not in schema:
            return jsonify(rtError("Wrong Keys in json post request"))
    d = rtSuccess("")
    return jsonify(d)

@cmdbapi.route('/search',methods=['POST'])
def cmdbsearch():
    d = request.json
    for i in d.keys():
        if i not in schema:
            return jsonify(rtError("Wrong Keys in json post request"))
    d = rtSuccess("")
    return jsonify(d)
