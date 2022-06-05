#!/usr/bin/python3
def uppercase(str):
    orda = ord('a')
    ordA = ord('A')
    ordz = ord('z')
    last = len(str) - 1
    if last < 0:
        print()
        return
    for i in range(len(str)):
        c = ord(str[i])
        print('{:c}'.format(ordA + c - orda if (c >= orda and c <= ordz)
                            else c), end=('\n' if i == last else ''))
