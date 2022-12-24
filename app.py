from flask import Flask, request, jsonify
import time

def timestamp():
    # ts stores the time in seconds
    ts = time.time()
    # print the current timestamp
    return ts

app = Flask(__name__)

@app.route("/", methods=["GET"])
def list():
    content = timestamp()
    return jsonify(content)



if __name__ == "__main__":
    app.run(debug=True)
