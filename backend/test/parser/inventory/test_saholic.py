#!/usr/bin/env python
"""
unit-tests for the parsers.saholic module.
"""
import unittest
from mock import Mock
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as bsoup
from backend.parser.inventory.saholic import SaholicInventory, SaholicCrawler, SaholicGrabber

class TestSaholicInventory(unittest.TestCase):
    
    def setUp(self):
        self.test = file("backend/test/data/inventory/test_20120310_055847_saholic.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('div', 'productItem')[0])

    def tearDown(self):
        self.test_data = None
        
        
    def test_get_items(self):
        si = SaholicInventory(self.test_data)
        self.assertEquals(1, len(si.get_items()))


    def test_get_item_price(self):
        si = SaholicInventory(self.test_data)
        actual = si.get_item_price(si.get_items()[0])

        expected = '949'
        self.assertEquals(expected, actual)
        
        
    def test_get_item_name(self):
        si = SaholicInventory(self.test_data)
        actual = si.get_item_name(si.get_items()[0])

        expected = 'Alcatel  OT-230D'
        self.assertEquals(expected, actual)

    
    def test_get_item_delivery_days(self):
        si = SaholicInventory(self.test_data)
        actual = si.get_item_delivery_days(si.get_items()[0])

        expected = None
        self.assertEquals(expected, actual)

        
    def test_get_item_image(self):
        si = SaholicInventory(self.test_data)
        actual = si.get_item_image(si.get_items()[0])

        expected = u"http://static2.saholic.com/images/media/1001720/alcatel-ot-230d-icon-1313564847734.jpg"
        self.assertEquals(expected, actual)

        
    def test_get_inventory(self):
        actual = SaholicInventory(self.test_data).get_inventory()
        expected = [[u'Alcatel  OT-230D',
                     None,
                     None,
                     None,
                     None,
                     u'949',
                     u"http://static2.saholic.com/images/media/1001720/alcatel-ot-230d-icon-1313564847734.jpg"]]
        self.assertEquals(expected, actual)

        

class TestSaholicCrawler(unittest.TestCase):
            
    def setUp(self):
        self.crawler = SaholicCrawler({}, "http://localhost/page")

    def tearDown(self):
        self.crawler = None
        
    def test_crawl_page(self):
        self.crawler.crawl_page = Mock(return_value="Mock Page!")
        self.assertEquals("Mock Page!", self.crawler.crawl_page())

        
class TestSaholicGrabber(unittest.TestCase):
    
    def setUp(self):
        self.test = file("backend/test/data/inventory/test_20120310_055847_saholic.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('div', 'productItem')[0])

    def tearDown(self):
        self.test_data = None
        
    def test_get_items(self):
        fki = SaholicInventory(self.test_data)
        self.assertEquals(1, len(fki.get_items()))

        
if '__main__' == __name__:
    unittest.main()
