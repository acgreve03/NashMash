import React from "react";
import { SearchResult } from "./SearchResult";
import "./SearchResults.css";

export const SearchResults = ({ results }) => {
  return (
    <div className="results-list">
      {results.map((result, index) => (
        <SearchResult key={index} result={result} />
      ))}
    </div>
  );
};