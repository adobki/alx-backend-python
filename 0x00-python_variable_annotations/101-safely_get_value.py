#!/usr/bin/env python3
""" This module showcases complex annotations in Python """
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


# mypy: no-implicit-optional
def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Duck typing """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == '__main__':
    annotations = safely_get_value.__annotations__

    print('Here\'s what the mappings should look like')
    for k, v in annotations.items():
        print(('{}: {}'.format(k, v)))
