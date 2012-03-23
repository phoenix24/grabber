#!/usr/bash/env python

from itertools import chain

from parser.inventory import SHOPS
from parser.inventory.saholic import *
from parser.inventory.flipkart import *
from parser.inventory.infibeam import *


if __name__ == '__main__':

    # fkart.
    fkg = FlipkartGrabber({
            "url" : SHOPS["flipkart"]["mobile"] % "1",
            "parser" : FlipkartInventory,
            "crawler" : FlipkartCrawler
            })

    
    # inbeam
    ibi = InfibeamGrabber({
            "url" : SHOPS["infibeam"]["mobile"] % "1",
            "parser" : InfibeamInventory,
            "crawler" : InfibeamCrawler
            })
    
    # sholic
    shc = SaholicGrabber({
            "url" : SHOPS["saholic"]["mobile"] % "1",
            "parser" : SaholicInventory,
            "crawler" : SaholicCrawler
            })
    
    

    # for index, item in enumerate(chain(fkg.grab(), ibi.grab(), shc.grab())):
    #     print index, item

    print "dumping fkart data."
    fkg.dump()
