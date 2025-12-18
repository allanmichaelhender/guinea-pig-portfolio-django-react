import React from "react";
import "../styles/Note.css";


export default function Portfolio({ portfolio, onDelete }) {
  const formattedDate = new Date(portfolio.submission_date).toLocaleDateString("en-UK");


  return (
    <div className="note-container">
        <h1>ID: {portfolio.id}</h1>
      <p className="note-title">investment_frequency {portfolio.investment_frequency}</p>
      <p className="note-content">start_date {portfolio.start_date}</p>
      <p className="note-content">end_date {portfolio.end_date}</p>
      <p className="note-content">FTSE_weight {portfolio.FTSE_weight}</p>
      <p className="note-content">SNP500_weight {portfolio.SNP500_weight}</p>
      <p className="note-content">NIKKEI225_weight {portfolio.NIKKEI225_weight}</p>
      <p className="note-content">submission_date {formattedDate}</p>
      <p className="note-content">total_amount_invested {portfolio.total_amount_invested}</p>
      <p className="note-content">final_amount {portfolio.final_amount}</p>
      <p className="note-content"> change_percentage {portfolio.change_percentage}</p>
      <button className="delete-button" onClick={() => onDelete(portfolio.id)}>
        Delete
      </button>
    </div>
  );
}
