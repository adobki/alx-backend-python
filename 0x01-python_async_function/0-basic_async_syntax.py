#!/usr/bin/env python3
""" This module showcases asynchronous coroutines in Python """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Returns the randomly generated wait time """
    wait = uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait


if __name__ == '__main__':
    """ Tests the code in this module """
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
