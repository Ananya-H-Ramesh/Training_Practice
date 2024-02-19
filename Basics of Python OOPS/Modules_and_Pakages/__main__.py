''' Main Script Entry Point'''

import logging
from .main import main
logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        logging.error("Error: %s", err)
        raise Exception(err)