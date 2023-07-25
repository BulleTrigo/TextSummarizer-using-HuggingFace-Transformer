from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed!<<<<<\n\nx================x================x\n")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed!<<<<<\n\nx================x================x\n")
except Exception as e:
    logger.exception(e)
    raise e