import pymongo
from Sensor.constant.databse import DATABASE_NAME
import certifi
import os

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name) -> None:

        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("MONGODB_URL_KEY")
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {mongo_db_url} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client(database_name)
            self.database_name = DATABASE_NAME

        except Exception as e:
            raise e


