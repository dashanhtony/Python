#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

ticks = time.time()
print("当前时间戳为:", ticks)#当前时间戳为: 1488761925.9934075

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)#本地时间为 : time.struct_time(tm_year=2017, tm_mon=3, tm_mday=6, tm_hour=8, tm_min=58, tm_sec=45, tm_wday=0, tm_yday=65, tm_isdst=0)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)#本地时间为 : Mon Mar  6 08:58:45 2017

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))