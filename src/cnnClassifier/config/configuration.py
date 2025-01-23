from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig)
from cnnClassifier.entity.config_entity import (PrepareBaseModelConfig)
from pathlib import Path



class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Now create the directories using the correct Path type
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Ensure that the root_dir is created as well
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        # Access prepare_base_model section of config
        config = self.config["prepare_base_model"]  

        # Create the directory for the base model
        create_directories([config["root_dir"]])

        # Build PrepareBaseModelConfig object
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config["root_dir"]),
            base_model_path=Path(config["base_model_path"]),
            updated_base_model_path=Path(config["updated_base_model_path"]),
            params_image_size=self.params["IMAGE_SIZE"],
            params_learning_rate=self.params["LEARNING_RATE"],
            params_include_top=self.params["INCLUDE_TOP"],
            params_weights=self.params["WEIGHTS"],
            params_classes=self.params["CLASSES"]
        )
        return prepare_base_model_config
