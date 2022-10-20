# import asyncio

# async def a():
#     print('hello')
#     await asyncio.sleep(5)
#     print('world')
    
# asyncio.run(a())


# import asyncio, time


# async def say_after(delay, what) :
#     await asyncio.sleep(delay)
#     print(what)
    
# async def main():
#     print(f"started at {time.strftime('%X')}")
    
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
    
#     print(f"finished at {time.strftime('%X')}")
    

# asyncio.run(main())

# print('Task')

# import asyncio, time


# async def say_after(delay, what) :
#     await asyncio.sleep(delay)
#     print(what)
    
# async def main():
    
#     task1 = asyncio.create_task(say_after(1, 'hello'))
#     task2 = asyncio.create_task(say_after(2, 'world'))
    
#     print(f"started at {time.strftime('%X')}")
    
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2

#     print(f"finished at {time.strftime('%X')}")
    

# asyncio.run(main())




# import asyncio

# async def nested():
#     return 42

# async def main():
#     # tidak akan terjadi apa-apa jika hanya call "nested()"
#     # nested()
    
#     #kita perlu "await"
#     print(await nested())
    
# asyncio.run(main())


import asyncio


async def nested() :
    return 42;


async def main():
    task = asyncio.create_task(nested())
    print(await task)
    
asyncio.run(main())
    