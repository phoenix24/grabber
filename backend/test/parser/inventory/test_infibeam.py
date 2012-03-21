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


    def test_get_item_price(self):
        ibi = InfibeamInventory(self.test_data)
        actual = ibi.get_item_price(ibi.get_items()[0])

        expected = '25767'
        self.assertEquals(expected, actual)
        
        
    def test_get_item_name(self):
        ibi = InfibeamInventory(self.test_data)
        actual = ibi.get_item_name(ibi.get_items()[0])

        expected = u'Sony Ericsson XPERIA X2 (Black)'
        self.assertEquals(expected, actual)
        

    def test_get_item_image(self):
        ibi = InfibeamInventory(self.test_data)
        actual = ibi.get_item_image(ibi.get_items()[0])

        expected = u'http://cdn-img-a.infibeam.net/img/2ffd0b46/80/22/p-e-m-sony-ericsson-xperiax2-front-1.wm.jpg?op_sharpen=1&wid=120&hei=140'
        self.assertEquals(expected, actual)

    
    def test_get_inventory(self):
        actual = InfibeamInventory(self.test_data).get_inventory()

        expected = [[u'Sony Ericsson XPERIA X2 (Black)',
                     None,
                     None,
                     None,
                     None,
                     u'25767',
                     u'http://cdn-img-a.infibeam.net/img/2ffd0b46/80/22/p-e-m-sony-ericsson-xperiax2-front-1.wm.jpg?op_sharpen=1&wid=120&hei=140']
                    ]
        self.assertEquals(expected, actual)
            

if '__main__' == __name__:
    unittest.main()
