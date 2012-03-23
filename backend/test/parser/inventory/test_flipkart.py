#!/usr/bin/env python
"""
unit-tests for the parsers.flipkart module.
"""
import unittest
from hashlib import md5
from httplib2 import Http
from mock import Mock, patch
from BeautifulSoup import BeautifulSoup as bsoup

from backend.parser.inventory import attribute
from backend.parser.inventory.flipkart import FlipkartCrawler, FlipkartGrabber, FlipkartInventory

class TestFlipkartInventory(unittest.TestCase):
    
    def setUp(self):        
        self.test = file("backend/test/data/inventory/test_20120310_055847_flipkart.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('div', 'fk-srch-item')[0])
        self.inventory = FlipkartInventory(self.test_data)
        
        self.attr = attribute()
        
        self.item  = {
            self.attr.name  : u'Samsung Galaxy Y S5360',
            self.attr.color : u'Grey',
            self.attr.specs : u'Android v2.3 OS, 2 MP Primary Camera, 3-inch Touchscreen, FM Radio',
            self.attr.stock : u'In Stock.',
            self.attr.price : u'7650',
            self.attr.image : u'http://img1.flixcart.com//image/mobile/4/4/4/samsung-galaxy-y-s5360-125x125-imad2pzjx3uq8paz.jpeg',
            self.attr.brand : None,
            self.attr.delivery : u'2-4 business days. Free Home Delivery.',
            self.attr.source : u'FKART',
            self.attr.url    : u'http://flipkart.com//samsung-galaxy-y-s5360-mobile-phone/p/itmd2pz2rpcg5smz/search-mobile-/1?pid=mobd2pyzfanvw444&ref=c337db2d-b97a-4b4b-9061-bf3705435edd&_l=HmmZvbFeU9Oo4NUBP6Fi6Q--&_r=t2xsnCM8eE1pqUPoLth04Q--',
            self.attr.id     : md5( 'FKART_Samsung Galaxy Y S5360' ).hexdigest()
         }
        

    def tearDown(self):
        self.item = None
        self.test = None
        self.test_data = None
        self.inventory = None
        
        
    def test_get_items(self):
        self.assertEquals(1, len(self.inventory.get_items()))


    def test_get_item_color(self):
        actual = self.inventory.get_item_color(self.inventory.get_items()[0])
        expected = self.item[ self.attr.color ]
        self.assertEquals(expected, actual)
        

    def test_get_item_specifications(self):
        actual = self.inventory.get_item_specifications(self.inventory.get_items()[0])
        expected = self.item[ self.attr.specs ]
        self.assertEquals(expected, actual)

    
    def test_get_item_delivery_days(self):
        actual = self.inventory.get_item_delivery_days(self.inventory.get_items()[0])
        expected = self.item[ self.attr.delivery ]
        self.assertEquals(expected, actual)

    
    def test_get_item_stock_status(self):
        actual = self.inventory.get_item_stock_status(self.inventory.get_items()[0])
        expected = self.item[ self.attr.stock ]
        self.assertEquals(expected, actual)
        
        
    def test_get_item_price(self):
        actual = self.inventory.get_item_price(self.inventory.get_items()[0])
        expected = self.item[ self.attr.price ]
        self.assertEquals(expected, actual)
        
        
    def test_get_item_name(self):
        actual = self.inventory.get_item_name(self.inventory.get_items()[0])
        expected = self.item[ self.attr.name ]
        self.assertEquals(expected, actual)
        

    def test_get_item_image(self):
        actual = self.inventory.get_item_image(self.inventory.get_items()[0])
        expected = self.item[ self.attr.image ]
        self.assertEquals(expected, actual)


    def test_get_item_url(self):
        actual = self.inventory.get_item_url(self.inventory.get_items()[0])
        expected = self.item[ self.attr.url ]
        self.assertEquals(expected, actual)

        
    def test_get_item_id(self):
        actual = self.inventory.get_item_id(self.inventory.get_items()[0])
        expected = self.item[ self.attr.id ]
        self.assertEquals(expected, actual)

        
    def test_get_item_source(self):
        actual = self.inventory.get_item_source()
        expected = self.item[ self.attr.source ]
        self.assertEquals(expected, actual)
        
    
    def test_get_inventory(self):
        actual = self.inventory.get_inventory()
        expected = [self.item]
        self.assertEquals(expected, actual)
            

        
class TestFlipkartCrawler(unittest.TestCase):
            
    def setUp(self):
        self.crawler = FlipkartCrawler({ "url" : "http://localhost/page" })

    def tearDown(self):
        self.crawler = None
        
    def test_crawl_page(self):
        self.crawler.crawl_page = Mock(return_value="Mock Page!")
        self.assertEquals("Mock Page!", self.crawler.crawl_page())

        

class TestFlipkartGrabber(unittest.TestCase):

    def setUp(self):
        self.grabber = FlipkartGrabber({
                "url" : "http://localhost/page",
                "parser" : FlipkartInventory,
                "crawler" : FlipkartCrawler,
                "dbname" : "GrabberTest",
                "dbhost" : "localhost",
                "source" : "FKART"
                })
        self.grabber.db.pages.drop()
        self.grabber.db.inventory.drop()
        
    def tearDown(self):
        self.grabber.db.pages.drop()
        self.grabber.db.inventory.drop()
        
    @staticmethod
    def FakeResponse(a):
        test = file("backend/test/data/inventory/test_20120310_055847_flipkart.html", "r").read()
        test_data = str(bsoup(test).fetch('div', 'fk-srch-item'))
        return '200 OK', test_data

    
    @patch.object(Http, 'request', FakeResponse)
    def test_inventory_grab(self):
        # kick inventory grabber.
        self.grabber.grab()
        
        #assert inventory insertion
        self.assertEquals(10, self.grabber.db.inventory.count())

        #assert page insertion
        self.assertEquals(1, self.grabber.db.pages.count())

        
if '__main__' == __name__:
    unittest.main()
