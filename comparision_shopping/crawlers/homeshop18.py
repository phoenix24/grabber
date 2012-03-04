#!/usr/bash/env python

import os
import sys
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as soup



class FlipkartInventory(object):
    def __init__ (self, content):
        self.content = content
        self.pagesp = soup(content)
    
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
                    #                self.get_item_specifications(item),
                    self.get_item_color(item)
                    )
            except:
                pass


def scrape_flipkart_mobiles(strtpage = 1, endpage = 3, nextpg = True):
    handle = Http(".cache")

    for page in range(strtpage, endpage):
        url_to_fetch = "http://flipkart.com/mobiles/all/%s?layout=list" % page
        print "fetching ", url_to_fetch
        
        resp, content = handle.request( url_to_fetch )
        fki = FlipkartInventory(content)
        fki.list_inventory()

#        pagesp = soup(content)
#        nextpg = pagesp.fetch('a', 'nav_bar_next_prev')[0].next.strip()       
#        if not nextpg  == 'Next Page':            break

    
if __name__ == '__main__':
    scrape_flipkart_mobiles(strtpage = 5, endpage = 28)
    
