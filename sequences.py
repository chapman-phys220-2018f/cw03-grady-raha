#!/usr/bin/env python3

def fibonacci(n):
# finds and prints a list of fibonacci numbers up to the nth fibonacci number.

    if (n < 1):
        print("Please enter a positive integer.")
    else:
        a = [1]
        x = 1
        y = 0
        f = 0
        n = n-1
        for i in range(n):
            f = x + y
            y = x
            x = f
            a.append(f)
    return a

