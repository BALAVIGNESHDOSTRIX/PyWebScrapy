from urllib.request import urlopen 
from bs4 import BeautifulSoup

content = urlopen('http://www.bbc.com/')
bs_obj = BeautifulSoup(content.read(), 'html.parser')

print(bs_obj.h1.string)