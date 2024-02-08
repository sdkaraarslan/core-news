import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './index.css';

const HomePage = () => {
    const [date, setDate] = useState('');
    const navigate = useNavigate();
    const fetchKeyword = async (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      const response = await fetch(`http://localhost:8000/get-keyword/?date=${date}`);
      const data = await response.json();
      navigate('/keyword', { state: { keyword: data.keyword } });
    };

  return (
    <div className="min-h-screen bg-gray-800 flex items-center justify-center">
      <form onSubmit={fetchKeyword} className="bg-gray-700 p-6 rounded-lg shadow-lg">
        <div className="mb-4">
          <label htmlFor="date" className="block text-white text-sm font-bold mb-2">
            Date
          </label>
          <input
            id="date"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="date"
            value={date}
            onChange={(e) => setDate(e.currentTarget.value)}
          />
        </div>
        <div className="flex items-center justify-between">
          <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
            Get Keyword
          </button>
        </div>
      </form>
    </div>
  );
};

export default HomePage;
