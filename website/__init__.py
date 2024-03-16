from flask import Flask
from flask import Flask
from flask_session import Session
from redis import Redis
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = '_5#y2L"F4Q8z\]/'
    
    # Configure your PostgreSQL database connection
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = Redis(host='localhost', port=6379)
    Session(app)

    app.permanent_session_lifetime = timedelta(minutes=60)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
