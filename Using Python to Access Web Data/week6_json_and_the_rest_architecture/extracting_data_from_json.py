import json
import urllib.request, urllib.error

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_803339.json'
output = urllib.request.urlopen(url).read()

info = json.loads(output)
total = 0
for i in info['comments']:
    total += i['count']

print(total)
