import { useLocation } from 'react-router-dom';

interface LocationState {
    keyword: string;
  }
  
  const KeywordPage = () => {
    const location = useLocation();
    const state = location.state as LocationState; // Cast to the state shape you expect
    const keyword = state?.keyword || 'Keyword not passed';
  
  // Placeholder for image URL - replace with image fetching logic
  const imageUrl = `https://source.unsplash.com/featured/?${keyword}`;

  return (
    <div className="min-h-screen bg-gray-800 flex flex-col items-center justify-center">
      <div className="bg-gray-700 p-6 rounded-lg shadow-lg text-center">
        <h1 className="text-2xl text-white font-bold mb-4">Keyword of the day:</h1>
        <p className="text-xl text-white mb-4">{keyword}</p>
        <img src={imageUrl} alt={keyword} className="max-w-xs rounded-lg shadow-lg" />
      </div>
    </div>
  );
};

export default KeywordPage;
