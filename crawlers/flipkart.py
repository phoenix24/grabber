#!/usr/bash/env python

from crawler import *

class FlipkartInventory(Crawler):
    """ flipkart inventory page crawler. """
    
    def __init__ (self, content, url):
        super(FlipkartInventory, self).__init__(content, url)
        
    def get_item_color(self, item):
        try:
            return "%s, %s " %  (
                (item.fetch('td', 'fk-item-specs-label')[0].string).strip(),
                (item.fetch('td', 'lastUnit')[0].string).strip()
                )
        except:
            return 'NA'

    def get_item_specifications(self, item):
        return ', '.join([x.string.strip() for x in item.fetch('li')])
        
    def get_item_delivery_days(self, item):
        return "%s, %s " %  (
            (item.fetch('span', 'shipping-period')[0].string).strip(),
            (item.fetch('span', 'free-hm-dlvry')[0].string).strip()
            )

    def get_item_stock_status(self, item):
        return (item.fetch('span', 'search-shipping')[0].string).strip()

    def get_item_price(self, item):
        return (item.fetch('b', 'fksd-bodytext price final-price')[0].string).strip()

    def get_item_name(self, item):
        return (item.fetch('a', 'fk-srch-title-text')[0].string).strip()

    def get_item_image(self):
        return (item.fetch('a', 'fk-srch-title-text')[0].string).strip()
    
    def list_inventory(self):
        """ fetch a list of inventory items. """
        items = self.pagesp.fetch('div', 'fk-srch-item')
        for index, item in enumerate(items):
            try :
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


