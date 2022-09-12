#!/usr/bin/env python3

'''
Created by Volodymyr Korobtsov

This script find the roots of quadratic equation
'''

import sys
from math import sqrt


def ask_value(message):
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
            if b == 0:
                print("'b' can't be zero, please try again")
            else:
                break
        except ValueError:
            print('Only integer number is allowed, please try again')
    while True:
        try:
            c = int(input('c = '))
            if c == 0:
                print("'c' can't be zero, please try again")
            else:
                break
        except ValueError:
            print('Only integer number is allowed, please try again')
    print(f'\na={a}, b={b}, c={c}')
    return (a,b,c)


def discriminant(a,b,c):
    d = b**2-4*a*c
    print(f'd={d}')
    if d < 0:
        print('This quadratic equation does not have a roots')
        sys.exit()
    else:
        return d


def roots(d,a,b,c):
    if d > 0:
        x1 = (-b + sqrt(d))/2*a
        x2 = (-b - sqrt(d))/2*a
        print(f'x1={x1}')
        print(f'x2={x2}')
    else:
        x1 = (-b + sqrt(d))/2*a
        print(f'x={x1}')


def solv_square(a,b,c):
    d = discriminant(a,b,c)
    roots(d,a,b,c)


def main():
    try:
        (a,b,c) = ask_value(msg)
        solv_square(a,b,c)
    except KeyboardInterrupt:
        print('\nProgramm was interrupted!')



msg = '''
This is a quadratic equation: ax^2+bx+c=0
To find the roots of quadratic equation please enter a,b,c:
'''

main()
