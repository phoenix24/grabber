#!/usr/bin/env python

import os
import sys
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as bsoup

from hashlib import md5
from pymongo.connection import Connection


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

    def get_item_brand(self, item):
        return None

    def get_item_url(self, item):
        return None

    def get_item_source(self):
        return None

    def get_item_id(self, item):
        name = "%s_%s" % (self.get_item_source(), self.get_item_name(item))
        return md5(name).hexdigest()
    

    def get_item_inventory(self, item):
        inventory = {}
        try:
            inventory = {
                "name"  : self.get_item_name(item),
                "color" : self.get_item_color(item),
                "specs" : self.get_item_specifications(item),
                "delivery" : self.get_item_delivery_days(item),
                "stock" : self.get_item_stock_status(item),
                "price" : self.get_item_price(item),
                "image" : self.get_item_image(item),
                "brand" : self.get_item_brand(item),
                "source": self.get_item_source(),
                "url"   : self.get_item_url(item),
                "id"    : self.get_item_id(item)
                }
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

        self.db_name = "grabber"
        self.db_host = "localhost"

        self.connection = Connection(self.db_host)
        self.db = self.connection[self.db_name]
        
                

    def grab(self):
        # save url+crawled page.
        url = self.config['url']
        crawler = self.crawler(self.config, url)

        # save parsed content.
        parser = self.parser( crawler.crawl_page() )
        
        return parser.get_inventory()

    def dump(self):
        inventory = self.grab()
        self.db.inventory.insert(inventory)
        
