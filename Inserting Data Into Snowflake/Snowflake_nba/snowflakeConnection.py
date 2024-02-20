from . import config
import snowflake.connector
from .loggingConfig import logging
from .config import snowflake_config


def snowflake_connection():
    '''Connecting to Snowflake'''

    try:
        connector = snowflake.connector.connect(
            user = snowflake_config['user'],
            password= snowflake_config['password'],
            account = snowflake_config['account'],
            database = snowflake_config['database'],
            schema = snowflake_config['schema']
        )

    except :
        logging.error("Failed to Connect to Snowflake")
        
    else:
         return connector
    
   

