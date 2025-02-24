import React, { useState } from "react";  
import { FaSearch } from "react-icons/fa";
import "./SearchBar.css";

export const SearchBar = ({ setResults }) => {
    const [input, setInput] = useState("");  

    const fetchData = (value) => {
        fetch("http://127.0.0.1:8000/search?q=" + encodeURIComponent(value))
            .then((response) => response.json())
            .then((json) => {
                if (!Array.isArray(json)) {
                    console.error("Unexpected API response:", json);
                    console.log("API Response:", json);
                    setResults([]); // Set to empty in case of unexpected data
                    return;
                }
                setResults(json); // Update the results in the parent state
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
                setResults([]); // Clear results on error
            });
    };

    const handleChange = (val) => {
        setInput(val);
        fetchData(val);
    };

    return (
        <div className="input-wrapper">
            <FaSearch id="search-icon" />
            <input 
                placeholder="Search" 
                value={input} 
                onChange={(e) => handleChange(e.target.value)} 
            />
        </div>
    );
};