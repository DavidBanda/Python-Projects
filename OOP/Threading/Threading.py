import threading
import time

start = time.perf_counter()
print(f'start: {start}')


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done sleeping...')


# only two threads without arguments

# t1 = threading.Thread(target=do_something, args=[1])
# t2 = threading.Thread(target=do_something, args=[1])

# start threads and run methods
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


# ten threads with arguments

# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()
print(f'finish: {finish}')

print(f'Finished in {round(finish-start, 2)} second(s)')



