#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   jenkins_api.py
@Time    :   2019/02/14 17:23:52
@Author  :   Li Zili 
@Version :   1.0
@Contact :   cn.zili.lee@gmail.com
'''

from jenkins import JenkinsException,NotFoundException
import jenkins
import json
import six
from six.moves.http_client import BadStatusLine
from six.moves.urllib.error import HTTPError
from six.moves.urllib.error import URLError
from six.moves.urllib.parse import quote, urlencode, urljoin, urlparse
from six.moves.urllib.request import Request, install_opener, build_opener, urlopen
import requests
# disbled warning
requests.packages.urllib3.disable_warnings()

class ServerError(Exception):
    pass

class JenkinsExApi(jenkins.Jenkins):
    """
    Jenkins Extension functions

    """

    def zili(self,**kwargs):
        return '自定义方法预留'


class JenkinsApi(object):
    """
    Jenkins api

    : param url
    : param username
    : param password

    """
    def __init__(self,**kwargs):
        self.url=kwargs.get('url')
        self.username=kwargs.get('username')
        self.password=kwargs.get('password')

    def conn_server(self):
        try:
            jenkins_conn = JenkinsExApi(self.url, username=self.username, password=self.password)
            return jenkins_conn
        except Exception as e:
            raise ServerError(e)
        
    def get_jenkins_jobs(self,jenkins_conn):
        """
        Get Jenkins jobs
        
        : param jenkins_conn
        """
        try:
            jobs= jenkins_conn.get_jobs()
            return jobs
        except Exception as e:
            return {'error':'get_jenkins_jobs','result':e}
    
    def start_jenkins_job(self,jenkins_conn,jenkins_item):
        """
        Start Jenkins job
        
        : param jenkins_conn
        : param jenkins_item
        """
        try:
            next_nu = jenkins_conn.get_job_info(jenkins_item)['nextBuildNumber']
            jenkins_conn.build_job(jenkins_item)
            # last_nu = jenkins_conn.get_job_info(jenkins_item)['lastBuild']['number']
            return next_nu

        except Exception as e:
            return {'error':'start_jenkins_job','result':e}


    def get_job_log(self,jenkins_conn,jenkins_item,build_num):
        try:
            job_log=jenkins_conn.get_build_console_output(jenkins_item, build_num)
            return job_log
        except Exception as e:
            return {'error':'get_job_log','result':e}
    
    def get_build_info(self,jenkins_conn,jenkins_item,build_num):
        try:
            build_info=jenkins_conn.get_build_info(jenkins_item, build_num)
            return build_info
        except Exception as e:
            return {'error':'get_build_info','result':e}
        
    def get_job_info(self,jenkins_conn,jenkins_item):
        try:
            build_info=jenkins_conn.get_job_info(jenkins_item)
            return build_info
        except Exception as e:
            return {'error':'get_info','result':e}