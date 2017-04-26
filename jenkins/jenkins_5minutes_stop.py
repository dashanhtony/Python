#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import datetime
from jenkinsapi.jenkins import Jenkins
import pytz
from multiprocessing import Process
import os


def get_server_instance():
    jenkins_url = 'http://116.228.151.160:28082/jenkins/'
    server = Jenkins(jenkins_url, username='shaoyuning', password='syn.0224')
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

def execute_process():
    J = get_server_instance()
    for j in J.get_jobs():
        job_instance = J.get_job(j[0])
        if(job_instance.is_running()):
            start_time =job_instance.get_last_build().get_timestamp()
            startSecond = utc_to_local(datetime_toString(start_time))
            now = datetime.datetime.utcnow()#获得现在时间的UTC时间
            nowSecond = time.time()
            lastTime = nowSecond - startSecond
            if(lastTime > 300):#执行时间超过300秒
                job_instance.get_last_build().stop()
                print(job_instance, start_time, now,startSecond,nowSecond)
if __name__ == '__main__':
    p = Process(target=execute_process)
    p.start()
    p.join()
