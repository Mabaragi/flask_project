from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)
    my_mongo_uri = os.getenv('MY_MONGO_URI')
    client = MongoClient(my_mongo_uri)
    # app인스턴스의 속성으로 db를 저장, 다른 모듈에서 current_app.db로 접근
    app.db = client.temp

    from .views import main_views
    app.register_blueprint(main_views.bp)

    # Flask Shell 컨텍스트 설정
    @app.shell_context_processor
    def make_shell_context():
        return {'app': app, 'db': app.db}

    return app
