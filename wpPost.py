'''
Created on 2013-3-14

@author: he
'''
import time
class Post(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.post_type='post'
        self.post_status='publish'
        self.post_title=''
        self.post_author=-1
        self.post_excerpt=''
        self.post_content=''
        self.post_date=None
        self.post_format=''
        self.post_name=''
        self.post_password=''
        self.comment_status='open'
        self.ping_status='open'
        self.sticky=None
        self.post_thumbnail=-1
        self.post_parent=-1
        self.custom_fields=[]
        self.terms={}
        self.terms_names={}
        self.enclosure=None

class PostFilter(object):
    '''
    '''
    def __init__(self):
        self.post_type = ''
        self.post_status = ''
        self.number=-1
        self.offset = -1
        self.orderby = ''
        self.order = ''

    
class CustomField(object):
    '''
    '''
    def __init__(self,key,value):
        self.key=key
        self.value=value

class Enclosure(object):
    '''
    '''
    def __init__(self):
        self.url=''
        self.length=-1
        self.type=''

class PostFormatesFilter(object):
    '''
    '''
    def __init__(self,show_supported=False):
        self.show_supported = show_supported