import pymongo
from pymongo import mongo_client
from Sensor.constant.database import DATABASE_NAME
import certifi
import os
from Sensor.constant.env_variable import MONGODB_URL_KEY
from Sensor.exception import SensorException


ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
        '''

        self.client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"),tlsCAFile=ca)
        self.db_name=DATABASE_NAME

      '''   
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            

        except Exception as e:
            raise e
            
       

        
''' original code: 
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("MONGODB_URL_KEY")
                if MongoDBClient.client is None:
                    #raise Exception(f"Environment key: {mongo_db_url} is not set")
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client(database_name)
            self.database_name = DATABASE_NAME

        except Exception as e:
            raise e


'''