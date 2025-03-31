import React, { useState } from "react";
import DragAndDrop from "../components/DragAndDrop";
import Swal from "sweetalert2";

const Classification = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) {
      Swal.fire("Error", "Please select an image first!", "error");
      return;
    }

    Swal.fire({
      title: "Processing...",
      text: "Identifying fruit...",
      allowOutsideClick: false,
      didOpen: () => Swal.showLoading(),
    });

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:5000/model/predict", {
        method: "POST",
        body: formData,
        headers: {
          "Accept": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("API Response:", data); // Debugging log

      // Ensure the API response contains predicted_class and confidence
      if (!data.predicted_class || !data.confidence) {
        throw new Error("Invalid API response");
      }

      setResult({
        predictedClass: data.predicted_class,
        confidence: data.confidence, // Already in percentage format
      });

      Swal.fire("Done!", `Fruit identified: ${data.predicted_class}`, "success");

    } catch (error) {
      Swal.fire("Error", "Something went wrong!", "error");
      console.error("Error:", error);
    }
  };

  return (
    <div className="container">
      <h2>Fruit Classification</h2>
      <DragAndDrop onFileSelect={setFile} />
      <button className="button" onClick={handleUpload}>Classify</button>

      {result && (
        <div className="result">
          <h3>Result:</h3>
          <p><strong>Predicted Fruit:</strong> {result.predictedClass}</p>
          <p><strong>Confidence:</strong> {result.confidence}</p>
        </div>
      )}
    </div>
  );
};

export default Classification;
