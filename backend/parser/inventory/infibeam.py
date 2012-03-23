#!/usr/bin/env python

from backend.parser.inventory.baseinventory import *

class InfibeamInventory(BaseInventory):
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

    def get_item_url(self, item):
        url = (item.fetch('a')[0]['href']).strip()
        return "http://infibeam.com%s" % url

    def get_item_source(self):
        return "IBEAM"


    
class InfibeamCrawler(BaseCrawler):
    """ infibeam inventory page crawler. """

    def __init__(self, config):
        super(InfibeamCrawler, self).__init__(config)

    
class InfibeamGrabber(BaseGrabber):
    """ infibeam page grabber """

    def __init__(self, config):
        super(InfibeamGrabber, self).__init__(config)
    
    def grab(self):
        return super(InfibeamGrabber, self).grab()
    
