#!flask/bin/python
from flask import Flask
from flask import request
from data import data_node as node
import data

app = Flask(__name__)
data.init_app(app)


@app.route('/api/v1.0/current')
def current():
    return node.get_current_weather(request.args)


@app.route('/api/v1.0/forecast')
def forecast():
    return node.get_forecast_weather(request.args)


app.run(debug=True)
