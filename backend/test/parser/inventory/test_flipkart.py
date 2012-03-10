#!/usr/bin/env python
"""
unit-tests for the parsers.flipkart module.
"""
import unittest
from BeautifulSoup import BeautifulSoup as bsoup
from parser.inventory.flipkart import FlipkartInventory

class TestFlipkartInventory(unittest.TestCase):
    
    def setUp(self):
        self.test = file("test/data/inventory/test_20120309_144841_flipkart.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('div', 'fk-srch-item')[0])

    def tearDown(self):
        self.test_data = None
        
        
    def test_get_items(self):
        fki = FlipkartInventory(self.test_data)
        self.assertEquals(1, len(fki.get_items()))


    def test_get_item_color(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_color(fki.get_items()[0])

        expected = 'Grey'
        self.assertEquals(expected, actual)
        

    def test_get_item_specifications(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_specifications(fki.get_items()[0])

        expected = u'Android v2.3 OS, 2 MP Primary Camera, 3-inch Touchscreen, FM Radio'
        self.assertEquals(expected, actual)

    
    def test_get_item_delivery_days(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_delivery_days(fki.get_items()[0])

        expected = u'2-4 business days. Free Home Delivery.'
        self.assertEquals(expected, actual)

    
    def test_get_item_stock_status(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_stock_status(fki.get_items()[0])

        expected = u'In Stock.'
        self.assertEquals(expected, actual)
        
        
    def test_get_item_price(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_price(fki.get_items()[0])

        expected = '7650'
        self.assertEquals(expected, actual)
        
        
    def test_get_item_name(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_name(fki.get_items()[0])

        expected = u'Samsung Galaxy Y S5360'
        self.assertEquals(expected, actual)
        

    def test_get_item_image(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_item_image(fki.get_items()[0])

        expected = u'http://img1.flixcart.com//image/mobile/4/4/4/samsung-galaxy-y-s5360-125x125-imad2pzjx3uq8paz.jpeg'
        self.assertEquals(expected, actual)

    
    def test_get_inventory(self):
        fki = FlipkartInventory(self.test_data)
        actual = fki.get_inventory(fki.get_items())

        expected = [[u'Samsung Galaxy Y S5360',
                     u'Grey',
                     u'Android v2.3 OS, 2 MP Primary Camera, 3-inch Touchscreen, FM Radio',
                     u'2-4 business days. Free Home Delivery.',
                     u'In Stock.',
                     u'7650',
                     u'http://img1.flixcart.com//image/mobile/4/4/4/samsung-galaxy-y-s5360-125x125-imad2pzjx3uq8paz.jpeg']
                    ]
        self.assertEquals(expected, actual)
            

if '__main__' == __name__:
    unittest.main()