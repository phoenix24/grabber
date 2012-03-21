#!/usr/bash/env python

from baseparser import *

class InfibeamInventory(BaseParser):
    """ infibeam inventory page crawler. """

    def __init__(self, content):
        super(InfibeamInventory, self).__init__(content)

    def get_items(self):
        return self.pagesp.fetch('ul', 'srch_result portrait')[0].fetch('li')
    
    def get_item_name(self, item):
        return (item.fetch('span', 'title')[0].string).strip()

    def get_item_image(self, item):
        return item.fetch('a')[0].fetch('img')[0]['src']

    def get_item_price(self, item):
        return str(item.fetch('span', 'normal')[0].string.replace(",", "")).strip()

    
class InfibeamCrawler(BaseCrawler):
    """ infibeam inventory page crawler. """

    def __init__(self, config, url):
        super(InfibeamCrawler, self).__init__(config, url)

    
class InfibeamGrabber(BaseGrabber):
    """ infibeam page grabber """

    def __init__(self, config):
        super(InfibeamGrabber, self).__init__(config)
    
    def grab(self):
        inventory = self.grab()
        for index, item in enumerate(inventory):
            print index, item
        
    
