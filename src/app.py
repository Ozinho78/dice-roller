from flask import jsonify, render_template
from typing import Any
from . import create_app
from .api import dices

# app = Flask(__name__)
app = create_app()



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


# if __name__ == '__main__':
#     app.run(debug=True)