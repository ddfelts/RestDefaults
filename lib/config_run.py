import os
import config
import json
from flask import Flask,jsonify

#Begin Import of API blueprints
from api.cmdb.controller import cmdbapi
#End Import of API blueprints

app = Flask(__name__,
            instance_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),'insance'),
            instance_relative_config=True)

#Register Blueprint Endpoints for API
app.register_blueprint(cmdbapi,url_prefix="/cmdb")
#End Register Blueprint Endpints for API

@app.errorhandler(404)
def not_found(error):
    data = {"status":"error",
            "code":"404",
            "msg":"end point not found"}
    return jsonify(json.dumps(data))

@app.errorhandler(500)
def error_page(error):
    data = {"status":"error",
            "code":"500",
            "msg":"web error found"}
    return jsonify(json.dumps(data))

