import numpy as np
import io
from flask import Blueprint, request, jsonify
from tensorflow.keras.preprocessing import image
from PIL import Image
from app.utils.model_loader import get_cnn_model

predict_bp = Blueprint('/model', __name__)

class_labels = ['apple', 'avocado', 'banana', 'cherry', 'kiwi', 'mango', 
                'orange', 'pineapple', 'strawberries', 'watermelon']

@predict_bp.route('/predict', methods=['POST'])
def predict():
    model = get_cnn_model()  

    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    # Read image and preprocess
    img = Image.open(io.BytesIO(file.read()))
    img = img.resize((224, 224))  
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Get predictions
    predictions = model.predict(img_array)

    print("Predictions:", predictions)
    
    if np.isnan(predictions).any() or np.isinf(predictions).any():
        return jsonify({'error': 'Invalid predictions from model'}), 500

    predicted_index = int(np.argmax(predictions))  
    predicted_class = class_labels[predicted_index]  
    confidence = float(np.max(predictions)) * 100  

    return jsonify({
        'predicted_class': predicted_class,
        'confidence': f"{confidence:.2f}%"
    })
