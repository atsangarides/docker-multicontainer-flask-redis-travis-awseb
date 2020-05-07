import os

from redis import Redis

r = Redis(host=os.getenv('REDIS_HOST'))

def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def fetch_fibonacci(n):
    fib_num = Fibonacci(n)
    r.hset('values', str(n), fib_num)