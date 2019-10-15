from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'c93b4e3cdcc2c8c10177034aae6e22d8'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


from flaskblog import routes