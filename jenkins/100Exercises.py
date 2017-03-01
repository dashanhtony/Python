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
'''

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



'''
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