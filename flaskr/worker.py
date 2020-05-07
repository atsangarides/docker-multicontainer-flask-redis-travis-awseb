import os

from redis import Redis
from rq import Worker, Queue, Connection


listen = ['default']

conn = Redis(host=os.getenv('REDIS_HOST'))

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
