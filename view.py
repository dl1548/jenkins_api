#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   run_api.py
@Time    :   2019/02/15 15:57:42
@Author  :   Li Zili 
@Version :   1.0
@Contact :   cn.zili.lee@gmail.com
'''

from jenkins_api import JenkinsExApi,JenkinsApi

def all_jobs():
    jenkins_api = JenkinsApi(
        url='http://192.168.1.111:8080/jenkins',
        username='admin',
        password='123qweASD'
    )
    jenkins_conn= jenkins_api.conn_server()
    
    jks_jobs = jenkins_api.get_jenkins_jobs(jenkins_conn=jenkins_conn)

    if 'error' in jks_jobs:
        return {'status':'failed'}
    else:
        return {'status':'success','result':jks_jobs}

def start_job():
    jenkins_api = JenkinsApi(
        url='http://192.168.1.111:8080/jenkins',
        username='admin',
        password='123qweASD'
    )
    jenkins_conn= jenkins_api.conn_server()
    res = jenkins_api.start_jenkins_job(jenkins_conn=jenkins_conn,jenkins_item='zili-test')

    if 'error' in str(res):
        return {'status':'failed'}
    else:
        return {'status':'success','build_num':str(res)}

def job_log():
    jenkins_api = JenkinsApi(
        url='http://192.168.1.111:8080/jenkins',
        username='admin',
        password='123qweASD'
    )

    jenkins_conn= jenkins_api.conn_server()
    res = jenkins_api.get_job_log(jenkins_conn=jenkins_conn,jenkins_item='zili-test',build_num=4)

    if 'error' in str(res):
        return {'status':'failed'}
    else:
        return {'status':'success','build_num':str(res)}

    return res

def build_info():
    jenkins_api = JenkinsApi(
        url='http://192.168.1.111:8080/jenkins',
        username='admin',
        password='123qweASD'
    )

    jenkins_conn= jenkins_api.conn_server()
    res = jenkins_api.get_build_info(jenkins_conn=jenkins_conn,jenkins_item='zili-test',build_num=6)

    return res


def job_info():
    jenkins_api = JenkinsApi(
        url='http://192.168.1.111:8080/jenkins',
        username='admin',
        password='123qweASD'
    )

    jenkins_conn= jenkins_api.conn_server()
    
    res = jenkins_api.get_job_info(jenkins_conn=jenkins_conn,jenkins_item='zili-test')

    return res
if __name__ == "__main__":
    test = build_info()
    print(test)
    