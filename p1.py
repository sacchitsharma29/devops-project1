from flask import Flask

app=Flask(__name__)

@app.route("/index")
def home():
    return "welcome to the LW"

@app.route("/exit")
def bye():
    return"BYE BYE"

app.run(host="0.0.0.0")
