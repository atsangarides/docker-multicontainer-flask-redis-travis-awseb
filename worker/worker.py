import os
from redis import Redis

r = Redis(host=os.environ.get('REDIS_HOST'))
sub = r.pubsub()
sub.subscribe('insert')


def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# keep listening on channel
for new_message in sub.listen():
    fib_index = new_message['data']
    fib_num = Fibonacci(int(fib_index))
    r.hset('values', fib_index, fib_num)
