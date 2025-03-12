import React from "react";
import { Link } from "react-router-dom";

const SearchPage = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>
        <img src="/search.png" alt="Search Icon" style={styles.icon} /> Search Movie Reviews
      </h1>
      <p style={styles.subtitle}>
        Enter keywords to find relevant annotated reviews.
      </p>
      
      {/* Placeholder for Search Functionality */}
      <input type="text" placeholder="Search reviews..." style={styles.input} />
      <button style={styles.button}>Search</button>

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
    gap: "10px", // Ensures spacing between icon and text
  },
  subtitle: {
    fontSize: "18px",
    color: "#555",
    marginBottom: "20px",
  },
  input: {
    padding: "10px",
    width: "300px",
    marginRight: "10px",
    borderRadius: "5px",
    border: "1px solid #ccc",
  },
  button: {
    padding: "10px 15px",
    fontSize: "16px",
    fontWeight: "bold",
    backgroundColor: "#007BFF",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
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

export default SearchPage;