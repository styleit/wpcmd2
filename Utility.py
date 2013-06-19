'''
Created on 2013-3-15

@author: Administrator
'''

import chardet
import json
import urllib
import re
import ftplib
from upyun import UpYun,md5,md5file
import sys
import datetime
from pywin.framework.mdi_pychecker import TheDialog


class Encoding(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def ToUTF8(self,value,encoding=''):
        if(encoding==''):
            encoding=chardet.detect(value)['encoding']
        return unicode(value,encoding).encode("UTF-8")
    
    def GetEncoding(self,value):
        return chardet.detect(value)['encoding']
    
    def GetExcerpt(self,value):
        if value is None:
            return None
        pattern = re.compile(r'<exc>([\d\D]*?)</exc>')
        the_excerpt=''
        first_par=value.find('\n')
        exc_list = pattern.findall(value)
        if(len(exc_list)>0):
            the_excerpt = 'exc:'
            for item in exc_list:
                the_excerpt += item
        else: 
            the_excerpt = value[0:first_par]
            
        return the_excerpt
    
    def GetAccountInfo(self):
        url=''
        user_name=''
        password=''
        try:    
            account_info = open("account.txt").read()
            url=self.ToUTF8(account_info.split(';')[0])
            user_name = self.ToUTF8(account_info.split(';')[1])
            password=self.ToUTF8(account_info.split(';')[2])
        except:
            ''
        while (url=='' or user_name=='' or password==''):
            url = raw_input('Your Site Addr:')
            user_name = self.ToUTF8(raw_input('Your user name:'))
            password = self.ToUTF8(raw_input('Password:'))
        
        account_info={
                     'url':url,
                     'user_name':user_name,
                     'password':password
                     }
        return account_info
    def Translation(self,value):
        query_data='http://fanyi.youdao.com/openapi.do?keyfrom=styleit&key=1875213668&type=data&doctype=json&version=1.1&q='+value
        page=urllib.urlopen(query_data).read()
        trans_result = json.loads(page)
        return trans_result['translation'][0]


class UpYunClient(object):
    '''
    '''
    def __init__(self):
        self.ftp_raw_info=open("upyun.txt").read().split(';')
        self.bucket_name=self.ftp_raw_info[0]
        self.server_user=self.ftp_raw_info[1]
        self.server_user_pwd = self.ftp_raw_info[2]
        self.base_access_url = self.ftp_raw_info[3]
        self.server = UpYun(self.bucket_name,self.server_user,self.server_user_pwd)
        self.server.setApiDomain('v0.api.upyun.com')
        
    def UpLoad(self,fileName):
        data = open(fileName,'rb')
        self.server.setContentMD5(md5file(data))
        date_info=datetime.datetime.today()
        remote_path=str(date_info.year)+'/'+str(date_info.month)
        remote_file_name = '/'+str(date_info.microsecond)+fileName.split('\\')[-1]
        
        to_write= remote_path+remote_file_name
        a = self.server.writeFile(to_write,data)
        
        if(a):
            return self.base_access_url+'/'+remote_path+remote_file_name
        else:
            return None
        
            