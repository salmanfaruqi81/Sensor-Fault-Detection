from Sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from Sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig
from Sensor.exception import SensorException
import sys, os
from Sensor.logger import logging
from Sensor.components.data_ingestion import DataIngestion
from Sensor.components.data_validation import DataValidation

class TrainPipeline:

    def __init__(self):
        training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)

        self.training_pipeline_config = training_pipeline_config


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact =  data_ingestion.initiate_data_ingestion()               
            logging.info(f"Data Ingestion Completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline Class")

        try: #2:27
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )
            data_validation_artifact =  data_validation.initiate_data_validation()
            logging.info("Performed the Data Validation Operation")

            logging.info("Exited the start_data_validation method of Pipeline")
            #return data_validation_artifact
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
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()

            data_validation_artifact =  self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)
            
        
        except Exception as e:
            raise SensorException(e,sys)

