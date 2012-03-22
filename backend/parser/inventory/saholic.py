#!/usr/bash/env python

from backend.parser.baseparser import *

class SaholicInventory(BaseParser):
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
    
class SaholicCrawler(BaseCrawler):
    """ saholic inventory page crawler. """

    def __init__(self, config, url):
        super(SaholicCrawler, self).__init__(config, url)

    
class SaholicGrabber(BaseGrabber):
    """ saholic page grabber """

    def __init__(self, config):
        super(SaholicGrabber, self).__init__(config)
    
    def grab(self):
        return super(SaholicGrabber, self).grab()
        
