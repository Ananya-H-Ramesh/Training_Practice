''' Main Script Entry Point'''
import logging
from .RetryDecorators import *

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

if __name__ == '__main__':
    try:
        data = connect_to_database()
        logging.info(f"Data retrieved successfully {data}")
    
    except Exception as e:
        logging.error('Failed to connect to database ', e)

    finally:
        logging.info(connect_to_database.retry.statistics)