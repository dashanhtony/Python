#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://116.228.151.160:28082/jenkins/'
    server = Jenkins(jenkins_url, username = 'shaoyuning', password = 'syn.0224')
    return server

"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        print('Job Name:%s' % (job_instance.name))
        print('Job Description:%s' %(job_instance.get_description()))
        print('Is Job running:%s' %(job_instance.is_running()))
        print('Is Job enabled:%s' %(job_instance.is_enabled()))

"""Disable a Jenkins job"""
def disable_job():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    job_name = 'Br-financing-crowdfunding-core'
    if (server.has_job(job_name)):
        job_instance = server.get_job(job_name)
        if(job_instance.is_running()):
            print("yes,it's running")
            #last_build.stop()
        last_build = job_instance.get_last_buildnumber()
        print(last_build)
        print('Name:%s,Is Job Enabled ?:%s' % (job_name, job_instance.is_enabled()))

def get_plugin_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for plugin in server.get_plugins().values():
        print("Short Name:%s" % (plugin.shortName))
        print("Long Name:%s" % (plugin.longName))
        print("Version:%s" % (plugin.version))
        print("URL:%s" % (plugin.url))
        print("Active:%s" % (plugin.active))
        print("Enabled:%s \n" % (plugin.enabled))

def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_last_good_build()
    print(lgb)
    return lgb.get_revision()

if __name__ == '__main__':
    #print(get_server_instance().version)
    #get_job_details()
    #disable_job()
    #get_plugin_details()
    jenkins_url = 'http://116.228.151.160:28082/jenkins/'
    username = 'shaoyuning'
    password = 'syn.0224'
    jobName = "Br-financing-crowdfunding-core"
    print(getSCMInfroFromLatestGoodBuild(jenkins_url, jobName, username, password))
