import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
import logging
from cnnClassifier.utils.common import save_json
from cnnClassifier.utils.common import create_directories
from cnnClassifier.utils.common import read_yaml
from cnnClassifier.entity.config_entity import EvaluationConfig
import os
import mlflow.tensorflow

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/diazmanne/e2e-mlflow-dvc.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="diazmanne"
os.environ["MLFLOW_TRACKING_PASSWORD"]="f4e87115c3d98a2ef151c0469443be9738fa35ff"

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.model = None
        self.valid_generator = None
        self.score = None
        logging.info("Evaluation instance created successfully.")

    def _valid_generator(self):  # Fixed method name (removed asterisks)
        try:
            logging.info("Initializing the validation data generator.")

            datagenerator_kwargs = dict(
                rescale=1.0 / 255,
                validation_split=0.30
            )

            dataflow_kwargs = dict(
                target_size=self.config.params_image_size[:-1],
                batch_size=self.config.params_batch_size,
                interpolation="bilinear",
                class_mode='categorical'  # Added class_mode for classification
            )

            valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )

            self.valid_generator = valid_datagenerator.flow_from_directory(
                directory=str(self.config.training_data),  # Convert Path to string
                subset="validation",
                shuffle=False,
                **dataflow_kwargs
            )
            logging.info("Validation data generator initialized successfully.")

        except Exception as e:
            logging.error(f"Error initializing validation generator: {e}")
            raise e

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        try:
            logging.info(f"Loading model from: {path}")
            model = tf.keras.models.load_model(str(path))  # Convert Path to string
            logging.info("Model loaded successfully.")
            return model
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise e

    def evaluation(self):
        try:
            logging.info("Starting model evaluation.")
            self.model = self.load_model(self.config.path_of_model)
            self._valid_generator()

            if self.valid_generator is None:
                raise ValueError("Validation generator not initialized.")

            self.score = self.model.evaluate(
                self.valid_generator,
                steps=len(self.valid_generator)  # Added steps parameter
            )
            logging.info(f"Evaluation completed. Loss: {self.score[0]}, Accuracy: {self.score[1]}")
            self.save_score()

        except Exception as e:
            logging.error(f"Error during evaluation: {e}")
            raise e

    def save_score(self):
        try:
            logging.info("Saving evaluation scores.")
            scores = {"loss": float(self.score[0]), "accuracy": float(self.score[1])}  # Convert to Python float
            save_json(path=Path("scores.json"), data=scores)
            logging.info(f"Scores saved successfully: {scores}")
        except Exception as e:
            logging.error(f"Error saving scores: {e}")
            raise e

    def log_into_mlflow(self):
        try:
            logging.info("Logging metrics and model to MLflow.")
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metrics({
                    "loss": float(self.score[0]),
                    "accuracy": float(self.score[1])
                })

                # Log model using mlflow.tensorflow
                logging.info("Generating model signature for MLflow logging.")
                input_data = next(iter(self.valid_generator))[0][:5]  # Get sample inputs
                predictions = self.model.predict(input_data)

                # Highlighted code
                mlflow.tensorflow.log_model(
                    self.model,
                    "model",
                    signature=mlflow.models.signature.infer_signature(input_data, predictions)
                )
                logging.info("Model logged to MLflow successfully.")
                print(tf.__version__)  # Instead of tensorflow.keras.__version__

        except Exception as e:
            logging.error(f"Error during MLflow logging: {e}")
            raise e
