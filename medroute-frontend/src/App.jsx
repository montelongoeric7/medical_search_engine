import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Events from './pages/Events';
import Contact from './pages/Contact';
import Login from './pages/Login';
import SignUp from './pages/Signup';
import Dashboard from './pages/Dashboard';
import Search from './pages/Search';
import UpdateData from './pages/UpdateData';
import SearchFree from './pages/SearchFree';

import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/events" element={<Events />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/search" element={<Search />} />
            <Route path="/update" element={<UpdateData />} />
            <Route path="/searchfree" element={<SearchFree />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
