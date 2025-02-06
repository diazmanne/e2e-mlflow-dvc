import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 
from pathlib import Path
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os 

class PredictionPipeline:
    def __init__(self, filename: Path):  # Add type hint for Path
        self.filename = filename
        
    def predict(self):
        # Convert Path to string for model operations
        # Alternative using Path for model path
        model_path = Path("model") / "trained_model.keras"
        model = load_model(str(model_path))  # Convert to string for TensorFlow compatibility

        # Convert Path object to string for image loading
        test_image = image.load_img(str(self.filename), target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        
        # Rest of your prediction logic remains the same
        if result[0] == 1:
            return [{"image": "Normal"}]
        else:
            return [{"image": "Adenocarcinoma Cancer"}]