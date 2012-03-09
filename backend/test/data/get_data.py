#!/usr/bash/env python

import os
import sys
import logging
from httplib2 import Http
from datetime import datetime
from parser.tours import TOURS
from parser.inventory import SHOPS


def fetch_inventory_test_pages(handle, tstamp):

    for shop, info in SHOPS.iteritems():
        if info["pages"] and info["mobile"] != "":
            shop_txt = "%s/test/data/inventory/test_%s_%s.html" % (os.getcwd(), tstamp, shop)
            shop_url = info["mobile"] % "1"
            try:
                print shop_txt, shop_url
                resp, content = handle.request( shop_url )
                output = open(shop_txt, "w")
                output.write(content)
                output.close()
            except:
                pass


def fetch_tours_test_pages(handle, tstamp):

    for shop, info in TOURS.iteritems():
        if info["pages"] and info["urls"]:
            for count, shop_url in enumerate(info["urls"]):
                shop_txt = "%s/test/data/tours/test_%s_%s_%s.html" % (os.getcwd(), count, tstamp, shop)
                try:
                    print shop_txt, shop_url
                    resp, content = handle.request( shop_url )
                    output = open(shop_txt, "w")
                    output.write(content)
                    output.close()
                except:
                    pass


if __name__ == '__main__':
    handle = Http(".cache")        

    print "preparing tours-test-data-set : ", datetime.now().strftime("%Y%m%d_%H%M%S") 
    fetch_tours_test_pages(handle,
                           datetime.now().strftime("%Y%m%d_%H%M%S"))
    
    print "preparing inventory-test-data-set : ", datetime.now().strftime("%Y%m%d_%H%M%S")
    fetch_inventory_test_pages(handle,
                               datetime.now().strftime("%Y%m%d_%H%M%S"))
