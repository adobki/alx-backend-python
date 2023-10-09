#!/usr/bin/env python3
""" This module showcases asynchronous coroutines in Python """
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def enqueue(queue: asyncio.Queue, max_delay: int) -> None:
    """ Adds a task to an asyncio queue for concurrent execution """
    await queue.put(await task_wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """ Returns the wait times in an automatically sorted list """
    queue = asyncio.Queue()
    await asyncio.gather(*[enqueue(queue, max_delay) for _ in range(n)])
    return [await queue.get() for _ in range(n)]


if __name__ == '__main__':
    """ Tests the code in this module """
    print(asyncio.run(task_wait_n(n=5, max_delay=6)))
