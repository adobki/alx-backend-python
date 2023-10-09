#!/usr/bin/env python3
""" This module showcases asynchronous coroutines in Python """
import _asyncio
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> _asyncio.Task:
    """ Returns an asyncio.Task object """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    """ Tests the code in this module """
    async def test(max_delay: int):
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
