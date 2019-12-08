#!flask/bin/python
from flask import Flask
from flask import request
from flask import send_from_directory
from flask_cors import CORS, cross_origin
from flask_backend.data import data_node as node

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../res'
CORS(app)
data.init_app(app)


@app.route('/api/v1.0/current')
@crossdomain(origin='*')
def current():
    return node.get_current_weather(request.args).to_json()


@app.route('/api/v1.0/forecast')
@crossdomain(origin='*')
def forecast():
    return node.get_forecast_weather(request.args).to_json()


@app.route('/loadfile/<filename>')
@crossdomain(origin='*')
def uploaded_file(filename):
    image = send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return image


