''' Main Script Entry Point'''

from .decorators import greet,add_five
import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )


if __name__ == '__main__':
    try:
        greet()

        result = add_five(10)
        logging.info(result)

    except Exception as err:
        logging.error("Error: %s", err)
        raise Exception(err)