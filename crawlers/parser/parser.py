#!/usr/bin/env python

import os
import sys
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as soup

class Crawler(object):
    """ the abstract crawler class!  """
    
    def __init__ (self, content, url):
        self.url = url
        handle = Http(".cache")
        
        self.resp, self.content = handle.request( self.url )
        self.pagesp = soup(self.content)

    def get_item_color(self, item):
        return 'NA'

    def get_item_specifications(self, item):
        return 'NA'
        
    def get_item_delivery_days(self, item):
        return 'NA'

    def get_item_stock_status(self, item):
        return 'NA'

    def get_item_price(self, item):
        return 'NA'

    def get_item_name(self, item):
        return 'NA'

    def get_item_image(self, item):
        return 'NA'
    
    def list_inventory(self, content):
        return 'NA'

