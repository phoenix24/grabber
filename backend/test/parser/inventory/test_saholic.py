#!/usr/bin/env python
"""
unit-tests for the parsers.saholic module.
"""
import unittest
from parser.inventory.saholic import SaholicInventory

class TestSaholicInventory(unittest.TestCase):
    
    def setUp(self):
        self.test_data = file("test/data/inventory/test_20120309_144841_saholic.html", "r").read()

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

    
    def test_list_inventory(self):
        si = SaholicInventory(self.test_data)
        actual = si.get_inventory(si.get_items())

        expected = [[u'Alcatel  OT-230D', None, None, None, None, u'949', None]]
        self.assertEquals(expected, actual)

    
    def test_get_item_delivery_days(self):
        si = SaholicInventory(self.test_data)
        actual = si.get_item_delivery_days(si.get_items()[0])

        expected = None
        self.assertEquals(expected, actual)
        

if '__main__' == __name__:
    unittest.main()
