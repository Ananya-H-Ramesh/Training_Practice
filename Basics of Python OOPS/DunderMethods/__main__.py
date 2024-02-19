''' Main Script Entry Point'''

import logging
from .dunderExample import BankAccount

try:
    #Creating Account object
    acc = BankAccount('AC001', 1000)
    logging.info(acc)

    #Crediting Amount to Balance
    acc += 500
    logging.info(acc)

    #Debiting Amount From Balance
    acc -= 200
    logging.info(acc)

    #Debiting Amount From Balance
    acc -= 1500
    logging.info(acc)

except Exception as err:
    logging.error("Error: %s", err)
    raise Exception(err)