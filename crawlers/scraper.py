#!/usr/bash/env python

import logging
from flipkart import FlipkartInventory


def scrape_flipkart_mobiles(parser, strtpage = 1, endpage = 3, nextpg = True):

    for page in range(strtpage, endpage):
        url_to_fetch = "http://flipkart.com/mobiles/all/%s?layout=list" % page
        
        # logging.info("scrapper fetching " %  url_to_fetch)
        parser('', url_to_fetch).list_inventory()

    
if __name__ == '__main__':
    scrape_flipkart_mobiles(FlipkartInventory,
                            strtpage = 1, endpage = 6, nextpg = False)
    
