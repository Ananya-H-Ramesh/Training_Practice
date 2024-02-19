''' Main Script Entry Point'''

import logging
from .snowflakeConnector import *


if __name__ == '__main__':

    try:
        connection = connect_to_snowflake()
    except Exception as e:
        logging.error(f"Error Occured while Connecting to SnowFlake : {e}")
    else:
        cursor = connection.cursor()
        result = cursor.execute("Select Top 5 * from nba_db")
        for row in result:
            logging.info(row)
    finally:
        logging.info(connect_to_snowflake.retry.statistics)
