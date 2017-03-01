#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#100
i = ['a', 'b']
l = [1, 2]
m = {}
ri = range(len(i))
rl = range(len(l))

for c in ri:
   for d in rl:
       if c==d:
           m[i[c]]=l[d]
print (m)
