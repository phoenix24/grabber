#!/usr/bash/env python

import os
import sys
import logging
from datetime import datetime
from httplib2 import Http
from parser.inventory.settings import SHOPS

if __name__ == '__main__':

    print "preparing test-data set"
    tstamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    handle = Http(".cache")

    for shop, info in SHOPS.iteritems():

        if info["pages"] and info["mobile"] != "":
            
            shop_txt, shop_url = "%s/test/data/test_%s_%s.html" % (os.getcwd(), tstamp, shop), info["mobile"] % "1"
            print shop_txt, shop_url

            resp, content = handle.request( shop_url )
            output = open(shop_txt, "w")
            output.write(content)
            output.close()

