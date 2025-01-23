import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import (PrepareBaseModelConfig)

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        try:
            # Validate input shape
            input_shape = tuple(self.config.params_image_size)

            # Print configuration for debugging
            print("Model Configuration:")
            print(f"Input Shape: {input_shape}")
            print(f"Weights: '{self.config.params_weights}'")  # Debugging print
            print(f"Include Top: {self.config.params_include_top}")
            print(f"Classes: {self.config.params_classes}")

            # Convert weights to string and strip any whitespace
            weights = str(self.config.params_weights).strip() if self.config.params_weights else None
            if weights not in {"imagenet", None}:
                raise ValueError(f"Invalid weights: '{weights}'. Must be 'imagenet' or None.")

            self.model = tf.keras.applications.VGG16(
                input_shape=input_shape,
                weights=weights,
                include_top=self.config.params_include_top,
                classes=self.config.params_classes if self.config.params_include_top else None
            )

            self.save_model(path=self.config.base_model_path, model=self.model)
        except Exception as e:
            print(f"Error in get_base_model: {e}")
            raise

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        model.save(path)
