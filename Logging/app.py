from logger import logging

def sum(a:int, b:int)->int:
    logging.info("function execution started")
    c = a + b
    logging.info("getting result")

    return c

logging.info("function execution ended")


sum(10,20)