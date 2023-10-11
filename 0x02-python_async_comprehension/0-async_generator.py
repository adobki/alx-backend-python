#!/usr/bin/env python3
""" This module showcases working with asynchronous coroutines in Python """
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ A basic async generator that completes execution in ten seconds """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


if __name__ == '__main__':
    """ Tests the code in this module """
    async def print_yielded_values() -> None:
        """ Tests the code in this module """
        result = []
        async for i in async_generator():
            result.append(i)
            print(i)
        print(result)

    asyncio.run(print_yielded_values())
