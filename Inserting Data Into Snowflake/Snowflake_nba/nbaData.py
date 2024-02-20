from .loggingConfig import logging
from . import config
from .snowflakeConnection import snowflake_connection


class LoadToStage:

    def __init__(self):
        """
        Initializes the class by creating a Snowflake connection and cursor.
        """
        self.connector = snowflake_connection()
        self.cursor = self.connector.cursor()

    def create_Internal_Stage(self):
        """
        Creates or replaces a stage in Snowflake.
        """
        
        self.cursor.execute(
            """create or replace stage Nba_data_stage
                FILE_FORMAT = (TYPE = csv FIELD_DELIMITER = ',' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1); 
            """)
    
    def put_to_Stage(self,path):
        """
        Puts a file from the specified path to the stage.

        Args:
            path (str): The path of the file to put to the stage.
        """
        self.cursor.execute(f"""put 'file:///{path}' @Nba_data_stage  """)

    def load_to_table(self,tableName):
        """
        Loads data from the stage into the specified table.

        Args:
            tableName (str): The name of the table to load data into.
        """
        query = 'COPY INTO ' + tableName + ' FROM @Nba_data_stage;'
        self.cursor.execute(query)

    def remove_From_Stage(self):
        """
        Removes the stage.
        """
        self.cursor.execute(""" REMOVE @Nba_data_stage;
                            """)
