#!flask/bin/python
from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
from flask_backend.data import data_node as node
import flask_backend.data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../res'
data.init_app(app)


@app.route('/api/v1.0/current')
def current():
    return node.get_current_weather(request.args).to_json()


@app.route('/api/v1.0/forecast')
def forecast():
    return node.get_forecast_weather(request.args).to_json()


@app.route('/loadfile/<filename>')
def uploaded_file(filename):
    image = send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    return image


@app.route('/<city>')
def index(city=None):
    c = node.get_current_weather({'q': city}).to_json()
    f = node.get_forecast_weather({'q': city}).to_json()
    return render_template('index.html', current=c, forecast=f)


