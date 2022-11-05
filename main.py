from Sensor.configuration.mongoDB_connection import MongoDBClient
import pymongo
import os, sys
from Sensor.constant import training_pipeline
from Sensor.exception import SensorException
from Sensor.logger import logging
# from Sensor.entity.config_entity import TrainPipelineConfig,DataIngestionConfig
from Sensor.pipeline import training_pipeline
from Sensor.pipeline.training_pipeline import TrainPipeline
from Sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig

if __name__=='__main__':

    try:

        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        #print(e)
        logging.exception(e)

    
    #training_pipeline_config = TrainingPipelineConfig()
    #data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    #print(data_ingestion_config.__dict__)




'''
def test_exception():
    try:
        logging.info("Dividing number by Zero for testing")
        1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__=='__main__':

    try:
        test_exception()
    except Exception as e:
        print(e)



   # mongodb_client = MongoDBClient()
   # db = mongodb_client.db_name

#client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
    

# mydb2 = client["DATABASE_NAME"]

# print("Collections Names: ", mydb2.list_collection_names())
    
    #print("Collection Names: ", mongodb_client.db_name)


    #print(mongodb_client.database.list_collection_names())

'''