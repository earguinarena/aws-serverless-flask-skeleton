from flask import Flask
from support.json_encoder import CustomJsonEncoder
from flask_cors import CORS, cross_origin
import logging
from flask import request


logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.json_encoder = CustomJsonEncoder
cors = CORS(app)


@app.before_request
def log_request_info():
    app.logger.info(request.method + ' ' + request.full_path)
    # app.logger.info('User: %s', request.environ["event"]["requestContext"]["authorizer"]["claims"]["cognito:username"])
    # app.logger.info('Event-> Request Context: %s', request.environ["event"]["requestContext"])
    # app.logger.info('Headers: %s', request.headers)
    app.logger.info('Body: %s', request.get_data())


from example import handler
