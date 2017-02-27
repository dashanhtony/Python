#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import datetime
from jenkinsapi.jenkins import Jenkins
import pytz


def get_server_instance():
    jenkins_url = 'http://116.228.151.160:28082/jenkins/'
    server = Jenkins(jenkins_url, username='shaoyuning', password='syn.0224')
    return server
'''
#将UTC时间转换成本地时间的UTC时间
def utc2local(utc_st):
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st
'''
#将String类型的UTC时间转换成到19700101的秒数
def utc_to_local(utc_time_str, utc_format='%Y-%m-%d %H:%M'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return int(time.mktime(time.strptime(time_str, local_format)))

#将datetime.datetime类型转换成String类型
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d %H:%M")


J = get_server_instance()
jobName = "aaa-jenkinstest"
startTime = J.get_job(jobName).get_last_build().get_timestamp()
#localStartTime = utc2local(startTime)
startSecond = utc_to_local(datetime_toString(startTime))
#minus = localStartTime - startTime
now = datetime.datetime.utcnow()#获得现在时间的UTC时间
print(startTime)
#print(localStartTime)
print(now)
#print(minus)
print(startSecond)
print(time.time())
