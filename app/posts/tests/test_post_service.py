import unittest
from app.app import db


class MyTest(unittest.TestCase):

    def setUp(self):
        app = flask.Flask(__name__)
        app.config.from_object("config.DevelopmentConfig")
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()