#!/usr/bin/env python
"""
unit-tests for the parsers.flipkart module.
"""
import unittest
from mock import Mock, patch
from hashlib import md5
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as bsoup

from backend.parser.inventory import attribute
from backend.parser.inventory.infibeam import InfibeamInventory, InfibeamCrawler, InfibeamGrabber

class TestInfibeamInventory(unittest.TestCase):
    
    def setUp(self):        
        self.test = file("backend/test/data/inventory/test_20120310_055847_infibeam.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('ul', 'srch_result portrait')[0].fetch('li')[0])

        #monkey patching test-data to get the correct minimal test-data 
        self.test_data = str("<ul class='srch_result portrait'>" +  self.test_data + "</ul>")

        #inventory object.
        self.inventory = InfibeamInventory(self.test_data)

        #inventory item to be tested against.
        self.attr = attribute()
        self.item = {
            self.attr.id    : md5( 'IBEAM_Sony Ericsson XPERIA X2 (Black)' ).hexdigest(),
            self.attr.url   : "http://infibeam.com/Mobiles/i-Sony-Ericsson-XPERIA-X2-Slider/P-E-M-Sony-Ericsson-XPERIAX2.html?id=Black",
            self.attr.name  : u'Sony Ericsson XPERIA X2 (Black)',
            self.attr.color : None,
            self.attr.specs : None,
            self.attr.stock : None,
            self.attr.brand : None,
            self.attr.price : u'25767',
            self.attr.source: u'IBEAM',
            self.attr.delivery : None,
            self.attr.image : u'http://cdn-img-a.infibeam.net/img/2ffd0b46/80/22/p-e-m-sony-ericsson-xperiax2-front-1.wm.jpg?op_sharpen=1&wid=120&hei=140'}
        

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
        

    def test_get_item_image(self):
        actual = self.inventory.get_item_image(self.inventory.get_items()[0])
        expected = self.item[ self.attr.image ]
        self.assertEquals(expected, actual)


    def test_get_item_id(self):
        actual = self.inventory.get_item_id(self.inventory.get_items()[0])
        expected = self.item[ self.attr.id ]
        self.assertEquals(expected, actual)

        
    def test_get_item_source(self):
        actual = self.inventory.get_item_source()
        expected = self.item[ self.attr.source ]
        self.assertEquals(expected, actual)


    def test_get_item_url(self):
        actual = self.inventory.get_item_url(self.inventory.get_items()[0])
        expected = self.item[ self.attr.url ]
        self.assertEquals(expected, actual)
        
        
    def test_get_inventory(self):
        actual = InfibeamInventory(self.test_data).get_inventory()
        expected = [ self.item ]
        self.assertEquals(expected, actual)
            

class TestInfibeamCrawler(unittest.TestCase):
            
    def setUp(self):
        self.crawler = InfibeamCrawler({}, "http://localhost/page")

    def tearDown(self):
        self.crawler = None
        
    def test_crawl_page(self):
        self.crawler.crawl_page = Mock(return_value="Mock Page!")
        self.assertEquals("Mock Page!", self.crawler.crawl_page())

        
class TestInfibeamGrabber(unittest.TestCase):
    
    @staticmethod
    def FakeResponse(a):
        test = file("backend/test/data/inventory/test_20120310_055847_infibeam.html", "r").read()
        test_data = str(bsoup(test).fetch('ul', 'srch_result portrait')[0].fetch('li')[0])

        #monkey patching test-data to get the correct minimal test-data 
        test_data = str("<ul class='srch_result portrait'>" + test_data + "</ul>")
        return '200 OK', test_data

        
    @patch.object(Http, 'request', FakeResponse)
    def test_inventory_grab(self):

        grabber = InfibeamGrabber({
                "url" : "http://localhost/page",
                "parser" : InfibeamInventory,
                "crawler" : InfibeamCrawler
                })

        inventory = grabber.grab()
        self.assertEquals(1, len(inventory))


if '__main__' == __name__:
    unittest.main()
