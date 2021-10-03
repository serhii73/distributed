from flask import Flask

MSG = "The test message"
app = Flask(__name__)


@app.route("/")
def get_msg():
    return f"{MSG}\n"


if __name__ == "__main__":
    app.run(port=5684)
