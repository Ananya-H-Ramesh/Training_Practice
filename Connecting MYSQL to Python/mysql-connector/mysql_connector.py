import mysql.connector
import logging
from .config import mysql_config
from tenacity import retry, stop_after_attempt, wait_fixed

logging.basicConfig(level=logging.INFO,
                    format = "%(process)s %(levelname)s %(message)s"
                    )

@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def connect_mysql():
        '''Connecting to MySQL '''
        mydb = mysql.connector.connect(
                user=mysql_config['user'],
                password=mysql_config['password'],
                host=mysql_config['host']
        )
        return mydb




