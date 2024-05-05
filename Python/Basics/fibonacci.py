from math import *
from collections import *
from sys import *
from os import *


def Fibonacci(n: int):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(1))
