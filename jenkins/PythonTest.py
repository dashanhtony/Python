#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def set_age(self, age):
    self.age = age
    return 25

class Student(object):
    def __init__(self, age):
        self.age = age
from types import MethodType
s = Student(10)
print (s.age)
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(22)# 调用实例方法
print (s.set_age(2))
print (s.age )# 测试结果