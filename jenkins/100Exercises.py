#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#1
list1=[1,2,3,4]
for i in list1:
    for j in list1:
        for k  in list1:
            if i!=j and i!=k and j!=k:
                num = 100*i+10*j+k
                print ('number is:%d' % num)


#2
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print ('总奖金：',r)



#3
import math
for y in range(10000):
    a = int(math.sqrt(y+100))
    b = int(math.sqrt(y+268))
    if a*a == y+100 and b*b == y+268:
        print('the number is :%d ' % y)

#4
year=int(input("input year:\n"))
month=int(input("input month:\n"))
day=int(input("input day:\n"))

day_month=(0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<13 :
    day_sum=day_month[month-1]
    day_sum+=day

leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    day_sum += 1
print(day_sum)


#5
l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l


#6
L=[]
def fib(maxnum):
    n,a,b=0,0,1
    while n < maxnum:
        L.append(b)
        a,b = b, a+b
        n=n+1
maxnum=int(input("input maxnum:"))
fib(maxnum)
print(L)

#7
a = [1, 2, 3]
b = a[:]
print b

#8
i,j = 1,1
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            num=i*j
            print("%d * %d = %2d   " % (i,j,num),end='')
    print("")

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
'''



