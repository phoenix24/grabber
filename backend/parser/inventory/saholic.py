#!/usr/bash/env python

from backend.parser.inventory.baseinventory import *

class SaholicInventory(BaseInventory):
    """ saholic inventory page. """

    def __init__(self, content):
        super(SaholicInventory, self).__init__(content)
        
    def get_items(self):
        return self.pagesp.fetch('div', 'productItem')

    def get_item_price(self, item):
        return (item.fetch('span', 'newPrice')[1].string).strip()

    def get_item_name(self, item):
        return (item.fetch('div', 'title')[0].fetch('a')[0].string).strip()

    def get_item_image(self, item):
        return item.fetch('div', 'productImg')[0].fetch('img')[0]['src']
    
    def get_item_url(self, item):
        url = (item.fetch('div', 'title')[0].fetch('a')[0]['href']).strip()
        return "http://saholic.com" + url

    def get_item_source(self):
        return 'SHOLIC'

class SaholicCrawler(BaseCrawler):
    """ saholic inventory page crawler. """

    def __init__(self, config):
        super(SaholicCrawler, self).__init__(config)

    
class SaholicGrabber(BaseGrabber):
    """ saholic page grabber """

    def __init__(self, config):
        super(SaholicGrabber, self).__init__(config)
    
    def grab(self):
        return super(SaholicGrabber, self).grab()
        
