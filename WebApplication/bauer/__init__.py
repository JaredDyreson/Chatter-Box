from flask import Flask
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from bauer import routes
