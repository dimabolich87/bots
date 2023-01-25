import requests
import lxml.html
from lxml import etree


tree = etree.parse('python.org.html', lxml.html.HTMLParser())
ul = tree.findall('/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[1]/a')

for li in ul:
    a = li.find('a')

print(a.text)