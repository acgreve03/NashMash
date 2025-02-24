import React from 'react'
import "./SearchResult.css"

export const SearchResult = ({ result }) => {
    return (
      <div className="search-result" onClick={(e) => alert(`You clicked on ${result.title} by ${result.artist}\nBPM: ${result.bpm_high}\nKey: ${result.key}`)}>
        {result.title} - {result.artist}
      </div>
    );
  };




  