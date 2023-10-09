#!/usr/bin/env python3
""" This module showcases annotations for variables in Python """

a: int = 1
pi: float = 3.14
school: str = 'Holberton'
i_understand_annotations: bool = True

if __name__ == '__main__':
    a = __import__('4-define_variables').a
    pi = __import__('4-define_variables').pi
    iua = __import__('4-define_variables').i_understand_annotations
    school = __import__('4-define_variables').school

    print('a is a {} with a value of {}'.format(type(a), a))
    print('pi is a {} with a value of {}'.format(type(pi), pi))
    print('i_understand_annotations is a {} with a value of {}'
          .format(type(iua), iua))
    print('school is a {} with a value of {}'.format(type(school), school))
