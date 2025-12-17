import React from "react";
import "../styles/Note.css";


export default function Portfolio({ portfolio, onDelete }) {

  return (
    <div className="note-container">
        <h1>ID: {portfolio.id}</h1>
      <p className="note-title">{portfolio.investment_frequency}</p>
      <p className="note-content">{portfolio.start_date}</p>
      <p className="note-content">{portfolio.end_date}</p>
      <p className="note-content">{portfolio.FTSE_weight}</p>
      <p className="note-content">{portfolio.SNP500_weight}</p>
      <p className="note-content">{portfolio.NIKKEI225_weight}</p>
      <button className="delete-button" onClick={() => onDelete(portfolio.id)}>
        Delete
      </button>
    </div>
  );
}
