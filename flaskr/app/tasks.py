import os
import logging

from redis import Redis

r = Redis(host=os.getenv('REDIS_SERVER_HOST'), port=int(os.getenv('REDIS_SERVER_PORT')))


def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def fetch_fibonacci(n):
    logging.info(f'Received task for index: {n}')
    fib_num = Fibonacci(n)
    logging.info(f'Setting value for index: {n}')
    r.hset('values', str(n), fib_num)
