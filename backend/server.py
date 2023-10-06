from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import requests
import scraper

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello server"

@app.route('/query', methods=['POST'])
def get_query():
    #we have the data
    data = request.json["query"]
    response_data = scraper.med_scraper(data)
    user_response = { 
            "issue" : data, 
            "response" : response_data
        } 
    json_resp = jsonify(user_response)
    print(json_resp)
    return json_resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="9874",debug=True)