import logging

name = "Ananya"
logging.error("%s raised an error",name)

#Capturing Stack traces

a=5
b=0

try:
    c = a/b
except Exception as e :
    logging.error("Exception Occured",exc_info=True)

#use logging.exception() if you are logging from an exception handler

x=10
y=0
try:
    z = x/y
except Exception as e :
    logging.exception("Exception Occured") 

 #Using logging.exception() would show a log at the level of ERROR. 
    #If you don’t want that, you can call any of the other logging functions from debug() to critical() and pass the exc_info parameter as True. 

#Classes and Functions

logger = logging.getLogger('ex_logger')
logger.warning("it's a warning") 
 