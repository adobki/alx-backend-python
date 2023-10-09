#!/usr/bin/env python3
""" This module showcases complex annotations in Python """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Creates a tuple from a string and a number """
    return str(k), v * v


if __name__ == '__main__':
    print(to_kv.__annotations__)
    print(to_kv('eggs', 3))
    print(to_kv('school', 0.02))
