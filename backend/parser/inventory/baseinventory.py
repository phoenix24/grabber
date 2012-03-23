#!/usr/bin/env python

from backend.parser.baseparser import *

class BaseInventory(BaseParser):
    """ the abstract parser class!  """
    
    def __init__ (self, content):
        self.pagesp = bsoup(content)
        self.content = content
        self.inventory = []
        super(BaseInventory, self).__init__(content)

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
                "_id"   : self.get_item_id(item)
                }
        except:
            pass
        return inventory
    
    def get_inventory(self):
        for item in self.get_items():
            self.inventory.append(self.get_item_inventory(item))
        return self.inventory

