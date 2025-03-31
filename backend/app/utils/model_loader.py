import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.losses import MeanSquaredError
from huggingface_hub import hf_hub_download

# Hugging Face model repo details
HF_REPO_ID = "shruti10951/DeepLearningModels"  # Replace with your actual repo
CNN_MODEL_FILENAME = "cnnModel.h5"
DAE_MODEL_FILENAME = "denoiseModel.h5"

# Get absolute path to project root
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Define model paths
MODEL_DIR = os.path.join(PROJECT_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)  # Ensure the directory exists

CNN_MODEL_PATH = os.path.join(MODEL_DIR, CNN_MODEL_FILENAME)
DAE_MODEL_PATH = os.path.join(MODEL_DIR, DAE_MODEL_FILENAME)


def download_model_if_needed(model_path, model_filename):
    """Download the model from Hugging Face if it doesn't exist locally."""
    if not os.path.exists(model_path):
        print(f"Downloading {model_filename} from Hugging Face...")
        hf_hub_download(
            repo_id=HF_REPO_ID,
            filename=model_filename,
            local_dir=MODEL_DIR
        )


# Download models if not present locally
download_model_if_needed(CNN_MODEL_PATH, CNN_MODEL_FILENAME)
download_model_if_needed(DAE_MODEL_PATH, DAE_MODEL_FILENAME)

# Load models
print(f"Loading CNN model from: {CNN_MODEL_PATH}")
cnn_model = load_model(CNN_MODEL_PATH)

print(f"Loading DAE model from: {DAE_MODEL_PATH}")
dae_model = load_model(DAE_MODEL_PATH, custom_objects={"mse": MeanSquaredError()})


def get_cnn_model():
    """Returns the loaded CNN model"""
    return cnn_model


def get_dae_model():
    """Returns the loaded DAE model"""
    return dae_model
