import json

from flask import Flask, jsonify, request

# data = requests.post("http://192.168.0.106:5000/", data=json.dumps({'k': 'v'}))

app = Flask(__name__)

data = []


@app.route("/", methods=["GET", "POST"])
def main():

    if request.method == "POST":
        msg = json.loads(request.data)
        data.append()
        return jsonify(msg)
    else:
        return jsonify(data)
