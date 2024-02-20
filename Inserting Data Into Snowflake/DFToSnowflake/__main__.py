''' Main Script Entry Point'''
import logging
from .config import snowflake_config
from .DFToSnowflake import DFToSnowflake

if __name__ == '__main__':
    try:
        df_snowflake = DFToSnowflake
        df_snowflake.df_to_Snowflake()

    except Exception as err:
        logging.error("Error: %s", err)
        raise Exception(err)