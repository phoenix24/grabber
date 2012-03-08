#!/usr/bash/env python

import logging
from flipkart import FlipkartInventory
from saholic import SaholicInventory


def scrape_inventory(parser, url, strtpage = 1, endpage = 3):

    for page in range(strtpage, endpage):
        url_to_fetch = url % page
        parser('', url_to_fetch).list_inventory()

    
if __name__ == '__main__':

    # fetch flipkart inventory.
    scrape_inventory(FlipkartInventory, strtpage = 1, endpage = 2,
                     url = "http://flipkart.com/mobiles/all/%s?layout=list")

    # fetch saholic inventory.
    scrape_inventory(SaholicInventory, strtpage = 1, endpage = 2,
                     url = "http://www.saholic.com/all-mobile-phones/10001?&page=%s")
