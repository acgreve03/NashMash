import { SearchBar } from './components/SearchBar';
import './App.css';
import { useState } from 'react';
import { SearchResults } from './components/SearchResults';

function App() {

const [results1, setResults1] = useState([])
const [results2, setResults2] = useState([])

  return (
    <div className="App">
      
      <div className='search-bar-container'>
        {/* left search bar */}
        <div className='search-item'>
          <SearchBar label="Song 1" setResults={setResults1} />
          <SearchResults results={results1}/>
        </div>

        {/* right search bar */}
        <div className='search-item'>
          <SearchBar label="Song 2" setResults={setResults2} />
          <SearchResults results={results2}/>
        </div>
      </div>

    </div>
  );
}

export default App;
