from flask import Flask, jsonify, abort, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
#from flask_restless import APIManager
#from flask_restful import Api

#api = Api(app)
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import models

@app.route('/dev/<string:id>/')
def get_dev(id):
    return jsonify({'dev': iotDevice.query.get(id)})

@app.route('/dev/iotDevice/', methods = ['POST'])
def create_dev():
    if not request.json or not 'uName' in request.json:
        abort(400)
    print(request.json['deviceNum'])
    dev = models.iotDevice(request.json['uName'], request.json['deviceNum'])
    devBackup = models.iotDeviceBackup(request.json['uName'], request.json['deviceNum'])
    db.session.add(dev)
    db.session.add(devBackup)
    db.session.commit()
    devAdded = models.iotDevice.query.filter_by(userName=dev.userName).first()
    return jsonify( { 'iotDevice': devAdded.deviceNum }) , 201

if __name__ == '__main__':
        app.run(debug = True)
