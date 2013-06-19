'''
Created on 2013-3-13

@author: he
'''
import datetime
import mimetypes
import xmlrpclib

class MediaItemSize(object):
    '''
    '''
    def __init__(self):
        self.file=''
        self.width=''
        self.height=''
        self.mime_type=''
    
class MediaItemMetadata(object):
    '''
    '''
    def __init__(self):
        self.width = 0
        self.height = 0
        self.file=''
        self.sizes = MediaItemSizes()

class MediaItemSizes(object):
    '''
    '''
    def __init__(self):
        self.thumbnail = MediaItemSize()
        self.medium = MediaItemSize()
        self.large = MediaItemSize()
        
class MediaItem(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.attachment_id = ''
        self.datetime = datetime.datetime()
        self.parent = 0
        self.link = ''
        self.title = ''
        self.caption=''
        self.description = ''
        self.metadata=MediaItemMetadata()
        self.image_meta = PostThumbnailImageMeta()
        self.thumbnail = ''
        
class PostThumbnailImageMeta(object):
    '''
    '''
    def __init__(self):
        self.aperture = 0
        self.credit = ''
        self.camera=''
        self.caption=''
        self.created_timespamp=0
        self.copyright=''
        self.focal_length=0
        self.iso=0
        self.shutter_speed=0
        self.title=''
    
class MediaForUpload(object):
    '''
    Media file to upload
    '''
    def __init__(self,fileName,overWrite=False):
        self.filename = fileName
        self.name = ''
        self.type = ''
        self.bits=''
        self.overwrite=overWrite
        
    def getName(self):
        return self.filename.split('\\')[-1]
    def getType(self):
        return mimetypes.guess_type(self.filename)[0]
    def getBits(self):
        mediafh = open(self.filename,'rb')
        mediabits = mediafh.read()
        mediafh.close()
        return xmlrpclib.Binary(mediabits)
    
class MediaUploadResult(object):
    '''
    Media file upload result
    '''
    def __init__(self):
        self.id=''
        self.file=''
        self.url=''
        self.type=''

class MediaFilter(object):
    '''
    '''
    def __init__(self):
        self.number=0
        self.offset=0
        self.parent_id=0
        self.mime_type=''