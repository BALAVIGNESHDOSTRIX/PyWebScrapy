import os
import ssl
from datetime import datetime as ts 
from . import logger as log

#SOLVE THE HTTP & HTTPS ISSUES
def Clear_all_http_isses():
    if not os.environ.get('PYTHONHTTPSVERIFY','') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

#WRITE THE HTML CONTENT TO REQUIRED FILE
def write_content_from_page(filename,data):
    try:
        with open("Html/" + filename +'.html','w') as file:
            file.write(data)
        print("Successfully writed")
    except Exception as e:
        log.File_log_info('Error/' + filename + '.log')
        log.GenReport(e)
        print(e)

