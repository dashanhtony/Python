#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, sys
path = "D:\git项目\Python\jenkins"
dirs = os.listdir(path)
print(dirs)
for file in dirs:
    print(file)
print([file for file in dirs if os.path.isfile(file)])

