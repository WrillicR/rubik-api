import unittest
import app


class SbomTest(unittest.TestCase):


    def test_sbom_author_name(self):
        my_name = "wgr0009"
        result_author_dict = app._getAuthor("../../")
        result_author = result_author_dict["author"]
        self.assertEqual(my_name,result_author)
        