from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "welcome to the bebop"

@app.route("/exit")
def bye():
    return"See You Space Cowboy"

app.run(host="0.0.0.0")
