import os
import logging

import time
import asyncio
from flask import g, Blueprint, render_template
from rq import Connection, Queue
from redis import Redis

from app import db
from ..tasks import fetch_fibonacci
from ..models import Values
from .forms import IndexForm


home = Blueprint('home', __name__)


# async def fetch_fib_num(f):
#     f_num = None
#     while not f_num:
#         f_num = g.db.hget('values', str(f))
#         time.sleep(0.01)
#     return f_num
#
#
# loop = asyncio.get_event_loop()
#
#
# @home.route('/<int:f>')
# def hello_world(f):
#     if f > 30:
#         return "No, can't do!"
#
#     if not g.db.hexists('values', str(f)):
#         g.db.publish('insert', f)
#
#     f_num = loop.run_until_complete(fetch_fib_num(f))
#
#     return f'For index {f} fibonacci number is: {int(f_num)}'


@home.route('/ping')
def ping():
    return str(g.db.ping())


@home.route('/exists/<int:f>')
def check(f):
    return str(g.db.hexists('values', str(f)))


@home.route('/<int:f>')
def specific_index(f):
    if f > 30:
        return "No, can't do!"

    if not g.db.hexists('values', str(f)):
        job = g.q.enqueue(fetch_fibonacci, f)
        value = Values(number=f)
        db.session.add(value)
        db.session.commit()

        while not job.is_finished:
            time.sleep(0.01)

    f_num = g.db.hget('values', str(f))

    return f'For index {f} fibonacci number is: {int(f_num)}'


@home.route('/', methods=['POST', 'GET'])
def calculator():
    form = IndexForm()

    if form.validate_on_submit():
        f = form.index.data

        logging.info('Checking if value exists')
        if not g.db.hexists('values', str(f)):
            logging.info(f'Index {f} does not exist')
            with Connection(Redis(host=os.getenv('REDIS_WORKER_HOST'),
                                  port=int(os.getenv('REDIS_WORKER_PORT')),
                                  decode_responses=True)
                            ):
                q = Queue()
                logging.info(f'Enqueueing index {f}')
                job = q.enqueue(fetch_fibonacci, f)
            logging.info(f'Adding {f} to postgres')
            value = Values(number=f)
            db.session.add(value)
            db.session.commit()

            logging.info('looping over job status')
            while not job.is_finished:
                time.sleep(1)

    # fetch all indexes from postgres
    indexes = Values.query.with_entities(Values.number).all()
    indexes = sorted([val for val, in indexes])

    # fetch all key, value pairs from redis
    f_dict = g.db.hgetall('values')
    return render_template('home.html', form=form, indexes=str(indexes).strip('[]'), f_dict=f_dict)
