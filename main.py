'''
Created on 2013-3-14

@author: he
'''
import WordPressAPI
import wpMedia,wpPost
from wpMedia import MediaFilter
from xmlrpclib import datetime
import _myPost
import wpTaxonomies
import Utility

cdn = Utility.UpYunClient()

result = cdn.UpLoad(r'E:\Pictures\performace.png')
print result

'''
tools =_myPost.PostMeta()

term_filter = wpTaxonomies.TermsFilter()

myBlog = WordPressAPI.WordPressClient('http://www.styleit.me','admin','Ehong@807095550')

result = myBlog.getTerms('category')

for item in result:
    print item['name']
'''

''' publish new post demo
artical = wpPost.Post()
artical.post_title='Test'
artical.post_content='Test Content'
artical.post_excerpt='Test Excerpt'
artical.post_name='test link'
artical.post_status='draft'
artical.post_type='post'
artical.post_date=datetime.datetime.now()
artical.custom_fields.append(wpPost.CustomField('key','value'))
artical.terms_names['category']=['Test Category']
artical.terms_names['post_tag']=['post','tag']

result = myBlog.newPost(artical)
print result
'''
'''getMediaLibrary Demo
result = myBlog.getMediaLibrary(MediaFilter())

for item in result:
    print item['attachment_id']
    print item['link']
'''
''' Up load Meida Demo
TouploadFile = wpMedia.MediaForUpload(r'C:\Documents and Settings\he\Desktop\t.jpg',False)
result = myBlog.uploadFile(TouploadFile)

print result['id']
print result['url']
'''

