#!/usr/bin/env python3

from sequences import fibonacci

#n = ("what fibonacci number would you like to find: ")
#n = int(n)

#a = fibonacci(n)

#x = a.pop(-1)

#print(x)

def main(argv):
    a = fibonacci(int(argv[1]))
    print(a[-1])

if __name__ == "__main__":
    import sys
    main(sys.argv)
