''' Main Script Entry Point'''

import logging
from .constructors import Person

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

if __name__ == '__main__':
    try:
        #creating Person Object
        person1 = Person()
        person2 = Person("Alice", 25)
        
        person1.display_info()
        person2.display_info()

    except Exception as err:
        logging.error("Error: %s", err)
        raise Exception(err)