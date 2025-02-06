import sys
import os

# Add the 'src' directory to the Python path so that cnnClassifier can be found.
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from pathlib import Path

# Now import your modules after updating the sys.path
from cnnClassifier.utils.common import decode_image
from cnnClassifier.pipeline.prediction import PredictionPipeline

# Optionally set locale environment variables
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# ClientApp class to initialize prediction pipeline and set filename for the input image
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Home route renders the index.html template
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

# Train route runs the main.py script (or dvc repro as needed)
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # Alternatively, if you want to use DVC, uncomment the following line:
    # os.system("dvc repro")
    return "Training done successfully!"

# Predict route: receives a POST request with image data, decodes it, and returns predictions.
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        if not request.json or 'image' not in request.json:
            return jsonify({"error": "No image data provided"}), 400
        
        # Extract image string from the request
        image_string = request.json['image']
        
        # Decode the image (convert filename to a Path object)
        decode_image(image_string, Path(clApp.filename))
        
        # Get prediction from the prediction pipeline
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        print("Error in /predict route:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True)
