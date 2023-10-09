#!/usr/bin/env python3
""" This module showcases complex annotations in Python """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Duck typing """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == '__main__':
    print(safe_first_element.__annotations__)
