# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
pos = int(input('Enter position - '))
repeat = int(input('Enter repeat time - '))
while(repeat > 0):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    list_url = []
    for tag in tags:
        list_url.append(tag.get('href', None))
    print(list_url[pos-1])
    url = list_url[pos-1]
    repeat -= 1
