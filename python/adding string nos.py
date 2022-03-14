# The included code stub will read an integer,n , from STDIN.
# Without using any string methods, try to print the following:
# 1234...n
# Note that ... represents the consecutive values in between.

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i+1,end="")