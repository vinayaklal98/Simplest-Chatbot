from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import Request
import re

def searching(want):
    
    query = want
    query = query.split()
    query = "+".join(query)
    
    query = 'http://www.google.com/search?q='+query
    #print(query)
    
    req = Request(query,headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html,'html.parser')
    
    tags = soup('a')
    
    urls = {}
    count = 0
    
    for tag in tags:
        t = tag.get('href')
        m = re.search(r"^/url\?q=(?P<urls>.*)",t)
        if m != None:
            count += 1
            urls[count] = m.group('urls')
    
    return urls

#for key,value in urls.items():
    #print(value)
    #print("++++++++++++++++++++++++++++++++")
