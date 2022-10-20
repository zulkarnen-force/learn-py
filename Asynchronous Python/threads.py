from asyncio import futures
from concurrent.futures import Future, thread
from re import T
from threading import Thread
import time

def thread_fetching(sleep_time: int):
    print(f"Start Fetching threads...")
    time.sleep(sleep_time)
    print('Fetching Complete!')
    return {'data': 'example data from thread'}
    
def thread_print_numbers():
    for i in range(10):
        print(i)
        time.sleep(0.5)

thread_1 = Thread(target=thread_fetching, args=(2,))
thread_2 = Thread(target=thread_print_numbers)


def start_threads(threads: list[Thread]):
    start_time = time.perf_counter()
    
    threads[0].start()
    threads[1].start()
    
    threads[0].join()
    threads[1].join()
    
           
    end_time = time.perf_counter()
    
    print(f'[Finished threads in{end_time-start_time: 0.2f}s]')
    
    
def run_main_threads():
    start_threads([thread_1, thread_2])

# run_main_threads()


def foo(data: str) -> dict :
    print(f'start {data.__str__}')
    time.sleep(2)
    print('complete processing')
    return {'message': data}

def run_threadpool(fn, *argv):
    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(3)
    async_result = pool.apply_async(fn, [n for n in argv])

    # DO Something other stuff in main process
    for i in range(10):
        print(i)
        time.sleep(0.5)
        
    return_value = async_result.get()
    print(return_value)
    
# run_threadpool(foo, 'ini message')


# CONCURRENT FUTURES

import concurrent.futures as futures

with futures.ThreadPoolExecutor(2) as executor:
    future = executor.submit(foo, 'this message futures')
    
    thread_print_numbers()
    
    print('outer task')
    return_value = future.result()
    print(return_value)
    
    
def is_done(future: Future):
    print(future.done())


is_done(future=future)
