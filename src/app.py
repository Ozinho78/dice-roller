from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dices")
def handle_dices():
    return "Look at these beautiful dices"


@app.route("/hello")
@app.route("/hello/<string:name>")
def hello_world(name: str = None):
    return render_template("hello.html", _name=name)