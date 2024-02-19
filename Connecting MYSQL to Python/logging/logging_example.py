import logging

#creating custom Logger
logger = logging.getLogger(__name__)

#crating handler
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("This is a warning")
logger.error("This is an error")

#The name of the logger corresponding to the __name__ variable is logged as __main__, 
#which is the name Python assigns to the module where execution starts.

