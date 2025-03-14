import React, { useState } from "react";
import { Link } from "react-router-dom";

const AnnotationsPage = () => {
  // State for the annotation label input
  const [annotationLabel, setAnnotationLabel] = useState("");

  // State for the returned annotation results
  const [results, setResults] = useState([]);

  // Loading & error states
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Handler to call the /annotations endpoint
  const handleAnnotationsSearch = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/annotations?annotation_label=${encodeURIComponent(annotationLabel)}`
      );
      if (!response.ok) {
        throw new Error("Error retrieving annotated reviews");
      }
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>
        <img src="/annotation.png" alt="Annotation Icon" style={styles.icon} /> View Annotations
      </h1>
      <p style={styles.subtitle}>Browse through annotated movie reviews.</p>

      {/* Annotation Label Input + Button */}
      <div style={styles.searchContainer}>
        <input
          type="text"
          placeholder="Enter an annotation label, e.g. Pathos"
          value={annotationLabel}
          onChange={(e) => setAnnotationLabel(e.target.value)}
          style={styles.input}
        />
        <button onClick={handleAnnotationsSearch} style={styles.button}>
          Search
        </button>
      </div>

      {/* Show loading or errors if any */}
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Render results if any */}
      {results.length > 0 ? (
        <div style={styles.resultsContainer}>
          {results.map((review) => (
            <div key={review.review_id} style={styles.resultItem}>
              <p>{review.text}</p>
              <p>
                <strong>Annotation:</strong> {review.annotation_label}
              </p>
            </div>
          ))}
        </div>
      ) : (
        !loading && <p>No annotations found.</p>
      )}

      {/* Navigation Links */}
      <div style={styles.navLinks}>
        <Link to="/" style={styles.link}>
          <img src="/home.png" alt="Home Icon" style={styles.icon} /> Return to Homepage
        </Link>
        <a
          href="https://github.ubc.ca/MDS-CL-2024-25/COLX_523_Group-Repository_David-Daoming-Jacob-Nicole"
          target="_blank"
          rel="noopener noreferrer"
          style={styles.link}
        >
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
    minHeight: "100vh",
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
  searchContainer: {
    display: "flex",
    justifyContent: "center",
    gap: "10px",
    marginBottom: "20px",
  },
  input: {
    padding: "10px",
    width: "300px",
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
  resultsContainer: {
    marginTop: "20px",
  },
  resultItem: {
    border: "1px solid #ccc",
    borderRadius: "5px",
    padding: "10px",
    margin: "10px auto",
    width: "80%",
    textAlign: "left",
    backgroundColor: "#fff",
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
