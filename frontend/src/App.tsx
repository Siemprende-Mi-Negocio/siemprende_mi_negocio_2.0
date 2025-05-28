import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';

const App: React.FC = () => (
  <Routes>
    <Route path="/" element={<LoginPage />} />
  </Routes>
);

export default App;
