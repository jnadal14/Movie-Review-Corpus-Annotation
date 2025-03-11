import React from "react";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div style={styles.container}>
      <img src="/logo.png" alt="Movie Review Logo" style={styles.logo} />
      <h1 style={styles.title}>Movie Review Corpus</h1>
      <p style={styles.subtitle}>Explore and search annotated movie reviews.</p>

      {/* Navigation Buttons */}
      <div style={styles.buttonContainer}>
        <Link to="/search" style={styles.button}>
          <img src="/search.png" alt="Search Icon" style={styles.icon} /> Search Reviews
        </Link>
        <Link to="/annotations" style={styles.button}>
          <img src="/annotation.png" alt="Annotations Icon" style={styles.icon} /> View Annotations
        </Link>
      </div>

      {/* GitHub Link */}
      <div style={styles.githubLink}>
        <a 
          href="https://github.ubc.ca/MDS-CL-2024-25/COLX_523_Group-Repository_David-Daoming-Jacob-Nicole" 
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
  logo: {
    width: "100px",
    height: "100px",
    marginBottom: "20px",
  },
  title: {
    fontSize: "32px",
    fontWeight: "bold",
    marginBottom: "10px",
  },
  subtitle: {
    fontSize: "18px",
    color: "#555",
    marginBottom: "20px",
  },
  buttonContainer: {
    display: "flex",
    justifyContent: "center",
    gap: "15px",
    marginTop: "20px",
  },
  button: {
    display: "flex",
    alignItems: "center",
    gap: "10px",
    padding: "10px 20px",
    fontSize: "16px",
    fontWeight: "bold",
    backgroundColor: "#007BFF",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    textDecoration: "none",
    cursor: "pointer",
  },
  githubLink: {
    marginTop: "30px",
    display: "flex",
    justifyContent: "center",
  },
  link: {
    display: "flex",
    alignItems: "center",
    gap: "10px",
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

export default HomePage;