import snowflake.connector
import logging
from SnowflakeConnector.configuration import snowflake_config
from tenacity import retry, stop_after_attempt, wait_fixed



logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def connect_to_snowflake():
    '''Connecting to Snowflake'''
    cnn = snowflake.connector.connect(
        user = snowflake_config['user'],
        password=snowflake_config['password'],
        account = snowflake_config['account'],
        database= snowflake_config['database']
    )
    return cnn

    
