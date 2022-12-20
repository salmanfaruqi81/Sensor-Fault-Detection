import numpy as np
import pandas as pd
import os, sys
from imblearn.combine import SMOTETomek
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from Sensor.constant.training_pipeline import TARGET_COLUMN
from Sensor.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact

from Sensor.entity.config_entity import DataTransformationConfig
from Sensor.exception import SensorException
from Sensor.logger import logging
from Sensor.utils.main_utils import save_numpy_array_data, save_object
from Sensor.ml.model.estimator import TargetValueMapping


class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact, data_transformation_config: DataTransformationConfig):

        """
        : param data_validation_artifact: Output reference of data integration artifact stage
        : param data transformation_config: Configuration for data Transformation
        """
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config

        except Exception as e:
            raise SensorException(e,sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e,sys)

    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        logging.info("Getting Data Transformation Object")
        try:
            robust_scaler = RobustScaler()
            simple_imputer = SimpleImputer(strategy="constant", fill_value=0)

            preprocessor = Pipeline(steps=[("Imputer", simple_imputer), # Replace missing values with Zero
            ("RobustScaler", robust_scaler)]) #keep every feature in same range and handles outliers
            
            return preprocessor
        except Exception as e:
            raise SensorException(e,sys) from e

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info("Initiating Data Transformation")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_fiLe_path)  
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)    
            preprocessor = self.get_data_transformer_object()         

            #TRAINING DATAFRAME
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)  
            target_feature_train_df = train_df[TARGET_COLUMN] 
            target_feature_train_df = target_feature_train_df.replace(TargetValueMapping().to_dict())

            # testing dataframe
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)  
            target_feature_test_df = test_df[TARGET_COLUMN] 
            target_feature_test_df = target_feature_test_df.replace(TargetValueMapping().to_dict())

            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_object.transform(input_feature_test_df)

            logging.info("completed train and test dfs in initiate transformation")

            smt = SMOTETomek(sampling_strategy="minority")

            input_feature_train_final, target_feature_train_final = smt.fit_resample(transformed_input_train_feature, target_feature_train_df)

            input_feature_test_final, target_feature_test_final = smt.fit_resample(transformed_input_test_feature, target_feature_test_df
            )

            train_arr = np.c_[input_feature_train_final, np.array(target_feature_train_final)]
            test_arr = np.c_[input_feature_test_final, np.array(target_feature_test_final)]

            # SAVE NUMPY DATA
            logging.info("Saving Numpy data from data transformation")
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr)

            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)
            
            # PREPARING ARTIFACT
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

            logging.info(f"Data Transformation Artifact: {data_transformation_artifact}")

        except Exception as e:
            raise SensorException(e,sys) from e