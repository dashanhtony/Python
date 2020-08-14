#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import datetime
from jenkinsapi.jenkins import Jenkins
import pytz
from multiprocessing import Process
import os
import re


def get_server_instance():
    jenkins_url = 'http://116.228.151.160:28082/jenkins/'
    server = Jenkins(jenkins_url, username='********', password='********')
    return server


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
