import json
from itertools import count

import grequests
from flask import Flask, jsonify, request

# r = requests.post("http://localhost:8000/", data=json.dumps({'k': 'v'}))
# r = requests.get("http://localhost:8000/")

app = Flask(__name__)

data = []
c = count()


@app.route("/", methods=["GET", "POST"])
def main():
    urls = ["http://localhost:9000/", "http://localhost:10000/"]

    if request.method == "POST":
        msg_id = next(c)
        msg = request.json.get("message")
        reqs = [
            grequests.post(u, json={"message": msg, "msg_id": msg_id}) for u in urls
        ]
        grequests.map(reqs)
        data.append(msg)
        return jsonify(msg)
    else:
        return jsonify(data)
