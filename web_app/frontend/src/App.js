import React from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";  // ✅ Ensure correct path
import SearchPage from "./pages/SearchPage";
import AnnotationsPage from "./pages/AnnotationsPage";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/annotations" element={<AnnotationsPage />} />
      </Routes>
    </div>
  );
};

export default App;