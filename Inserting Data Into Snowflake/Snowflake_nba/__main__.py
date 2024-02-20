import logging
from .nbaData import *
from . import constants


if __name__ == '__main__':
    stage = LoadToStage()
    

    try:
        stage.create_Internal_Stage()

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    else:
        try:
            stage.put_to_Stage(constants.path)
            logging.info("Loaded to Stage")
            stage.load_to_table('nba_db')
            logging.info("Loaded to Table")

        except Exception as e:
            logging.error(f"Error occurred: {e}")

        else:
            stage.remove_From_Stage()
    finally:
        logging.info("Done")
