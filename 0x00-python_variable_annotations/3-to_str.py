#!/usr/bin/python3
""" This module showcases basic annotations in Python """


def to_str(n: float) -> str:
    """ Converts a float to a string """
    return str(n)


if __name__ == '__main__':
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print('to_str(3.14) returns {} which is a {}'.format(pi_str, type(pi_str)))
