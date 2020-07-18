from routes import *
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


# app configuration
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(
    # Set the secret key to a sufficiently random value
    SECRET_KEY=os.urandom(24),
    DEBUG=True
)

# initialise the cursor
db = SQLAlchemy(app)

from routes import *

if __name__ == "__main__":
    app.run()
