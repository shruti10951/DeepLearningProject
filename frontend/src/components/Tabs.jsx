import React from "react";
import "../index.css";

const Tabs = ({ selectedTab, setSelectedTab }) => {
  return (
    <div className={`tab-container ${selectedTab}`}>
      <div className="tab-slider"></div> {/* 🔥 The Actual Sliding Part */}
      <button 
        className={`tab-button ${selectedTab === "classification" ? "active" : ""}`} 
        onClick={() => setSelectedTab("classification")}
      >
        Classification
      </button>
      <button 
        className={`tab-button ${selectedTab === "denoising" ? "active" : ""}`} 
        onClick={() => setSelectedTab("denoising")}
      >
        Denoising
      </button>
    </div>
  );
};

export default Tabs;
