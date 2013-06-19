'''
Created on 2013-3-15

@author: Administrator
'''
import Utility
import wpPost
import os
import re
import wpMedia


class PostMeta(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        '''
        self.encode_utli = Utility.Encoding()
        
    def getContentFromOper(self,parser,options,server):
        investegateEncoding=''
        if(not options.title is None):
            investegateEncoding+=options.title
        if(not options.excerpt is None):
            investegateEncoding+=options.excerpt
        if(not options.category is None):
            investegateEncoding+=options.category
        if(not options.tag is None):
            investegateEncoding+=options.tag
        if(not options.content is None):
            if(not options.content.endswith('.txt')):
                investegateEncoding += options.content
        encoding=self.encode_utli.GetEncoding(investegateEncoding)
        Content = wpPost.Post()
        if(options.type):
            Content.post_type = self.encode_utli.ToUTF8(options.type)
        if(options.post_status):
            Content.post_status=self.encode_utli.ToUTF8(options.post_status)
        if(options.title):
            Content.post_title = self.encode_utli.ToUTF8(options.title,encoding)
        if(options.author_id):
            Content.post_author=self.encode_utli.ToUTF8(options.author_id)
        if(options.content):
            if(options.content.endswith('.txt') or options.content.endswith('.html') or options.content.endswith('.htm')):
                Content.post_content=self.readContentFor(options.content, server)
            else:
                Content.post_content=self.encode_utli.ToUTF8(options.content,encoding)
        if(options.excerpt):
            Content.post_excerpt=self.encode_utli.ToUTF8(options.excerpt,encoding)
        else:
            tmp_post_excerpt=self.encode_utli.GetExcerpt(Content.post_content)
            if tmp_post_excerpt.find('exc:') == 0:
                Content.post_content = Content.post_content.replace('<exc>','').replace('</exc>', '')
                tmp_post_excerpt = tmp_post_excerpt.replace('exc:', '')
            Content.post_excerpt = tmp_post_excerpt
        if(options.date):
            Content.post_date=self.encode_utli.ToUTF8(options.date)
        if(options.format):
            Content.post_format = self.encode_utli.ToUTF8(options.format)
        if(options.name):
            Content.post_name=self.encode_utli.ToUTF8(options.name,encoding)
        else:
            Content.post_name=self.encode_utli.Translation(Content.post_title)
        if(options.password):
            Content.post_password=self.encode_utli.ToUTF8(options.password)
        if(options.comment_status):
            Content.comment_status=self.encode_utli.ToUTF8(options.comment_status)
        if(options.ping_status):
            Content.ping_status=self.encode_utli.ToUTF8(options.ping_status)
        if(options.sticky):
            Content.sticky=self.encode_utli.ToUTF8(options.sticky)
        if(options.post_thumbnail):
            Content.post_thumbnail=self.encode_utli.ToUTF8(options.post_thumbnail)
        if(options.post_parent):
            Content.post_parent=self.encode_utli.ToUTF8(options.post_parent)
        if(options.custom_fields):
            cf=[]
            kvs=options.custom_fields.split('##')
            if(kvs.count==0):
                parser.error("Custom Fields Failed!")
            for item in kvs:
                if(not '>>' in item):
                    parser.error("Custom Fields key value pair Failed!")
                _key=self.encode_utli.ToUTF8(item.split('>>')[0],encoding)
                _value=self.encode_utli.ToUTF8(item.split('>>')[1],encoding)
                pattern = re.compile(r'\[(.*?)\]')
                base_path=''
                if(len(re.findall(pattern,_value))>0):
                    if(options.content.endswith('.txt') or options.content.endswith('.html') or options.content.endswith('.htm')):
                        base_path = os.path.dirname(options.content)
                        if(base_path is ''):
                            parser.error('The content file should be a full file name with absolue path.')
                    else:
                        if(os.path.dirname(_value) is ''):
                            parser.error('Using direct content should give absolue path of the media '+ _value)    
                    match_dir=self.upLoadMeddiaByReg(server, _value, pattern, base_path)
                    for (key,value) in match_dir.items():
                        _value = _value.replace('['+key+']',value)      
                    '''match_dir=self.upLoadMeddiaByReg(server, _value, pattern, base_path, expect_media_info)'''
                cf.append(wpPost.CustomField(_key,_value))
            Content.custom_fields=cf   
        if(options.terms):
            terms={}
            kvs=options.terms.split('##')
            if(kvs.count==0):
                parser.error("Terms Failed!")
            for item in kvs:
                if(not '>>' in item):
                    parser.error("Terms key value pair Failed!")
                key=self.encode_utli.ToUTF8(item.split('>>')[0])
                value=item.split('>>')[1].split(',')
                for i in range(len(value)):
                    value[i]=self.encode_utli.ToUTF8(value[i],encoding)
                terms[key]=value
            Content.terms=terms
        if(options.terms_names):
            terms_names={}
            kvs=options.terms_names.split('##')
            if(kvs.count==0):
                parser.error("Terms Name Failed!")
            for item in kvs:
                if(not '>>' in item):
                    parser.error("Terms Name key value pair Failed!")
                key=self.encode_utli.ToUTF8(item.split('>>')[0])
                value=item.split('>>')[1].split(',')
                for i in range(len(value)):
                    value[i]=self.encode_utli.ToUTF8(value[i],encoding)
                terms_names[key]=value
            Content.terms_names=terms_names
        if(options.enclosure):
            enc = wpPost.Enclosure()
            enc.url = options.enclosure
            enc.type=options.enclosure.split('.')[-1]
            Content.enclosure=enc      
        if(options.category):
            catlist=options.category.split(',')
            if(catlist.count!=0):
                for i in range(len(catlist)):
                    catlist[i]=self.encode_utli.ToUTF8(catlist[i],encoding)
            Content.terms_names['category']=catlist
        
        if(options.tag):
            taglist=options.tag.split(',')
            if(taglist.count!=0):
                for i in range(len(taglist)):
                    taglist[i]=self.encode_utli.ToUTF8(taglist[i],encoding)
            Content.terms_names['post_tag']=taglist
        return Content

    def readContentFor(self,filename,server):
        fh=open(filename)
        tmp_buffer = fh.read()
        fh.close()
        result = self.encode_utli.ToUTF8(tmp_buffer)
        
        baseDir=os.path.dirname(filename)
        pattern = re.compile(r'<img.*?src="\[(.*?)\].*?"')

        match_dir = self.upLoadMeddiaByReg(server, result, pattern, baseDir)

        for (key,value) in match_dir.items():
            result = result.replace('src="['+key+']','src="'+value)    
            
        return result
    
    def upLoadMeddiaByReg(self,server,content,reg,base_path='',expect_media_info='url'):
        match_all = re.findall(reg, content)
        match_dir={}
        for item in match_all:
            if (base_path is ''):
                match_dir[item]=item
            else:
                match_dir[item]=os.path.join(base_path,item)
        for (key,value) in match_dir.items():
            if(os.path.exists('upyun.txt')):
                upYun = Utility.UpYunClient()
                remote_file=upYun.UpLoad(value)
                match_dir[key]=remote_file
            else:
                media_file = wpMedia.MediaForUpload(value)
                remote_file = server.uploadFile(media_file)
                match_dir[key]=remote_file[expect_media_info]
        return match_dir
