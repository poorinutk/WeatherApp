from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# Initialize app
app = Flask(__name__)

# Set SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

# Turn off track modifications (it's deprecated)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set secret key (to use messages)
app.config['SECRET_KEY'] = 'e1bc9ace66f8f5c5f4679b05e4b4c4753c33d9e08ed'

db = SQLAlchemy(app)

from weather_app import routes
