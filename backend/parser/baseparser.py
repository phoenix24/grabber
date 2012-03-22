#!/usr/bin/env python

import os
import sys
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as bsoup

class BaseParser(object):
    """ the abstract parser class!  """
    
    def __init__ (self, content):
        self.pagesp = bsoup(content)
        self.content = content
        self.inventory = []


    def get_items(self):
        return None

    def get_item_name(self, item):
        return None

    def get_item_color(self, item):
        return None

    def get_item_specifications(self, item):
        return None
        
    def get_item_delivery_days(self, item):
        return None

    def get_item_stock_status(self, item):
        return None

    def get_item_price(self, item):
        return None

    def get_item_image(self, item):
        return None

    def get_item_inventory(self, item):
        inventory = []
        try:
            inventory = [
                self.get_item_name(item),
                self.get_item_color(item),
                self.get_item_specifications(item),
                self.get_item_delivery_days(item),
                self.get_item_stock_status(item),
                self.get_item_price(item),
                self.get_item_image(item),
                ]
        except:
            pass
        return inventory
    
    def get_inventory(self):
        for item in self.get_items():
            self.inventory.append(self.get_item_inventory(item))
        return self.inventory



class BaseCrawler(object):
    """ the abstract crawler class!  """
    
    def __init__ (self, config, url):
        self.config = config
        self.handle = Http(".cache")

        self.url = url
        self.resp = None
        self.content = None
        
    def crawl_page(self):
        self.resp, self.content = self.handle.request( self.url )
        return self.content
        

class BaseGrabber(object):
    """
    the abstract grabber class!
    # all the book-keeping needs to be done here.
    ## todo : store crawled urls into the db.
    ## todo : store crawled pages into the db.
    ## todo : store extracted inventory into the db.
    """

    def __init__(self, config):
        self.config = config
        self.parser = self.config['parser']
        self.crawler = self.config['crawler']
                
        
    def grab(self):

        url = self.config['url']
        crawler = self.crawler(self.config, url)
        parser = self.parser( crawler.crawl_page() )
        
        return parser.get_inventory()

