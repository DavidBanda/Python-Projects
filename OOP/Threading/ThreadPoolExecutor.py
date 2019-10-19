import concurrent.futures
import time

start = time.perf_counter()
print(f'start: {start}')


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


# only two threads with arguments
'''
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)

    print(f1.result())
    print(f2.result())
'''

# ten threads with arguments
'''
with concurrent.futures.ThreadPoolExecutor() as executor:

    secs = [5, 4, 3, 2, 1]

    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
'''

# ten threads with arguments. Map built-in function
with concurrent.futures.ThreadPoolExecutor() as executor:

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


finish = time.perf_counter()
print(f'finish: {finish}')

print(f'Finished in {round(finish-start, 2)} second(s)')



