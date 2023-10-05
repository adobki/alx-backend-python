#!/usr/bin/python3
""" This module showcases basic annotations in Python """
import math


def floor(n: float) -> int:
    """ Returns the floor (integer value) of a float """
    return math.floor(n)


if __name__ == '__main__':
    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print('floor(3.14) returns {}, which is a {}'.format(ans, type(ans)))
