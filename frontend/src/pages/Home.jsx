import { useState, useEffect } from "react"
import api from "../api"
import PortfoliosForm from "../components/PortfoliosForm"
import Portfolio from "../components/Portfolio"
import "../styles/Home.css"

function Home() {
  const [portfolios, setPortfolios] = useState([])

  useEffect(() => {
    getPortfolios()
  }, [])

  const getPortfolios = () => {
    api
      .get("/api/portfolios/")
      .then((res) => res.data)
      .then((data) => {
        setPortfolios(data)
        console.log(data)
      })
      .catch((err) => alert(err))
  }

  const deletePortfolio = (id) => {
    api
      .delete(`/api/portfolios/${id}/`)
      .then((res) => {
        if (res.status === 204) alert("Porfoliio deleted!")
        else alert("Failed to delete note.")
        getPortfolios()
      })
      .catch((err) => alert(err))
  }

  return (
    <div>
      <PortfoliosForm onSourceChange={getPortfolios} />
      <div>
        <h2>Portfolios</h2>
        {portfolios.map((portfolio) => (
          <div key={portfolio.id}>
            <Portfolio portfolio={portfolio} onDelete={deletePortfolio} />
          </div>
        ))}
      </div>
    </div>
  )
}

export default Home
