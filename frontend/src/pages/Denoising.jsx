import React, { useState } from "react";
import DragAndDrop from "../components/DragAndDrop";
import Swal from "sweetalert2";

const Denoising = () => {
  const [file, setFile] = useState(null);
  const [denoisedImage, setDenoisedImage] = useState(null);

  const handleDenoise = async () => {
    if (!file) {
      Swal.fire("Error", "Please select an image first!", "error");
      return;
    }

    Swal.fire({
      title: "Processing...",
      text: "Denoising image...",
      allowOutsideClick: false,
      didOpen: () => Swal.showLoading(),
    });

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:5000/model/denoise", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to process image");
      }

      // Convert response to an image blob
      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);
      setDenoisedImage(imageUrl);

      Swal.fire("Done!", "Image denoised successfully!", "success");
    } catch (error) {
      Swal.fire("Error", "Something went wrong!", "error");
      console.error("Error:", error);
    }
  };

  return (
    <div className="container">
      <h2>Image Denoising</h2>
      <DragAndDrop onFileSelect={setFile} />
      <button className="button" onClick={handleDenoise}>Denoise</button>

      {denoisedImage && (
        <div className="result">
          <h3>Denoised Image:</h3>
          <img src={denoisedImage} alt="Denoised" className="output-image" />
        </div>
      )}
    </div>
  );
};

export default Denoising;
