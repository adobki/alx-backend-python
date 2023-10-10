#!/usr/bin/env python3
""" This module showcases working with asynchronous coroutines in Python """
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """ Gathers results from an async generator """
    return [num async for num in async_generator()]


if __name__ == '__main__':
    """ Tests the code in this module """
    async def main() -> None:
        """ Tests the code in this module """
        print(await async_comprehension())

    asyncio.run(main())
