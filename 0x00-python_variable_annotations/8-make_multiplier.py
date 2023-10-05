#!/usr/bin/python3
""" This module showcases complex annotations in Python """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a multiplier function that creates multiples of multiplier """
    return lambda x: float(x * multiplier)


if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print('{}'.format(fun(2.22)))
    print('{}'.format(fun(1)))
    print('{}'.format(fun(5)))
