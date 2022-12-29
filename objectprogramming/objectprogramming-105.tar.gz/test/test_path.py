# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116


"path tests"


import unittest


from op import fntime


FN = "store/op.handler.Event/a1eb7b9506914aa0bec3caa2d51f3746/2022-04-11/22:40:31.259218"


class TestPath(unittest.TestCase):


    def test_path(self):
        fnt = fntime(FN)
        self.assertEqual(fnt, 1649709631.259218)
