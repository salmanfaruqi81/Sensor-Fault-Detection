from Sensor.exception import SensorException
from Sensor.logger import logging
from Sensor.entity.artifact_entity import ModelTrainerArtifact, ModelPusherArtifact, ModelEvaluationArtifact
from Sensor.entity.config_entity import ModelEvaluationConfig
import os, sys
from Sensor.ml.metric.classification_metric import get_classification_score
from Sensor.ml.model.estimator import SensorModel
from Sensor.utils.main_utils import save_object, load_object, write_yaml_file
from Sensor.ml.model.estimator import ModelResolver
import shutil


class ModelPusher:

    def __init__(self, model_pusher_config:ModelPusherArtifact,model_eval_artifact:ModelEvaluationArtifact):
        
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact

        except Exception as e:
            raise SensorException(e,sys)


    def initiate_model_pusher(self,) -> ModelPusherArtifact:
        try:
            trained_model_path = self.model_eval_artifact.trained_model_path

            # Creating Model Pusher Directory to Save model
            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)

            shutil.copy(src=trained_model_path, dst=model_file_path)

            # Saved Model Dir
            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            # Prepare Artifact:
            model_pusher_artifact = ModelPusherArtifact(saved_model_path=saved_model_path, model_file_path=model_file_path)
            return model_pusher_artifact

        except Exception as e:
            raise SensorException(e,sys)
    


