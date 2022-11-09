from decimal import *
import math
from unicodedata import decimal

def soma(i, j, q):
    print()
    print('{} + {} = {} '.format(i, j, q))
    print()

def subt(i, j, q):
    print()
    print('{} - {} = {} '.format(i, j, q))
    print()

def multi(i, j, q):
    print()
    print('{} * {} = {} '.format(i, j, q))
    print()

def divi(i, j, q):
    print()
    print('{} / {} = {} '.format(i, j, q))
    print()

def poten(i, j, q):
    print()
    print('{} ^ {} = {} '.format(i, j, q))
    print()

def rq(i, j):
    print()
    a = Decimal(i)
    b = Decimal(j)

    print('√{} = {}'.format(i, a.sqrt()))

    print('√{} = {}'.format(j, b.sqrt()))
    print()

def fato(i, j):
    print()
    print('!{} = {}'.format(i, math.factorial(i)))

    print('!{} = {}'.format(j, math.factorial(j)))
    print()
