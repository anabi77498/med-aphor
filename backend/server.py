from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello server"

@app.route('query', methods=['POST'])
def get_query():
    data = request.form
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True)