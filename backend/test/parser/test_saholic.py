#!/usr/bin/env python
"""
unit-tests for the parsers.saholic module.
"""
import unittest
from parser.saholic import SaholicInventory as si

class TestSaholicInventory(unittest.TestCase):
    
    def setUp(self):
        file_data = file("test_albums.json").read()
        self.file_data = json.loads(file_data)
        self.test_data = json.loads(file_data)

        # get a db hanadle.
        self.ml = MusicLibrary("MusicLibraryTest", "localhost")

        #insert test data-into-db.
        self.ml.db.tracks.insert(self.test_data["tracks"])
        self.ml.db.charts.insert(self.test_data["charts"])
        self.ml.db.artists.insert(self.test_data["artists"])
        self.ml.db.playlists.insert(self.test_data["playlists"])


    def unmarshall(self, items):
        result = []
        for item in items:
            del item['_id']
            result.append(item)
        return result

    
    def tearDown(self):
        self.ml.db.tracks.remove()
        self.ml.db.charts.remove()
        self.ml.db.artists.remove()
        self.ml.db.playlists.remove()
        
        
    def test_top_charts(self):        
        expected = self.file_data["charts"]
        actual = self.unmarshall(self.ml.top_charts)
        
        self.assertEquals(expected, actual)
        self.assertEquals(len(expected), len(actual))


if '__main__' == __name__:
    unittest.main()
