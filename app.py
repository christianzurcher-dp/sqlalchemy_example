import os
from flask import Flask
import psycopg2

from db import *
from util.blueprints import register_blueprints

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://127.0.0.1:5432/apc"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)


def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

register_blueprints(app)

if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port='8086', debug=True)