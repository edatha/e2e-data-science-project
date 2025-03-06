from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataIngestionValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataIngestionTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n==========x")
except Exception as e:
        logger.exception(e)
        raise e
