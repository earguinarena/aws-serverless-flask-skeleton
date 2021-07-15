from flask import jsonify, request
from application import app
from example import service as service_example
from support.exceptions import UndefinedExampleException
# from support.json_loader import load_json

BASE_ROUTE = "/examples"


@app.route(BASE_ROUTE, methods=["GET"])
def get_example():
    try:
        # example_id = request.environ["event"]["requestContext"]["authorizer"]["claims"]["cognito:username"]
        return jsonify(service_example.get_examples())
    except UndefinedExampleException:
        return jsonify("undefined_example"), 400
    except Exception as e:
        print(e)
        return jsonify(str(e)), 500


@app.route(f"{BASE_ROUTE}/<string:example_id>", methods=["GET"])
def get_by_id(example_id):
    try:
        # example_id = request.environ["event"]["requestContext"]["authorizer"]["claims"]["cognito:username"]
        return jsonify(service_example.get_example(example_id))
    except UndefinedExampleException:
        return jsonify("undefined_example"), 400
    except Exception as e:
        print(e)
        return jsonify(str(e)), 500