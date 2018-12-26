#LOGGING CONFIGURATION
import logging as log

def File_log_info(filename):
    log.basicConfig(filename=filename, level=log.INFO)

def GenReport(e:Exception):
    log.exception(str(e))

    