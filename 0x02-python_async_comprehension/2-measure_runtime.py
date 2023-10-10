#!/usr/bin/env python3
""" This module showcases working with asynchronous coroutines in Python """
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures runtime of running an async generator concurrently """
    start_time = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time() - start_time


if __name__ == '__main__':
    """ Tests the code in this module """
    async def main() -> None:
        """ Tests the code in this module """
        print(await measure_runtime())

    asyncio.run(main())
