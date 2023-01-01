from flask import Flask,request,Blueprint,jsonify
from flask_restful import Api,marshal_with,fields
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
import jwt


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://deva:deva@localhost/flask'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'your secret key'

#run "flask test"
@app.cli.command('test')
def test():
    print('work')

from api import routes
from api import models