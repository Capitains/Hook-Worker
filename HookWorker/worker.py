#!/usr/bin/env python3
import os
from rq import Queue, Connection, Worker
import redis
from sys import argv

# Preload libraries
import HookTest.test

def worker(redis_url="localhost:6379"):
    """ Run a work for python-rq

    :param redis_url: Redis URI (redis://SOMETHING)
    :type redis_url:None
    :return: Nothing
    """
    redis_url = "redis://{0}".format(redis_url)
    conn = redis.from_url(redis_url)

    with Connection(conn):
        qs = [Queue()]

        w = Worker(qs)
        w.work()


if __name__ == "__main__":
    worker()