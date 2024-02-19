''' Main Script Entry Point'''

import logging
from .mysql_connector import connect_mysql

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )

if __name__ == '__main__':
    connection = connect_mysql()

    try:
        mycursor = connection.cursor()
        
    except Exception as e :
          logging.error("Error Occured while connecting : {e}")
    else:
          mycursor.execute("show databases")
          for row in mycursor:
                print(row)
    finally:
          print(connect_mysql.retry.statistics)
          
        
