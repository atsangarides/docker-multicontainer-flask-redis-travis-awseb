import os
import logging

from redis import Redis
from rq import Worker, Queue, Connection


listen = ['high', 'default', 'low']

conn = Redis(host=os.getenv('REDIS_WORKER_HOST'), port=int(os.getenv('REDIS_WORKER_PORT')))
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
