'''
Created on 2013-3-18

@author: he
'''
import sys
import WordPressAPI
import wpMedia
import Utility
from optparse import OptionParser

def _upload(fileName,over_write=False):
    mfile = wpMedia.MediaForUpload(fileName,over_write)
    _util = Utility.Encoding()
    account_info = _util.GetAccountInfo()
    server = WordPressAPI.WordPressClient(account_info['url'],account_info['user_name'],account_info['password'])
    result = server.uploadFile(mfile)
    print result['id'] +'\t' + result['url']
    
def main():
    parser = OptionParser()
    over_write = False
    parser.add_option('-a','--add',
                      dest='add_media',
                      metavar='MediaPath',
                      help='Add a media file to remote.')
    
    parser.add_option('-o','--over_write',
                      dest='over_write',
                      help='Overwrite exist file.')
    
    (options, args) = parser.parse_args()
    
    if(len(sys.argv)==1):
        parser.error("Please check the usage of newPost: with -h or --help.")
    
    if (options.over_write):
        if(options.over_write == 'True'):
            over_write = True
    
    if(options.add_media):
        _upload(options.add_media,over_write)
    

if __name__ == '__main__':
    main()