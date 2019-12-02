from queue import Queue
import time

q = Queue(maxsize=0)

def do_stuff(q):
    while not q.empty():
        print('Retrieve Item from Queue:', q.get())
        q.task_done()

for x in range(20):
    time.sleep(1)
    print('Creating Item in Queue :', x)
    q.put(x)

do_stuff(q)
