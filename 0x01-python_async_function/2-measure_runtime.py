#!/usr/bin/env python3
""" This module showcases asynchronous coroutines in Python """
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Returns the runtime of wait_n function """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - start_time) / n


if __name__ == '__main__':
    """ Tests the code in this module """
    print(measure_time(n=5, max_delay=9))
