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
        r = requests.post("http://localhost:8000/", data=json.dumps({'k': 'v'}))
        import ipdb
        ipdb.set_trace()
        r = requests.get("http://localhost:8000/")
        return jsonify(msg)
    else:
        return jsonify(data)
