#!/usr/bash/env python

from crawler import *

class SaholicInventory(Crawler):
    """ saholic inventory page. """

    def __init__(self, content, url):
        super(SaholicInventory, self).__init__(content, url)
        
    def get_item_delivery_days(self, item):
        return 'NA'

    def get_item_price(self, item):
        return (item.fetch('span', 'newPrice')[1].string).strip()

    def get_item_name(self, item):
        return (item.fetch('div', 'title')[0].fetch('a')[0].string).strip()
    
    def list_inventory(self):
        """ fetch inventory items list. """
        items = self.pagesp.fetch('div', 'productItem')
        for index, item in enumerate(items):
            try:
                print "%s.  %-25s | %-10s | %s | | %s | %s" % (
                    index,
                    self.get_item_name(item),
                    self.get_item_price(item),
                    self.get_item_stock_status(item),
                    self.get_item_delivery_days(item),
                    #self.get_item_specifications(item),
                    self.get_item_color(item)
                    )
            except:
                pass
            
