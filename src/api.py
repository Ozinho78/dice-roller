from flask import Blueprint, jsonify, request
from .errors import InvalidDiceError, DiceAlreadyExistsError

api_bp = Blueprint("api", __name__)

dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 20}
]

@api_bp.route("/dices", methods=["GET"])
def get_dices():
    return jsonify(available_dices=dices)


@api_bp.route("/dices", methods=["POST"])
def create_dice():
    try:
        payload = request.json

        if not payload or "numberOfSides" not in payload:
            raise InvalidDiceError("Payload must contain 'numberOfSides'.")
        if payload["numberOfSides"] <= 1:
            raise InvalidDiceError()

        new_dice = {"numberOfSides": payload["numberOfSides"]}

        if new_dice in dices:
            raise DiceAlreadyExistsError()

        dices.append(new_dice)
        return {"message": "dice created"}, 201

    except InvalidDiceError as e:
        return {"message": e.message}, 400
    except DiceAlreadyExistsError as e:
        return {"message": e.message}, 409
    except Exception as e:
        return {"message": "An unexpected error occurred."}, 500



@api_bp.route("/sample")
def return_sample_json():
    return {"key": "value"}


@api_bp.route("/alt")
def return_alternate_json():
    # return jsonify(foo="bar") # erzeugt JSON
    return jsonify(foo=["bar", "baz", "sample"])
  
  
# @api_bp.route("/dices", methods=["GET", "POST"])
# def handle_dice_requests():
#     # return jsonify(available_dices=dices)
#     if request.method == "GET":
#         return jsonify(available_dices=dices)
#     # POST request handling
#     else:
#         try:
#             payload = request.json
            
#             if not payload["numberOfSides"]:
#                 raise Exception()
#             if not payload["numberOfSides"] > 1:
#                 raise Exception()
            
#             new_dice = {"numberOfSides": payload["numberOfSides"]}
            
#             if new_dice in dices:
#                 raise Exception()
            
#             dices.append(new_dice)
            
#             return {"message": "dice created"}, 201
        
#         except:
#             return {"message": "An Unknown Error occured"}, 500

