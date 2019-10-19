import time

start = time.perf_counter()
print(f'start: {start}')


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


do_something()
do_something()

finish = time.perf_counter()
print(f'finish: {finish}')

print(f'Finished in {round(finish-start, 2)} second(s)')



