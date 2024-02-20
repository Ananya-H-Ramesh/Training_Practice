import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
from .config import snowflake_config
from . import constants
import logging

logging.basicConfig(level=logging.INFO,
                    format = "%(levelname)s %(message)s"
                    )


class DFToSnowflake:
    '''This Class Loads Dataframe to a Snowflake Table'''

    def df_to_Snowflake():
            """
            Read a CSV file into a pandas DataFrame and write it to a Snowflake database.
            Logs the success status, number of chunks, and number of rows written to the Snowflake table using logging.

            Returns:
                None
            """

            df = pd.read_csv(constants.path,sep = ',',header=0,index_col = False)
            df.reset_index(drop=True,inplace=True)
            logging.info(df.head(3))

            cnn = snowflake.connector.connect(
                        user = snowflake_config['user'],
                        password=snowflake_config['password'],
                        account = snowflake_config['account'],
                        database= snowflake_config['database'],
                        schema = 'public'
                    )
                    
            success , nchunks , nrows, _ = write_pandas(cnn,df,'airport',quote_identifiers=False)
            logging.info(str(success) + ", " + str(nchunks) + " ," + str(nrows))