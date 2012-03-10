#!/usr/bin/env python

import os
import sys
from httplib2 import Http
from BeautifulSoup import BeautifulSoup as soup


class BaseCrawler(object):
    """ the abstract crawler class!  """
    
    def __init__ (self, content, url):
        self.url = url
        handle = Http(".cache")
        
        self.resp, self.content = handle.request( self.url )
        self.pagesp = soup(self.content)


    def get_content(self):
        return self.content

    
