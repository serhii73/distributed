import json
import requests
from flask import Flask, jsonify, request

# r = requests.post("http://localhost:8000/", data=json.dumps({'k': 'v'}))
# r = requests.get("http://localhost:8000/")

app = Flask(__name__)

data = []


@app.route("/", methods=["GET", "POST"])
def main():

    if request.method == "POST":
        msg = json.loads(request.data)
        data.append(msg)
        req = requests.post("http://localhost:9000/", data=json.dumps(msg))
        req2 = requests.post("http://localhost:10000/", data=json.dumps(msg))
        return jsonify(msg) if (req.ok and req2.ok) else "Error"
    else:
        return jsonify(data)
