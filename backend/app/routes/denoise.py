# this is 32*32 image of cifar

# import io
# import numpy as np
# from flask import Blueprint, request, jsonify, send_file
# from PIL import Image
# from app.utils.model_loader import get_dae_model  # Import from model_loader

# denoise_bp = Blueprint("denoise", __name__)

# dae_model = get_dae_model()  # Get preloaded model

# def preprocess_image(img):
#     """Convert the uploaded image to a format suitable for the model."""
#     img = img.resize((32, 32))  # Resize to match the model's expected input shape
#     img = np.array(img) / 255.0  # Normalize pixel values
#     img = np.expand_dims(img, axis=0)  # Add batch dimension
#     return img

# @denoise_bp.route("/denoise", methods=["POST"])
# def denoise_image():
#     """Denoise an uploaded image using the autoencoder."""
#     if "file" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["file"]
#     img = Image.open(file).convert("RGB")
#     img_array = preprocess_image(img)  # Resize to (32, 32)

#     # Perform denoising
#     denoised_img_array = dae_model.predict(img_array)[0]  # Remove batch dimension
#     denoised_img_array = (denoised_img_array * 255).astype(np.uint8)  # Convert to image format

#     # Convert to PIL Image
#     denoised_img = Image.fromarray(denoised_img_array)

#     # **Upscale the denoised image to 256x256**
#     denoised_img = denoised_img.resize((256, 256), Image.NEAREST)  # Use nearest-neighbor scaling

#     # Save the denoised image to a buffer
#     img_io = io.BytesIO()
#     denoised_img.save(img_io, format="PNG")
#     img_io.seek(0)

#     return send_file(img_io, mimetype="image/png")


# this is 128*128 image of bsd68

import io
import numpy as np
from flask import Blueprint, request, jsonify, send_file
from PIL import Image
from app.utils.model_loader import get_dae_model  # Import from model_loader

denoise_bp = Blueprint("denoise", __name__)

dae_model = get_dae_model()  # Get preloaded model

def preprocess_image(img):
    """Convert the uploaded image to a format suitable for the model."""
    img = img.resize((128, 128))  # Resize to match model input shape
    img = np.array(img).astype("float32") / 127.5 - 1  # Normalize to [-1,1]
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@denoise_bp.route("/denoise", methods=["POST"])
def denoise_image():
    """Denoise an uploaded image using the autoencoder."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = Image.open(file).convert("RGB")
    img_array = preprocess_image(img)  # Resize to (128,128)

    # Perform denoising
    denoised_img_array = dae_model.predict(img_array)[0]  # Remove batch dimension
    denoised_img_array = ((denoised_img_array + 1) * 127.5).astype(np.uint8)  # Convert back to [0,255]

    # Convert to PIL Image
    denoised_img = Image.fromarray(denoised_img_array)

    # **Upscale the denoised image back to original size only if necessary**
    if img.size != (128, 128):  # Prevent unnecessary resizing
        denoised_img = denoised_img.resize(img.size, Image.BILINEAR)  # Use bilinear interpolation

    # Save the denoised image to a buffer
    img_io = io.BytesIO()
    denoised_img.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")
