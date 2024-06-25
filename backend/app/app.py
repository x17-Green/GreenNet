#!/usr/bin/python3
# App Configs

from flask import Flask

app = Flask(__name__)
@app.route("/")

def index():
    return "Welcome to GreenNet"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3440, debug=True)