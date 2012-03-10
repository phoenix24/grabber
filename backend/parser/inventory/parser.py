#!/usr/bin/env python

import os
import sys
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as bsoup

class Parser(object):
    """ the abstract crawler class!  """
    
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
    
    def get_inventory(self, items):
        for item in items:
            self.inventory.append(self.get_item_inventory(item))
        return self.inventory


