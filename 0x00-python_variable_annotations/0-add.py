#!/usr/bin/python3
""" This module showcases basic annotations in Python """


def add(a: float, b: float) -> float:
    """ Returns the sum of two float values """
    return float(a + b)


if __name__ == '__main__':
    """ Returns the sum of two float values """
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
