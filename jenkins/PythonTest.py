#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
print(os.environ)
print("PATH=%s" % os.environ.get('PATH'))
print(os.environ.get('x','dddd'))
print(os.environ.get('x'))
print(os.path.abspath('.'))
print(os.listdir('.'))
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x * x for x in range(1, 11) if x*x < 50])
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
with open('E:\\冒险岛pic\\1.txt','a') as f:
    json.dump(d,f)
print(json.dump.__doc__)