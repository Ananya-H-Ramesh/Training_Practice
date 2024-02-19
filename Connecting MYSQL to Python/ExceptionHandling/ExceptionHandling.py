import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

x=5
y="Hello"
try:
    z=x+y
except TypeError:
    logging.error("Cannot add an integer to String")

#-----------------
    
a=[1,2,3]
try:
    logging.info("Second Element : ",a[1])
    logging.info("Fourth Element : ",a[3])
except:
    logging.error("An error occured")

#----------------------------

def fun(a):
    if a < 4:
        b = a/(a-3)
    logging.info("Value of b :",b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    logging.error("Zero Division Error")
except NameError:
    logging.error("Name Error")

#-------------------

def function(a,b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        logging.error("a/b results in Zero")
    else:
        logging.info(c)

function(2,3)
function(3,3)

#-----------------

try:
    a = 5//0
    logging.info(a)
except ZeroDivisionError:
    logging.error("Zero Division Error ")
finally:
    logging.info("Finally is Always Executed")
    

#---------------
    
try:
    raise NameError("Hello")
except NameError:
    logging.error("An Exception")
    raise