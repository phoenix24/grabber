#!/usr/bash/env python

from parser import *

class FlipkartInventory(Parser):
    """ flipkart inventory page crawler. """
    
    def __init__ (self, content):
        super(FlipkartInventory, self).__init__(content)
        
    def get_items(self):
        return self.pagesp.fetch('div', 'fk-srch-item')
        
    def get_item_color(self, item):
        return "%s" %  (item.fetch('td', 'lastUnit')[0].string).strip()

    def get_item_specifications(self, item):
        return ', '.join([x.string.strip() for x in item.fetch('li')])
        
    def get_item_delivery_days(self, item):
        return "%s %s" %  (
            (item.fetch('span', 'shipping-period')[0].string).strip(),
            (item.fetch('span', 'free-hm-dlvry')[0].string).strip()
            )

    def get_item_stock_status(self, item):
        return (item.fetch('span', 'search-shipping')[0].string).strip()

    def get_item_price(self, item):
        price = (item.fetch('b', 'fksd-bodytext price final-price')[0].string).strip()
        return price.replace("Rs.", "").strip()

    def get_item_name(self, item):
        return (item.fetch('a', 'fk-srch-title-text')[0].string).strip()

    def get_item_image(self, item):
        return item.fetch('div', 'lastUnit')[0].fetch('img')[0]['src']
    
