from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)
    my_mongo_uri = os.getenv('MY_MONGO_URI')
    client = MongoClient(my_mongo_uri)
    # app�ν��Ͻ��� �Ӽ����� db�� ����, �ٸ� ��⿡�� current_app.db�� ����
    app.db = client.temp

    from .views import main_views
    app.register_blueprint(main_views.bp)
    return app
