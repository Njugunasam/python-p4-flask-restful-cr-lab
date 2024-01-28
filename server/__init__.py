

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/plants.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import the Plant model to ensure it is recognized by Flask-Migrate
from server.models import Plant

# Additional configurations, routes, etc., can be added below

if __name__ == '__main__':
    app.run(debug=True)
