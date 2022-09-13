#!/usr/bin/env python3

'''
Created by Volodymyr Korobtsov

This script find the roots of quadratic equation
'''

import sys
from math import sqrt

def line() -> None:
    print('\n-------------------------------------------\n')

def ask_value(message: str) -> int:
    print(message)
    while True:
        try:
            a = int(input('a = '))
            if a == 0:
                print("'a' can't be zero, please try again")
            else:
                break
        except ValueError:
            print('Only integer number is allowed, please try again')
    while True:
        try:
            b = int(input('b = '))
            break
        except ValueError:
            print('Only integer number is allowed, please try again')
    while True:
        try:
            c = int(input('c = '))
            break
        except ValueError:
            print('Only integer number is allowed, please try again')
    line()
    print(f'a = {a}, b = {b}, c = {c}')
    return (a,b,c)


def discriminant(a: int, b: int, c: int) -> int:
    d = b**2-4*a*c
    print(f'\nD = {d}\n')
    if d < 0:
        print('This quadratic equation does not have a roots')
        line()
        sys.exit()
    else:
        return d


def roots(d: int, a: int, b: int, c: int) -> None:
    if d > 0:
        x1 = (-b + sqrt(d))/2*a
        x2 = (-b - sqrt(d))/2*a
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
    else:
        x1 = (-b + sqrt(d))/2*a
        print(f'x={x1}')


def solv_square(a: int, b: int, c: int) -> None:
    d = discriminant(a,b,c)
    roots(d,a,b,c)


def main() -> None:
    try:
        (a,b,c) = ask_value(msg)
        solv_square(a,b,c)
        line()
    except KeyboardInterrupt:
        print('\nProgramm was interrupted!')



msg = '''
This is a quadratic equation: ax^2+bx+c=0
To find the roots of quadratic equation please enter a,b,c:
'''

main()
