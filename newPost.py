'''
Created on 2013-3-15

@author: he
'''
import _myPost

'''
Descriptin:

post -new
    --type              is post type
-s  --status            is post status
-t  --title             is post title
    --author            is post author
-e  --excerpt           is post excerpt
-c  --content           is post content
    --date              is post date
    --format            is post format
-n  --name              is post name
    --password          is password
    --comment_status    is commment status
    --ping_status       is ping status 
    --sticky            is set post to sticky or not
    --post_thumbnail    is post thumbnail
    --post_parent       is post_parent
-u  --custom_fields     is custom_fields
    --terms             is terms
    --terms_names       is terms_names
    --enclosure         is enclosure
-g  --category          is category
-a  --tag               is tag
'''
from optparse import OptionParser
import WordPressAPI
import Utility
import sys

_utli = Utility.Encoding()
post_tools = _myPost.PostMeta()
parser = OptionParser()
parser.add_option('--type',
                  dest='type',
                  metavar='type',
                  help='The type of the content. \
TYPE should be one of \'post\' | \'page\' | \'link\' | \'nav_menu_item\' | custom post type ')

parser.add_option('-s','--status',
                  dest='post_status',
                  help='The status of the post. \
POST_STATUS should be on of \'draft\' | \'publish\' | \'pending\'| \'future\' | \'private\' | custom registered status')
                  
parser.add_option('-t','--title',
                  dest='title',
                  help='The title of the post. ')

parser.add_option('--author',
                  dest='author_id',
                  type='int',
                  help='The ID of the User')
parser.add_option('-e','--excerpt',
                  dest='excerpt',
                  help='The excerpt of the post')

parser.add_option('-c','--content',
                  dest='content',
                  help='The post content')

parser.add_option('--date',
                  dest='date',
                  help='Post date to publish,current server time by default, further time for scheduler')

parser.add_option('--format',
                  dest='format',
                  help='The format of the post.standard by default.')

parser.add_option('-n','--name',
                  dest='name',
                  help='The sulg(url) of the post.')

parser.add_option('--password',
                  dest='password',
                  help='The password of the post')

parser.add_option('--comment_status',
                  dest='comment_status',
                  help='COMMENT_STATUS should be one of \'closed\' | \'open\'')

parser.add_option('--ping_status',
                  dest='ping_status',
                  help='The ping status of the post')

parser.add_option('--sticky',
                  dest='sticky',
                  metavar='bool',
                  help='Set post to sticky or not,if TRUE the post will sticky on the top')

parser.add_option('--post_thumbnail',
                  dest='post_thumbnail',
                  metavar='MEDIA_ID',
                  type='int',
                  help='The meida id for thumbnail.')

parser.add_option('--post_parent',
                  dest='post_parent',
                  metavar='POST_ID',
                  type='int',
                  help='The parent post_id')

parser.add_option('-u','--custom_fields',
                  dest='custom_fields',
                  help='The custom fields of the post,use \'>>\' to split key and value,\
and \'##\' to split custom fields so the split token(\'>>\' and \'##\') should not in your key or value. \
Example: add two custom fields to the post:\
newPost -u key1>>value1##key2>>value2')

parser.add_option('--terms',
                  dest='terms',
                  help='Set post terms,term name as key, ids as value,for example:\
--terms=category>>2,3##post_tag>>13,12,17 or --terms=post_tag>>13,12,17')

parser.add_option('--terms_names',
                  dest='terms_names',
                  help='Set post terms_names,term name as key, names as value,for example:\
--terms=category>>Category1,Category3##post_tag>>tag1,tag2,tag3 or --terms=post_tag>>tag1,tag2,tag3')

parser.add_option('--enclosure',
                  dest='enclosure',
                  metavar='URL',
                  help='Set an enclosure url to the post')

parser.add_option('-g','--category',
                  dest='category',
                  help='Set category to the post.Same as using --term_names with key "category" mulity category joined by ","')

parser.add_option('-a','--tag',
                  dest='tag',
                  help='Set tag to the post.Same as using --term_names with key "post_tag" mulity tags joined by ","')


(options, args) = parser.parse_args()


if(len(sys.argv)==1):
    parser.error("Please check the usage of newPost: with -h or --help.")
    
account_info=_utli.GetAccountInfo()

blog = WordPressAPI.WordPressClient(account_info['url'],account_info['user_name'],account_info['password'])
Content = post_tools.getContentFromOper(parser, options,blog)
result = blog.newPost(Content)
print result
    
    
    
    