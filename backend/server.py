from flask import Flask, request, make_response, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello server"

@app.route('/query', methods=['POST'])
def get_query():
    #we have the data
    data = request.json['query'] + " remedy"
    
    # we scrape data with metaphor & openai (src/scraper)
    
    response_data = { 
            "issue" : data, 
            "response1" : ["ibuprofen", "this is a good medication for malaria"]
        } 
    json_resp = jsonify(response_data)
    print(json_resp)
    return json_resp

if __name__ == "__main__":
    app.run(debug=True)