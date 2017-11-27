from flask import Flask 
from flask_mongoalchemy import MongoAlchemy


app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'login'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://mock:root12@ds121726.mlab.com:21726/login'

db = MongoAlchemy(app)

class Example(db.Document):
	name = db.StringField()