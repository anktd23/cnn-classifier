import os
import logging
from datetime import datetime

#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"

#log file dir
LOG_FILE_DIR = os.path.join(os.getcwd(),'logs')

#create directory if not avilable
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)


logging.basicConfig(filename = LOG_FILE_PATH,
                    level=logging.INFO,
                    format='[%(asctime)s]-%(name)s-%(lineno)d-%(levelname)s- %(message)s')