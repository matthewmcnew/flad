import flask

app = flask.Flask(__name__)

@app.route("/posts/new")
def posts_new():
    return flask.jsonify(name='')