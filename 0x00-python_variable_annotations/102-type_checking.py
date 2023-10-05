#!/usr/bin/python3
""" This module showcases complex annotations in Python """
from typing import Mapping, Any, Union, TypeVar, TypeAlias

Tuple: TypeAlias = tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """ Duck typing for complex annotations in Python"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)


if __name__ == '__main__':
    print(zoom_array.__annotations__)
