import React, { useState } from "react";
import Classification from "./pages/Classification";
import Denoising from "./pages/Denoising";
import Tabs from "./components/Tabs";
import Footer from "./components/Footer";

const App = () => {
  const [selectedTab, setSelectedTab] = useState("classification");

  return (
    <div>
      <h1>Deep Learning Image Processor</h1>
      <Tabs selectedTab={selectedTab} setSelectedTab={setSelectedTab} />
      {selectedTab === "classification" ? <Classification /> : <Denoising />}
      <Footer></Footer>
    </div>
  );
};

export default App;
