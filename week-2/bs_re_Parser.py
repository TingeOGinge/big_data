#pseudo html example from beautifulsoup documentation
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html
#please check the functions one by one to see if you know how to parse/extract the data you need - Dalin
from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

soup = bs(html_doc, 'lxml')
#print(soup.prettify())

print(soup.p)
#only return the first tag p if there are multiple ones
print(soup.head)
print(soup.find_all(['p','a']))
#filter all the tags
print(soup.select('head'))
print(soup.select('.sister'))
print(soup.select('p[class=title]'))
print(soup.select('p[class="title"]'))
print(soup.select('p > a'))
print(soup.select('body > a'))
print(soup.select('body > p > a'))
#select using tags, atrributes, classes and combinations


for link in soup.find_all('a'):
    print(link.get('href'))
#get the 'href' attribute value from all items with tag 'a'
    
print(soup.get_text())

#tools like beautifulsoup are great for those with good attribute allocations
#for complex pages, please use regular expressions

#a simple regular expression
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)