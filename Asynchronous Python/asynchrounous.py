import asyncio, time
from typing import Coroutine, Literal



async def foo(text: str):
    print(text)
    await asyncio.sleep(2);
    print('foo')


async def main():
    print('zul')
    task = asyncio.create_task(foo('hello'))
    print('finished')

    

def run(main_coroutine):
    start = time.perf_counter()
    asyncio.run(main_coroutine())
    end = time.perf_counter()
    print(f'[Finished in{end-start: 0.2f}s]')

run(main)
    
# function ```main()``` akan mengembalikan Coroutine Object
# print(main()) 

# asyncio.run(main())



async def fetch_data():
    print('Start Fetching...')
    await asyncio.sleep(2)
    print('Done Fetching!')
    return {'status': 200}
    
async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    task_2 = asyncio.create_task(print_numbers())
    task_1 = asyncio.create_task(fetch_data())
    data = await asyncio.gather(task_1, task_2)
    print(data)
    print(asyncio.get_event_loop())
    
    
run(main)
