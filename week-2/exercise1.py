import urllib
import requests

targetUrl = 'https://developer.mozilla.org/en-US/'
userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'

try:
  urr = urllib.request.urlopen(targetUrl)
  content = urr.read()
  urr.close()
  html = content.decode()
  with open('urllib-output.txt', 'w') as output:
    output.write(html)
  
  rer = requests.get(targetUrl)
  print('requests status code: {0}'.format(rer.status_code))
  html = rer.text
  with open('requests-output.txt', 'w') as output:
    output.write(html)
except Exception as err:
  print(err)