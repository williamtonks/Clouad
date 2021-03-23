from flask import Flask, request, jsonify, abort
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
import subprocess
app = Flask(__name__)

temps = [{'title': u'current temp', 'temp': 34},{'title': u'setpoint', 'temp': 32}]

@app.route('/ThermsAreUs/api/v1.0/current-temp', methods = ['GET'])
def current_temp():
   if request.method == 'GET':
      return jsonify({'current_temp': temps[0]['temp']})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods = ['GET', 'PUT'])
def get_setpoint():
   if request.method == 'GET':
      return jsonify({'setpoint': temps[1]['temp']})
   if request.method == 'PUT':
      if not request.json:
         abort(400)
      if 'setpoint' not in request.json:
         abort(404)
      temps[1]['temp'] = request.json['setpoint']
      return jsonify({'setpoint': temps[1]['temp']})

if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")
