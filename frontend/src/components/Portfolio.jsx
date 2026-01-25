import React from "react";

export default function Portfolio({ portfolio, onDelete }) {
  const formattedDate = new Date(portfolio.submission_date).toLocaleDateString(
    "en-UK",
  );

  return (
  <div className="portfolio-card">
    <div className="portfolio-header">
      <h3>Portfolio ID: {portfolio.id.toString().slice(-4)}</h3>
      <span className="frequency-badge">{portfolio.investment_frequency}</span>
    </div>

    <div className="portfolio-grid">
      <div className="info-section">
        <h4>Schedule</h4>
        <p><span>Start:</span> {portfolio.start_date}</p>
        <p><span>End:</span> {portfolio.end_date}</p>
      </div>

      <div className="info-section">
        <h4>Weights</h4>
        <div className="weight-tags">
          <span className="tag">FTSE: {portfolio.FTSE_weight}</span>
          <span className="tag">S&P: {portfolio.SNP500_weight}</span>
          <span className="tag">NIK: {portfolio.NIKKEI225_weight}</span>
          <span className="tag">EUR: {portfolio.EUROSTOXX_weight}</span>
          <span className="tag">HSI: {portfolio.HSI_weight}</span>
        </div>
      </div>

      <div className="info-section performance">
        <h4>Performance</h4>
        <p className="total-invested">Total: £{portfolio.total_amount_invested}</p>
        <p className="final-value">Final: £{Number(portfolio.final_amount).toFixed(2)}</p>
        <p className={`change ${portfolio.change_percentage >= 0 ? 'pos' : 'neg'}`}>
          {portfolio.change_percentage >= 0 ? '▲' : '▼'} {(portfolio.change_percentage * 100).toFixed(2)}%
        </p>
      </div>
    </div>

    <button className="delete-button" onClick={() => onDelete(portfolio.id)}>
      Delete Portfolio
    </button>
  </div>
);
}
