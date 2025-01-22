from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info("Data ingestion pipeline completed successfully.")
        except Exception as e:
            logger.exception("An error occurred during the data ingestion pipeline.")
            raise e
