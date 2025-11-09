from flask import Flask, render_template

app = Flask(__name__)



@app.route("/") # Decorator, der auf eine Route verweist, erster Param URL, die auf Flask registriert wird, Code darunter wird dann bei Request auf diese URL ausgeführt
@app.route("/<string:name>")
def hello_world(name: str = None):
    # return "<p>Hello, World!</p>"
    return render_template("hello.html", _name=name)


# @app.route("/<name>")
# def personalized_hello(name):
#     # return f"Hello, {name}"
#     return render_template("hello.html", _name=name)


@app.route("/dices")
def handle_dices():
    return "Look at these beautiful dices"