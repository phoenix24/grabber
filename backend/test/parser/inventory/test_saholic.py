#!/usr/bin/env python
"""
unit-tests for the parsers.saholic module.
"""
import unittest
from mock import Mock, patch
from hashlib import md5
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as bsoup

from backend.parser.inventory import attribute
from backend.parser.inventory.saholic import SaholicInventory, SaholicCrawler, SaholicGrabber

class TestSaholicInventory(unittest.TestCase):
    
    def setUp(self):
        self.test = file("backend/test/data/inventory/test_20120310_055847_saholic.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('div', 'productItem')[0])
        self.inventory = SaholicInventory(self.test_data)

        self.attr = attribute()
        self.item = {
            self.attr.name  : u'Alcatel  OT-230D',
            self.attr.id    : md5( 'SHOLIC_Alcatel  OT-230D' ).hexdigest(),
            self.attr.url   : u'http://saholic.com/mobile-phones/alcatel-ot-230d-1001720',
            self.attr.specs : None,
            self.attr.color : None,
            self.attr.brand : None,
            self.attr.stock : None,
            self.attr.source: u'SHOLIC',
            self.attr.price : u'949',
            self.attr.image : u"http://static2.saholic.com/images/media/1001720/alcatel-ot-230d-icon-1313564847734.jpg",
            self.attr.delivery : None
            }
        
        
    def tearDown(self):
        self.item = None
        self.test = None
        self.test_data = None
        self.inventory = None
        
        
    def test_get_items(self):
        self.assertEquals(1, len(self.inventory.get_items()))


    def test_get_item_price(self):
        actual = self.inventory.get_item_price(self.inventory.get_items()[0])
        expected = self.item[ self.attr.price ]
        self.assertEquals(expected, actual)
        
        
    def test_get_item_name(self):
        actual = self.inventory.get_item_name(self.inventory.get_items()[0])
        expected = self.item[ self.attr.name ]
        self.assertEquals(expected, actual)

    
    def test_get_item_delivery_days(self):
        actual = self.inventory.get_item_delivery_days(self.inventory.get_items()[0])
        expected = self.item[ self.attr.delivery ]
        self.assertEquals(expected, actual)

        
    def test_get_item_image(self):
        actual = self.inventory.get_item_image(self.inventory.get_items()[0])
        expected = self.item[ self.attr.image ]
        self.assertEquals(expected, actual)

        
    def test_get_item_url(self):
        actual = self.inventory.get_item_url(self.inventory.get_items()[0])
        expected = self.item[ self.attr.url ]
        self.assertEquals(expected, actual)


    def test_get_item_source(self):
        actual = self.inventory.get_item_source()
        expected = self.item[ self.attr.source ]
        self.assertEquals(expected, actual)


    def test_get_item_id(self):
        actual = self.inventory.get_item_id(self.inventory.get_items()[0])
        expected = self.item[ self.attr.id ]
        self.assertEquals(expected, actual)

        
    def test_get_inventory(self):
        actual = SaholicInventory(self.test_data).get_inventory()
        expected = [ self.item ]
        self.assertEquals(expected, actual)
        

class TestSaholicCrawler(unittest.TestCase):
            
    def setUp(self):
        self.crawler = SaholicCrawler({ "url" : "http://localhost/page" })

    def tearDown(self):
        self.crawler = None
        
    def test_crawl_page(self):
        self.crawler.crawl_page = Mock(return_value="Mock Page!")
        self.assertEquals("Mock Page!", self.crawler.crawl_page())

        
class TestSaholicGrabber(unittest.TestCase):

    def setUp(self):
        self.grabber = SaholicGrabber({
                "url" : "http://localhost/page",
                "parser" : SaholicInventory,
                "crawler" : SaholicCrawler,
                "dbname" : "GrabberTest",
                "dbhost" : "localhost",
                "source" : "IBEAM"
                })
        self.grabber.db.pages.drop()
        self.grabber.db.inventory.drop()
        
    def tearDown(self):
        self.grabber.db.pages.drop()
        self.grabber.db.inventory.drop()
    
    @staticmethod
    def FakeResponse(a):
        test = file("backend/test/data/inventory/test_20120310_055847_saholic.html", "r").read()
        test_data = str(bsoup(test).fetch('div', 'productItem')[0])
        return '200 OK', test_data
    
    @patch.object(Http, 'request', FakeResponse)
    def test_inventory_grab(self):
        # kick inventory grabber.
        self.grabber.grab()
        
        #assert inventory insertion
        self.assertEquals(1, self.grabber.db.inventory.count())

        #assert page insertion
        self.assertEquals(1, self.grabber.db.pages.count())

        
if '__main__' == __name__:
    unittest.main()
