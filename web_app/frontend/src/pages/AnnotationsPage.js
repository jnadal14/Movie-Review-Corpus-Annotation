import React from "react";
import { Link } from "react-router-dom";

const AnnotationsPage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>
        <img src="/annotation.png" alt="Annotation Icon" style={styles.icon} /> View Annotations
      </h1>
      <p style={styles.subtitle}>Browse through annotated movie reviews.</p>

      {/* Placeholder for Annotation Display */}
      <div style={styles.annotationBox}>
        <p><strong>Example Annotation:</strong></p>
        <p><em>"A thrilling masterpiece with stunning cinematography!"</em></p>
        <p>
          <img src="/annotation.png" alt="Annotation Icon" style={styles.icon} /> Annotation: <strong>Pathos (Emotional Appeal)</strong>
        </p>
      </div>

      {/* Navigation Links */}
      <div style={styles.navLinks}>
        <Link to="/" style={styles.link}>
          <img src="/home.png" alt="Home Icon" style={styles.icon} /> Return to Homepage
        </Link>
        <a href="https://github.ubc.ca/MDS-CL-2024-25/COLX_523_Group-Repository_David-Daoming-Jacob-Nicole" 
           target="_blank" 
           rel="noopener noreferrer"
           style={styles.link}>
          <img src="/github_icon.png" alt="GitHub Icon" style={styles.icon} /> View on GitHub
        </a>
      </div>
    </div>
  );
};

const styles = {
  container: {
    textAlign: "center",
    fontFamily: "Arial, sans-serif",
    padding: "40px",
    backgroundColor: "#f0f5ff",
    height: "100vh",
  },
  title: {
    fontSize: "28px",
    fontWeight: "bold",
    marginBottom: "10px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    gap: "10px",
  },
  subtitle: {
    fontSize: "18px",
    color: "#555",
    marginBottom: "20px",
  },
  annotationBox: {
    border: "1px solid #ccc",
    borderRadius: "8px",
    padding: "20px",
    backgroundColor: "#ffffff",
    maxWidth: "500px",
    margin: "0 auto",
  },
  navLinks: {
    marginTop: "30px",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  link: {
    display: "flex",
    alignItems: "center",
    gap: "8px",
    marginTop: "10px",
    fontSize: "16px",
    color: "#007BFF",
    textDecoration: "none",
    fontWeight: "bold",
  },
  icon: {
    width: "20px",
    height: "20px",
  },
};

export default AnnotationsPage;