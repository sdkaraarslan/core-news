import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage';
import KeywordPage from './KeywordPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/keyword" element={<KeywordPage />} />
      </Routes>
    </Router>
  );
};

export default App;
