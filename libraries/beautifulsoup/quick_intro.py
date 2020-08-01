# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

##### 快速开始

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
"""

# import the bs4 library 
# (why there's bs4.BeautifulSoup? why not just "import bs4"?)
from bs4 import BeautifulSoup

# create an instance of class BeautifulSoup, from the above doc
soup = BeautifulSoup(html_doc, 'html.parser')

# have a look!
print(soup.prettify())
print()

# easily browse certain kinds of data
print("soup.title", soup.title)
print("soup.title.name", soup.title.name)
print("soup.title.string", soup.title.string)
print("soup.title.parent.name", soup.title.parent.name)

print()

print("soup.p", soup.p)
print("soup.p['class']", soup.p['class'])

print()

print("soup.a", soup.a)
print("soup.find_all('a')", soup.find_all('a'))
print("soup.find(id='link3')", soup.find(id="link3"))

# find all links that have <a> label
for link in soup.find_all('a'):
    print(link.get('href'))
    
# get all text content from the doc
print(soup.get_text())