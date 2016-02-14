# -*- coding: utf-8 -*-
from cookielib import CookieJar

import os
import sys
import urllib
import unicodedata
import re
import urllib2
import struct
import shutil
import StringIO
import gzip
from BeautifulSoup import BeautifulSoup

try:
    import xbmc
    import xbmcvfs
    import xbmcaddon
    import xbmcplugin
    import xbmcgui
	
except ImportError:
    from stubs import xbmc, xbmcgui, xbmcaddon, xbmcplugin, xbmcvfs

__addon__ = xbmcaddon.Addon()
__scriptid__ = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString