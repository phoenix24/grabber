#!/usr/bash/env python

from crawler import Crawler

class LetsBuyInventory(Crawler):
    def __init__ (self, content, url):
        super(LetsBuyInventory, self).__init__(content, url)
    
    def get_item_specifications(self, item):
        return  item.fetch('p')[0].string
    
    def get_item_discount_save(self, item):
        try:
            return (item.fetch('span', 'save-bg')[0].string)
        except:
            return 'NA'
        
    def get_item_price(self, item):
        return (item.fetch('span', 'text12_stb')[0].string)

    def get_item_name(self, item):
        return (item.fetch('h2', 'green')[0].fetch('a')[0].string).strip()
    
    def list_inventory(self):
        """ fetch a list of inventory items. """
        items = self.pagesp.fetch('div', 'search_products')
        for index, item in enumerate(items):
            print "%s. %s %s %s"  % (
                index,
                self.get_item_name(item),
                self.get_item_price(item),
                self.get_item_discount_save(item),
                )
    
if __name__ == '__main__':
    url_to_fetch = "http://www.letsbuy.com/mobile-phones-mobiles-c-254_88ve"
    print "fetching ", url_to_fetch
    
    #content = open("../test/data/letsbuy.html").read()
    
    lsb = LetsBuyInventory('', url_to_fetch)
    lsb.list_inventory()
