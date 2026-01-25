import { useState, useEffect } from "react";
import api from "../api";
import PortfoliosForm from "../components/PortfoliosForm";
import Portfolio from "../components/Portfolio";
import "../styles/Home.css";
import "../styles/Form.css";
import "../styles/Portfolio.css";
import { v4 as uuidv4 } from "uuid";

function Home({ isLoggedIn }) {
  const [portfolios, setPortfolios] = useState([]);

  useEffect(() => {
    if (isLoggedIn) {
      getPortfolios();
    } else {
      setPortfolios([]);
    }
  }, [isLoggedIn]);

  const getPortfolios = () => {
    api
      .get("/api/portfolios/")
      .then((res) => res.data)
      .then((data) => {
        setPortfolios(data);
      })
      .catch((err) => alert(err));
  };

  const handleNewPortfolio = (PortfolioData) => {
    const PortfolioWithId = {
      ...PortfolioData,
      id: PortfolioData.id || uuidv4(),
    };

    setPortfolios((prev) => [PortfolioWithId, ...prev]);
  };

  const deletePortfolio = (id) => {
    if (isLoggedIn) {
      api
        .delete(`/api/portfolios/${id}/`)
        .then((res) => {
          if (res.status === 204);
          else alert("Failed to delete note.");
          getPortfolios();
        })
        .catch((err) => alert(err));
    } else {
      setPortfolios(portfolios.filter((p) => p.id !== id));
    }
  };

  return (
    <div className="home-wrapper">
      <PortfoliosForm
        onPortfolioCreated={handleNewPortfolio}
        isLoggedIn={isLoggedIn}
      />
      <div className="portfolios-list">
        {portfolios.map((p) => (
          <Portfolio
            key={p.id}
            portfolio={p}
            onDelete={() => deletePortfolio(p.id)}
          />
        ))}
      </div>
    </div>
  );
}

export default Home;
