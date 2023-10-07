import React, {useState} from "react";
import { FaSearch } from "react-icons/fa";
import axios from 'axios';
import '../App.css'
import ReactLoading from "react-loading";

export const Search = () => {
  const [query, setQuery] = useState("")
  const [postvalue, setPostValue] = useState("")
  const [submitted, setSubmitted] = useState(false);
  const [meddata, setMedData] = useState("")
  const [prevquery, setprevQuery] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault(); 

    // updating states
    setPostValue(query);
    setprevQuery('')
    setMedData('')
    setSubmitted(true);

    // fetching responses from backend
    axios.post("http://localhost:5000/query", {query})
    .then(resp => {
        setSubmitted(false)
        setprevQuery(query)
        setMedData("\t    " + resp.data.response); 
        console.log(resp.data.response);
      })
    .catch(err=> console.log(err))
    
  };


    return (
      <main className="main">
          <section className="search-bar">
            <p>Tell us what's wrong</p>
            <form onSubmit={handleSubmit}>
            <div className="form-search">
              <button type="submit" value="Submit">
              <FaSearch id="search-icon" className="search-icon"/>
              </button>
              <input type="query" 
              placeholder="arthritis, athletes foot, flu, etc" 
              value={query} 
              onChange={(e) => setQuery(e.target.value)}/>
            </div>
            </form>
          </section>
          {submitted ? 
          <div className="loading">
          <p>{"Submitted! Hang tight, We're crawling for information about " + postvalue}</p>
            <ReactLoading type="spin" color="#FFFFFF"
                  height={100} width={50} />
          </div> : ""}
          <section className="med-resp">
            <h4>{(meddata == '') ? '' : prevquery + " information and remedies"}</h4>
            <p>{meddata}</p>
          </section>
        </main>
      )
}