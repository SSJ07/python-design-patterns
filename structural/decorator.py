"""
Decorator design pattern

-> Structural design pattern
-> It allows to attach new behavior to the existing object by placing these objects inside special wrapper objects
    that contain the behavior
-> Decorator design pattern used mostly for:
    1. Data validation
    2. Caching
    3. Logging
    4. Monitoring
    5. Debugging
    6. Business rules
    7. Encryption
"""
import time
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fib_cache(func) -> object:
    cache = dict()

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]

    return wrapper


def fib_logger(func) -> object:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        logger.info(f"Logging info: {args}, kwargs: {kwargs}")
        logger.info(f"Calling: {func.__name__}")
        resp = func(*args, **kwargs)
        logger.info(f"Function resp is: {resp}")
        return resp

    return wrapper


@fib_logger
@fib_cache
def fibonacci(number) -> int:
    a, b = 0, 1
    while number > 1:
        a, b = b, a + b
        number -= 1
    return b


if __name__ == '__main__':
    s = time.time()
    logger.info(fibonacci(90000))
    e = time.time()
    logger.info(f"First time taken: {(e - s)}")

    logger.info(fibonacci(90000))
    e1 = time.time()
    logger.info(f'Second time took: {(e1 - e)}')
