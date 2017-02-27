#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
tr = True
print(isinstance(tr, bool))

L = ['Hello', 'World', 'IBM', 'Apple']
print([s[0] for s in L])
print([str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]])

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None,  'C', '  '])))
'''
def is_palindrome(n):
    nlist = str(int(n))
    print(nlist)
    print(len(nlist))
    print(int(len(nlist)/2))
    for x in range(int(len(nlist)/2)):
        if nlist[x] != nlist[len(nlist)-x-1]:
            return False
        else:
            continue
    return True
print(is_palindrome(98989898989))
print(is_palindrome(98))


