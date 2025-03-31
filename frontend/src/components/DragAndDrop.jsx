import React, { useState } from "react";

const DragAndDrop = ({ onFileSelect }) => {
  const [image, setImage] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
      onFileSelect(file);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
      onFileSelect(file);
    }
  };

  return (
    <div 
      className="upload-box" 
      onClick={() => document.getElementById("fileInput").click()}
      onDragOver={(e) => e.preventDefault()}
      onDrop={handleDrop}
    >
      <input 
        id="fileInput" 
        type="file" 
        accept="image/*" 
        onChange={handleFileChange} 
        hidden 
      />
      {image ? (
        <img src={image} alt="Preview" style={{ maxWidth: "100%", borderRadius: "10px" }} />
      ) : (
        <p>Drag & Drop or Click to Upload</p>
      )}
    </div>
  );
};

export default DragAndDrop;
