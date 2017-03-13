#!/usr/local/bin/python3

# this smaple for thread creation.

from queue import Queue
from threading import Thread
import time


q = Queue(maxsize=0)
num_thread = 10


# Perform Functional Activity
def do_stuff(q):
    while True:
        time.sleep(3)
        print(q.get())
        q.task_done()


# Creating the Queue for Operations.
for x in range(30):
    print('Creating Queue of', x)
    q.put(x)

print('Successfully Created the Queues')

for y in range(num_thread):
    worker = Thread(target=do_stuff, args=(q,))
    worker.setDaemon(True)
    worker.start()

q.join()
