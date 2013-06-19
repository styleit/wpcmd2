'''
Created on 2013-3-13

@author: he
'''
import xmlrpclib

class WordPressClient(object):
    '''
    classdocs
    '''
    def __init__(self,url='',user='',password=''):
        if(url.endswith('/xmlrpc.php')):
            self.url = url
        else:
            if(url[-1]=='/'):
                self.url = url+'xmlrpc.php'
            else:
                self.url = url+'/xmlrpc.php'
        self.user = user
        self.password = password
        self._server = xmlrpclib.ServerProxy(self.url)
        self.blogid=0
 
    def getPost(self,post_id,fields=[]):
        return self._server.wp.getPost(self.blogid,self.user,self.password,post_id,fields)
    
    def getPosts(self,post_filter=None,fields=[]):
        getPostFilter={}
        if(post_filter):
            getPostFilter={
                'post_type'     :post_filter.post_type,
                'post_status'   :post_filter.post_status,
                'number'        :post_filter.number,
                'offset'        :post_filter.offset,
                'orderby'       :post_filter.orderby,
                'order'         :post_filter.order
            }
        
        return self._server.wp.getPosts(self.blogid,self.user,self.password,getPostFilter,fields)
    
    def _postStructMap(self,value):
        post={}
        if(value.post_type != ''):
            post['post_type']=value.post_type
        if(value.post_status!=''):
            post['post_status']=value.post_status
        if(value.post_title!=''):
            post['post_title']=value.post_title
        if(value.post_author!=-1):
            post['post_author']=value.post_author
        if(value.post_excerpt!=''):
            post['post_excerpt']=value.post_excerpt
        if(value.post_content!=''):
            post['post_content']=value.post_content
        if(value.post_date!=None):
            post['post_date']=value.post_date
        if(value.post_format!=''):
            post['post_format']=value.post_format
        if(value.post_name!=''):
            post['post_name']=value.post_name
        if(value.post_password!=''):
            post['post_password']=value.post_password
        if(value.comment_status!=''):
            post['comment_status']=value.comment_status
        if(value.ping_status!=''):
            post['ping_status']=value.ping_status
        if(value.sticky!=None):
            post['sticky']=value.sticky
        if(value.post_thumbnail!=-1):
            post['post_thumbnail']=value.post_thumbnail
        if(value.post_parent!=-1):
            post['post_parent']=value.post_parent
        if(value.custom_fields!=[]):
            post['custom_fields']=value.custom_fields
        if(value.terms!={}):
            post['terms']=value.terms
        if(value.terms_names!={}):
            post['terms_names']=value.terms_names
        if(value.enclosure!=None):
            post['enclosure']=value.enclosure
        return post
            
        
    def newPost(self,value):
        post=self._postStructMap(value)
        return self._server.wp.newPost(self.blogid,self.user,self.password,post) 
    
    def editPost(self,post_id,content):
        post=self._postStructMap(content)
        return self._server.wp.editPost(self.blogid,self.user,self.password,post_id,post)
    
    def deletePost (self,post_id):
        return self._server.wp.deletePost (self.blogid,self.user,self.password,post_id)
    
    def getPostType (self,post_type_name,fields=[]):
        return self._server.wp.getPostType (self.blogid,self.user,self.password,post_type_name,fields)
    
    def getPostTypes(self,post_types_filter={},fields=[]):
        return self._server.wp.getPostType (self.blogid,self.user,self.password,post_types_filter,fields)
    
    def getPostFormats(self,value=None):
        post_formates_filter={}
        if(value is not None):
            post_formates_filter['show-supported']=value.show_supported    
        return self._server.wp.getPostFormats(self.blogid,self.user,self.password,post_formates_filter)
    
    def getPostStatusList(self):
        return  self._server.wp.getPostFormats  (self.blogid,self.user,self.password)
    
    def getMediaItem(self,value):
        return self._server.wp.getMediaItem(self.blogid,self.user,self.password,value) 
        
    def getMediaLibrary (self,value):
        media_filter={}
        if(value != None):
            media_filter = {
                      'number':value.number,
                      'offset':value.offset,
                      'parent_id':value.parent_id,
                      'mime_type':value.mime_type
                      }
        return self._server.wp.getMediaLibrary(self.blogid,self.user,self.password,media_filter) 
        
    def uploadFile(self,value):
        if(value.name == ''):
            value.name = value.getName()
            
        if(value.type == ''):
            value.type = value.getType()
            
        if(value.bits == ''):
            value.bits = value.getBits()
            
        data = {'name':value.name,
                'type':value.type,
                'bits':value.bits,
                'overwrite':value.overwrite
                }
        
        return self._server.wp.uploadFile(self.blogid,self.user,self.password,data)
    
    def getTaxonomy(self,taxonomy_name):
        return self._server.wp.getTaxonomy(self.blogid,self.user,self.password,taxonomy_name)
    
    def getTaxonomies(self):
        return self._server.wp.getTaxonomies(self.blogid,self.user,self.password)
    
    def getTerm(self,taxonomy_name,term_id):
        return self._server.wp.getTerm (self.blogid,self.user,self.password,taxonomy_name,term_id)
    
    def getTerms(self,taxonomy_name,taxonomy_filter=None):
        _filter={}
        if(not taxonomy_filter is None):
            if(taxonomy_filter.number!=-1):
                _filter['number']=taxonomy_filter.number
            if(taxonomy_filter.offset!=-1):
                _filter['offset']=taxonomy_filter.offset
            if(taxonomy_filter.orderby!=''):
                _filter['orderby']=taxonomy_filter.orderby
            if(taxonomy_filter.search!=''):
                _filter['search']=taxonomy_filter.search
            _filter['hide_empty']=taxonomy_filter.hide_empty
        
        return self._server.wp.getTerms(self.blogid,self.user,self.password,taxonomy_name,_filter)
