from app import something_else
from flask.ext.sqlalchemy import SQLAlchemy
import os
import flask

app = flask.Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy()


@app.route("/posts/new")
def posts_new():
    return flask.jsonify(name='')

something_else = 5

if __name__ == '__main__':
    app.run()


#RDMS
#Marathon
#Luigi Internals
#Mock out instance