import React, {useState} from "react";
import { FaSearch } from "react-icons/fa"
import '../App.css'

export const Search = () => {
  const [query, setQuery] = useState("")
  const [postvalue, setPostValue] = useState("")
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault(); // Prevent the default form submission behavior
    setPostValue(query)
    setSubmitted(true);
  };

  // handleSubmit = () => {
  //   setQuery("query" + "handled")
  // }
  // const fetchData = (value) => 
    return (
          <section className="search-bar">
            <p>Tell us what's wrong</p>
            <form onSubmit={handleSubmit}>
            <div className="form-search">
              <button type="submit" value="Submit">
              <FaSearch id="search-icon" className="search-icon"/>
              </button>
              <input type="query" 
              placeholder="arthiritis, athletes foot, whooping cough, etc" 
              value={query} 
              onChange={(e) => setQuery(e.target.value)}/>
            </div>
            </form>
            {submitted ? postvalue + " has been submitted" : query}
          </section>
      )
}