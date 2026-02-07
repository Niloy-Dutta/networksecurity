from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
import sys

if __name__ == '__main__': 
    try:
        trainingpipeleineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipeleineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(training_pipeline_config = trainingpipeleineconfig)
        data_validation = DataValidation(data_ingstion_artifact=dataingestionartifact,
                                         data_validation_config=data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.inititate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)
        data_transformation_config =  DataTransformationConfig(training_pipeline_config=trainingpipeleineconfig)
        logging.info("data Transformation started")
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=data_transformation_config)  
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        logging.info("Model Training sstared")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config=trainingpipeleineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.iniitate_model_trainer()
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    