from flask import Flask
from flask_cors import CORS

from app.controllers.v1 import version1

application = Flask(__name__)

cors = CORS(application, resources={r"/*": {"origins": "*"}}, support_credentials=True)
application.config["CORS_HEADERS"] = 'application/json'
application.register_blueprint(version1,url_prefix="/twitter-sentiment-analysis/v1")




