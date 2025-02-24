import { SearchBar } from './components/SearchBar';
import './App.css';
import { useState } from 'react';
import { SearchResults } from './components/SearchResults';

function App() {

const [results, setResults] = useState([])

  return (
    <div className="App">
      <div className='search-bar-container'>
        <SearchBar setResults={setResults} />
        <SearchResults results={results}/>
      </div>
    </div>
  );
}

export default App;
