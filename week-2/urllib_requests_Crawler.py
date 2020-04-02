import urllib, requests
#import re
#headers ommitted here
urr = urllib.request.urlopen('https://www.port.ac.uk/')
content = urr.read()
urr.close()
html1 = content.decode()
#print(html1)

rer = requests.get('https://www.port.ac.uk/')
print(rer.status_code)
html2 = rer.text
print(html2)

print(type(urr))
print(type(rer))

print(type(html1))
print(type(html2))

#Check if the html1 and html2 are having the same contents in them.
#If not, identify the difference yourself.

#response = urllib.request.urlopen('https://www.port.ac.uk/study/subject-area/computing').read().decode()
#reString = '<a href=.*>(.*?)</a>'
#pattern = re.compile(reString)
#print(pattern.findall(response))

#print('\n'*3)
#reString2 = '<a href=.*data-gtm-vis-has-fired-9152982_32="1">(.*?)</a>'
#pattern2 = re.compile(reString2)
#print(pattern2.findall(response))