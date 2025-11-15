from flask import Flask, jsonify, render_template, request
from typing import Any

app = Flask(__name__)
dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20}
]


def wrap_template_rendering(template_name: str, **context: Any):
    return render_template(template_name, _author="Michael", **context)
    

@app.route("/")
def home():
    # return render_template("home.html", _author="Michael")
    # return wrap_template_rendering("home.html", _author="Michael")
    return wrap_template_rendering("home.html")


@app.route("/dices")
def handle_dices():
    # return "Look at these beautiful dices"
    return wrap_template_rendering("dice.html", _dices=dices)


@app.route("/hello")
@app.route("/hello/<string:name>")
def hello_world(name: str = None):
    # return render_template("hello.html", _name=name)
    return wrap_template_rendering("hello.html", _name=name)


@app.route("/api/sample")
def return_sample_json():
    return {"key": "value"}


@app.route("/api/alt")
def return_alternate_json():
    # return jsonify(foo="bar") # erzeugt JSON
    return jsonify(foo=["bar", "baz", "sample"])



@app.route("/api/dices", methods=["GET", "POST"])
def handle_dice_requests():
    # return jsonify(available_dices=dices)
    if request.method == "GET":
        return jsonify(available_dices=dices)
    # POST request handling
    else:
        try:
            payload = request.json
            
            if not payload["numberOfSides"]:
                raise Exception()
            if not payload["numberOfSides"] > 1:
                raise Exception()
            
            new_dice = {"numberOfSides": payload["numberOfSides"]}
            
            if new_dice in dices:
                raise Exception()
            
            dices.append(new_dice)
            
            return {"message": "dice created"}, 201
        
        except:
            return {"message": "An Unknown Error occured"}, 500
        
    
