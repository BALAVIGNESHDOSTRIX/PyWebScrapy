from tools import logger as log 
from tools import file_handler as pyfile

from urllib.request import urlopen as urls
from bs4 import BeautifulSoup as BS 

class ScaberPy:

    def __init__(self):
        pyfile.Clear_all_http_isses()

    def GetSourceHTML(self,url,filename):
        source_c = urls(url)
        bsobj = BS(source_c.read(),'html.parser')
        pyfile.write_content_from_page(filename,str(bsobj))



scapytrix = ScaberPy()

scapytrix.GetSourceHTML('http://www.bbc.com/','bbc.html')
