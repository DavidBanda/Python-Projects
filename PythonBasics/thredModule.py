import threading
from queue import Queue
import time

print_lock = threading.Lock()
q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('entire job took:', time.time()-start)