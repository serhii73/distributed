import json

from flask import Flask, jsonify, request

# r = requests.post("http://localhost:10000/", data=json.dumps({'k': 'v'}))
# r = requests.get("http://localhost:10000/")

app = Flask(__name__)

data = []


@app.route("/", methods=["GET", "POST"])
def main():

    if request.method == "POST":
        msg = request.json.get("message")
        msg_id = request.json.get("msg_id")
        data.append(msg)
        return jsonify(msg)
    else:
        return jsonify(data)
