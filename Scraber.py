'''
            DEVELOPER NAME : BALAVIGNESH.M

            IMPLEMENTATION DATE : 27/12/2018

            SCOPE OF IMPLEMENTATION : scrab the html data what ever you want by using this scabber

'''

#Importing the logger & file Handler


from tools import logger as log 
from tools import file_handler as pyfile

#Importing the main tools for scapy

from urllib.request import urlopen as urls
from bs4 import BeautifulSoup as BS 


# Class declaration
class ScaberPy:

    def __init__(self):
        pyfile.Clear_all_http_isses()

    #Function for Getting page full source content
    def GetSourceHTML(self):
        urlb = str(input("URL : "))
        filename = str(input("Filename : "))
        source_c = urls(urlb)
        bsobj = BS(source_c.read(),'html.parser')
        pyfile.write_content_from_page(filename,str(bsobj))

    def Shutdown(self):
        quit()




# Instatnce creation
scapytrix = ScaberPy()

# Choice Requestion
print("Enter the choice 1 for GetPageSource.")
print("Enter the choice 5 for Quit")


# Action_Dispatcher for access the required functionalities
def Action_Dispatcher(contoller):
    {
        1 : scapytrix.GetSourceHTML,
        5 : scapytrix.Shutdown
    }.get(contoller,"sorry not able to perform")()
        

# choice assker
while True:
    choice = int(input("Enter the choice:"))
    Action_Dispatcher(choice)

  
        




