#!flask/bin/python
from flask import Flask
from flask import request
from flask import render_template
from flask_backend.data import data_node as node
from flask import jsonify
import flask_backend.data

app = Flask(__name__)
data.init_app(app)


@app.route('/api/v1.0/current')
def current():
    return jsonify(node.get_current_weather(request.args))


@app.route('/api/v1.0/forecast')
def forecast():
    return jsonify(node.get_forecast_weather(request.args))


@app.route('/<city>')
def index(city=None):
    c = node.get_current_weather({'q': city}).to_json()
    f = node.get_forecast_weather({'q': city}).to_json()
    return render_template('index.html', current=c, forecast=f)


