#!/usr/bin/env python
import sys
# from redis import Redis
# from rq import Queue, Worker, Connection
#
# class Worker:
#     def __init__(self):
#         self.queue_name = ""
#
#     # Returns all workers registered in this connection
#     redis = Redis()
#     workers = Worker.all(connection=redis)
#
#     # Returns all workers in this queue (new in version 0.10.0)
#     queue = Queue('queue_name')
#     workers = Worker.all(queue=queue)
#     worker = workers[0]
#     print(worker.name)
#
# # Provide queue names to listen to as arguments to this script,
# # similar to rq worker
# with Connection():
#
#     w = Worker(qs)
#     w.work()