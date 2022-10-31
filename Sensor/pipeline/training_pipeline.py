from Sensor.entity.artifact_entity import DataIngestionArtifact
from Sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from Sensor.exception import SensorException
import sys, os
from Sensor.logger import logging

class TrainPipeline:

    def __init__(self):
        training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        from Sensor.entity.artifact_entity import DataIngestionArtifact

        self.training_pipeline_config = training_pipeline_config


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Starting Data Ingestion")
            logging.info("Data Ingestion Completed")
        except Exception as e:
            raise SensorException(e, sys)

    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)


    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def run_pipeline(self):
        try:
            data_inigestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e, sys)

