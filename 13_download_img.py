import urllib.request as urlrequest
from bs4 import BeautifulSoup
from os.path import basename
import urllib.parse as urlparse
import re

web_url = 'http://tieba.baidu.com/p/2166231880'
def getpage(web_url=web_url):
    urlcontent = urlrequest.urlopen(web_url).read()
    web_page = re.findall(r'http:.+\.jpg',urlcontent)
    return int(web_page[0])

print(getpage())
