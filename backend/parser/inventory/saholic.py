#!/usr/bash/env python

from parser import *

class SaholicInventory(Parser):
    """ saholic inventory page. """

    def __init__(self, content):
        super(SaholicInventory, self).__init__(content)
        
    def get_items(self):
        return self.pagesp.fetch('div', 'productItem')

    def get_item_price(self, item):
        return (item.fetch('span', 'newPrice')[1].string).strip()

    def get_item_name(self, item):
        return (item.fetch('div', 'title')[0].fetch('a')[0].string).strip()
    
