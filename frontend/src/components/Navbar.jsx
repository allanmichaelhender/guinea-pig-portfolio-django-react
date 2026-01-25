import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navbar.css';

function Navbar({ isLoggedIn }) {
  return (
    <nav className="navbar">
      <Link to="/" className="nav-link">Home</Link>
      {!isLoggedIn ? (
        <>
          <Link to="/login" className="nav-link">Login</Link>
          <Link to="/register" className="nav-link">Register</Link>
        </>
      ) : (
        <Link to="/logout" className="nav-link">Logout</Link>
      )}
    </nav>
  );
}

export default Navbar;