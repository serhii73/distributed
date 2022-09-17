from time import sleep

from flask import Flask, jsonify, request

# r = requests.post("http://localhost:9000/", data=json.dumps({'k': 'v'}))
# r = requests.get("http://localhost:9000/")

app = Flask(__name__)

data = []
start_id = 0


def compare_ids(start_id, msg_id):
    if msg_id == start_id:
        return True
    return False


@app.route("/", methods=["GET", "POST"])
def main():

    if request.method == "POST":
        global start_id
        msg = request.json.get("message")
        msg_id = request.json.get("msg_id")
        data.append(msg)
        while compare_ids(start_id, msg_id) is not True:
            sleep(1)
        start_id += 1
        return jsonify(msg)
    else:
        return jsonify(data)
