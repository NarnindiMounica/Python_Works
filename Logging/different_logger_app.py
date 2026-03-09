import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler("Logging/arthimetic_app.log"),
              logging.StreamHandler()
]
)

logger1=logging.getLogger("application_logs")
logger1.setLevel(logging.INFO)

def add(a:int, b:int):
    logger1.info("summing function execution")
    return a+b

def subtract(a:int, b:int):
    logger1.info("subtraction function execution")
    return a-b
logger1.info("app completed..")

print(add(2,3))
print(subtract(4,2))