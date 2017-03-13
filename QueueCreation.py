from queue import Queue
import time

q = Queue(maxsize=0)

def do_stuff(q):
    while not q.empty():
        print('My Queue Name:', q.get())
        q.task_done()

for x in range(20):
    time.sleep(1)
    print('Creating Queue :', x)
    q.put(x)

do_stuff(q)
