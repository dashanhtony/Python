#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shell(arr):
    l=len(arr)
    h=1
    while h<l//3:
        h=3*h+1
    while h>=1:
        for i in range(h,l):
    j=i
    while j>= h and arr[j]<arr[j-h]:
        arr[j],arr[j-h]=arr[j-h],arr[j]
    j-=h
    h=h//3
    return arr