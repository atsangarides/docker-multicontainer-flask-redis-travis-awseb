import os

import redis
from redis import Redis
from rq import Worker, Queue, Connection


listen = ['default']

pool = redis.ConnectionPool(host=os.getenv('REDIS_HOST'), decode_responses=True)
conn = Redis(connection_pool=pool)


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
