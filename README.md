# Deep Learning Web App

This project is a deep learning-powered web application that provides two main functionalities:
- **Image Classification using a CNN**
- **Image Denoising using a Denoising Autoencoder (DAE)**

The project consists of:
- **Frontend**: Built with React and Tailwind CSS.
- **Backend**: Built with Flask, using TensorFlow/Keras models for inference.

---

## Features
- Upload images for classification or denoising.
- Perform real-time inference using pre-trained deep learning models.
- Fetch models from Hugging Face instead of storing them locally.

---

## Project Structure
```
DL-project
│── frontend/       # React frontend
│── backend/        # Flask backend
│   ├── app/
│   │   ├── routes/
│   │   │   ├── predict.py  # Handles model inference
│   │   │   ├── denoise.py  # Handles image denoising
│   │   ├── utils/
│   │   │   ├── model_loader.py  # Loads models from Hugging Face
│   ├── models/      # (Empty) Models will be downloaded at runtime
│   ├── run.py       # Main backend entry point
│── README.md        # Project documentation
│── .gitignore       # Ignore unnecessary files
```

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/shruti10951/DeepLearningProject.git
cd DL-project
```

### 2. Backend Setup
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Frontend Setup
```sh
cd frontend
npm install
```

---

## Running the Project

### 1. Start the Backend
```sh
cd backend
python run.py
```

### 2. Start the Frontend
```sh
cd frontend
npm run dev
```

---

## Model Downloading from Hugging Face

Instead of storing models locally, they are downloaded from Hugging Face before inference.

Modify `backend/app/utils/model_loader.py`:
```python
from huggingface_hub import hf_hub_download

CNN_MODEL_PATH = hf_hub_download(repo_id="your-hf-repo", filename="cnnModel.h5")
DAE_MODEL_PATH = hf_hub_download(repo_id="your-hf-repo", filename="denoiseModel.h5")
```

---

## Technologies Used
- **Frontend:** React, Vite, Tailwind CSS
- **Backend:** Flask, TensorFlow/Keras
- **Models:** Convolutional Neural Network (CNN), Denoising Autoencoder (DAE)
- **Hosting:** Hugging Face for model storage

