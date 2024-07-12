import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import logo from '../assets/logo.png'; // Assuming you have a logo.png in the src/assets folder

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo-container">
        <img src={logo} alt="Mediconnect Logo" className="logo" />
        <h1>Mediconnect</h1>
      </div>
      <div className="links">
        <Link to="/">Home</Link>
        <Link to="/events">Events</Link>
        <Link to="/contact">Contact</Link>
        <Link to="/login">Login</Link>
        <Link to="/signup">Sign Up</Link>
      </div>
    </nav>
  );
};

export default Navbar;
