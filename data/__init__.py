from flask_mongoengine import MongoEngine

host = 'mongodb://master:master228@ds125068.mlab.com:25068/heroku_wsvtmzmb?retryWrites=false'
app_db_config = {
            'db': 'heroku_wsvtmzmb',
            'host': host
        }


def init_app(app):
    app.config['MONGODB_SETTINGS'] = app_db_config
    db = MongoEngine(app)

