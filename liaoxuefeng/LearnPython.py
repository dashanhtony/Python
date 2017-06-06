#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#数据类型和变量
print("n = 123")
print('s1 = \'Hello, world\'')
print(r"s2 = 'Hello, \'Adam\'\"'")
print(r"s3 = r'Hello, "+r'"Bart"'+r"'")
print("s3 = r\'Hello, \"Bart\"\'中文")

#字符串和编码
s1 = 72
s2 = 85
r=(s2-s1)/s2*100
print("%003d %03.1f%%" % (s1,r))

#使用list和tuple
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print(len(L))
print(L[2])

#条件判断
age = 20
if age >= 6 and age < 18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
height = 1.75
weight = 80.5
bmi = weight /(height**2)
if bmi < 18.5:
    print('过轻')
elif bmi <25:
    print('正常')
elif bmi <28:
    print('过重')
elif bmi <32:
    print('肥胖')
else:
    print('严重肥胖')

#循环
print(range(5))
print(list(range(5)))
if 2 in range(5):
    print("true")
else:
    print("false")
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello "+name)

#使用dict和set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('Thomas' in d)
print(d.get('Thomas',-1))
s1 = set([1, 2, 3])
print(s1)
s2 = set([4, 2, 3])
print(s2)
L=[5,6,7]
print(L)
#s1.add(L)
print(d.keys())
print(d.items())
print(d)
print(d.get('Bob', 99))

#调用函数
n1 = 255
n2 = 1000
print(hex(n1),hex(n2))

#定义函数
import math
def quadratic(a, b, c):
    if a!=0:
        delta = b**2-4*a*c
    if delta >=0:
        x1 = (-b+math.sqrt(delta))/2/a
        x2 = (-b-math.sqrt(delta))/2/a
    return x1,x2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))

#递归函数
#这里注意，调用递归函数的时候把剩余n-1个当成一个整体，所以逻辑是a移n-1个到b，移1个到c，然后把n-1个从b移到c，一层就完成了
def move(n, a, b, c):
    if n==1:
        print(a, " --> ", c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3, 'A', 'B', 'C')

#列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])

#生成器
g = (x * x for x in range(10))
for n in g:
    print(n)

def triangles():
    list1 = [1]
    while True:
        yield list1
        list1.append(0)#list1 = [1,0]
        list1 = [list1[i - 1] + list1[i] for i in range(len(list1))]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

#map/reduce
def normalize(name):
    return name[:1].upper()+name[1:len(name)].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce


def prod(L):
    def prod2(a, b):
        return a*b
    return reduce(prod2,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    return float(s)
print('str2float(\'123.456\') =', str2float('123.456'))


#filter
def is_palindrome(n):
    nlist = str(int(n))
    for x in range(int(len(nlist)/2)):
        if nlist[x] != nlist[len(nlist)-x-1]:
            return False
        else:
            continue
    return True
output = filter(is_palindrome, range(1, 1000))
print(list(output))


#sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]
L3 = sorted(L, key=by_score, reverse=True)
print(L3)


def build(x, y):
    return lambda: x * x + y * y
f1=build(3,4)
print(f1())
print(build)
print(build(3, 4)())

#1
def func_lambda1(x):
    return lambda: x ** 2
f1=func_lambda1(2)
print(f1())
#2
def func_lambda2():
    return lambda x: x ** 2
f2 = func_lambda2()
print(f2(2))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log #等同于now = log(now)
def now():
    print('2015-3-25')

now()

def log(func):
    def wrapper(*args, **kw):
        print('begin call ')
        return func(*args, **kw)

    return wrapper

@log
def f():
    print("starting the function")

#类和实例
class Student(object):
    def __init__(self, name, score, **kw):
        self.name = name
        self.score = score
        self.age = kw['age']
        self.sex = kw['sex']

bart = Student('Bart Simpson', 59,age=18,sex='male')

print(bart.age,"   ",bart.sex)

#使用@property


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        self._resolution = self._width * self._height
        return self._resolution
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
#assert (s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution)

f1 = open('E:\\冒险岛pic\\86767.jpg', 'rb')
#f2 = open('E:\\冒险岛pic\\1.txt', 'r')
#print(f1.read())
f1.close()
#print(f2.read())
#f2.close()
with open('E:\\冒险岛pic\\1.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

from io import StringIO
f = StringIO()
f.write("Hello")
f.write(" ")
f.write("World!")
print(f.getvalue())
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

import os
print(os.name)
#print(os.environ)
print(os.path.abspath('.'))
#os.mkdir('D:\git项目\Python\jenkins/testdir')
#os.rmdir('D:\git项目\Python\jenkins/testdir')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
f = open('jsonfile.txt','w')
json.dump(d,f)
f.close()
f1 = open('jsonfile.txt','r')
d = json.load(f1)
f1.close()
print(d)

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

import re
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$', t)
print(m)
print(m.groups())
print(re.match(r'^(\d+)?(0*)$', '1020300').groups())

import struct
print(struct.pack('>I', 10240099))#b'\x00\x9c@c'
print(struct.pack('>I', 10240100))#b'\x00\x9c@d'

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

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
with open('E:\\冒险岛pic\\1.txt','w+') as f:
    json.dump(d,f)
'''