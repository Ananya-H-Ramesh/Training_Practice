import logging
from .snowflakeDataIntoDF import *\


if __name__ == '__main__':

    try:
        connection = connect_to_snowflake()
    except Exception as e:
        logging.error(f"Error Occured while Connecting to SnowFlake : {e}")
    else:
        cursor = connection.cursor()
        cursor.execute("Select * from nba_db")
        df = cursor.fetch_pandas_all()
        transform(df)
       
    finally:
        logging.info(connect_to_snowflake.retry.statistics)

    
        
