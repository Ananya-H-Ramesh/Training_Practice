import logging

logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt= "%y-%m-%d %H:%M:%S",
        filename="Schedule/log_info.log"
    )


logging.info("Script ran Now \n")

