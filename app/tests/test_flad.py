# import json
# import unittest
# from ..app import app
#
#
# class FladTest(unittest.TestCase):
#
#     def test_new_post(self):
#         app = app.test_client()
#
#         rv = app.get('/posts/new')
#         self.assertEqual(dict(name=''), json.loads(rv.data))