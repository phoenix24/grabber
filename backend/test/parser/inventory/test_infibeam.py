#!/usr/bin/env python
"""
unit-tests for the parsers.flipkart module.
"""
import unittest
from BeautifulSoup import BeautifulSoup as bsoup
from parser.inventory.infibeam import InfibeamInventory

class TestInfibeamInventory(unittest.TestCase):
    
    def setUp(self):
        self.test = file("test/data/inventory/test_20120310_055847_infibeam.html", "r").read()
        self.test_data = str(bsoup(self.test).fetch('ul', 'srch_result portrait')[0].fetch('li')[0])

        #monkey patching test-data to get the correct minimal test-data 
        self.test_data = str("<ul class='srch_result portrait'>" +  self.test_data + "</ul>")

    def tearDown(self):
        self.test_data = None
        
        
    def test_get_items(self):
        ibi = InfibeamInventory(self.test_data)
        self.assertEquals(1, len(ibi.get_items()))


    # def test_get_item_specifications(self):
    #     ibi = InfibeamInventory(self.test_data)
    #     actual = ibi.get_item_specifications(ibi.get_items()[0])

    #     expected = u'Android v2.3 OS, 2 MP Primary Camera, 3-inch Touchscreen, FM Radio'
    #     self.assertEquals(expected, actual)

    # def test_get_item_price(self):
    #     ibi = InfibeamInventory(self.test_data)
    #     actual = ibi.get_item_price(ibi.get_items()[0])

    #     expected = '7650'
    #     self.assertEquals(expected, actual)
        
        
    def test_get_item_name(self):
        ibi = InfibeamInventory(self.test_data)
        actual = ibi.get_item_name(ibi.get_items()[0])

        expected = u'Sony Ericsson XPERIA X2 (Black)'
        self.assertEquals(expected, actual)
        

    def test_get_item_image(self):
        ibi = InfibeamInventory(self.test_data)
        actual = ibi.get_item_image(ibi.get_items()[0])

        expected = u'http://img1.flixcart.com//image/mobile/4/4/4/samsung-galaxy-y-s5360-125x125-imad2pzjx3uq8paz.jpeg'
        self.assertEquals(expected, actual)

    
    # def test_get_inventory(self):
    #     ibi = InfibeamInventory(self.test_data)
    #     actual = ibi.get_inventory(ibi.get_items())

    #     expected = [[u'Samsung Galaxy Y S5360',
    #                  u'Grey',
    #                  u'Android v2.3 OS, 2 MP Primary Camera, 3-inch Touchscreen, FM Radio',
    #                  u'2-4 business days. Free Home Delivery.',
    #                  u'In Stock.',
    #                  u'7650',
    #                  u'http://img1.flixcart.com//image/mobile/4/4/4/samsung-galaxy-y-s5360-125x125-imad2pzjx3uq8paz.jpeg']
    #                 ]
    #     self.assertEquals(expected, actual)
            

if '__main__' == __name__:
    unittest.main()
