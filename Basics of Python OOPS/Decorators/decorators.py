import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

def decorator(func):
    def wrapper():
        logging.info("Before function execution")
        func()
        logging.info("After function execution")
    return wrapper

@decorator
def greet():
    logging.info("Hello, World!")




#--------------------------

def multiply_by_two(func):
    def wrapper(x):
        result = func(x) * 2
        return result
    return wrapper

@multiply_by_two
def add_five(x):
    return x + 5


