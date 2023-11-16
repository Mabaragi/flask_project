from pymongo import MongoClient
import os


class Database:
    def __init__(self) -> None:
        client = MongoClient(os.getenv('MONGO_URI'))
        self.db = client['flask-project']

    def get_collection(self, collection_name):
        return self.db[collection_name]

# 데이터베이스 인스턴스 생성
db=Database()

