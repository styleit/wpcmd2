'''
Created on 2013-3-18

@author: he
'''
import sys
import WordPressAPI
import wpMedia
import Utility
from optparse import OptionParser

def main():
    parser = OptionParser()
    _filter = wpMedia.MediaFilter()
    _util = Utility.Encoding()
    
    parser.add_option('-n','--number',
                      dest='number',
                      type='int',
                      help='How many items you want to list.')

    (options, args) = parser.parse_args()
    if(len(sys.argv)==1):
        _filter = None
    if(options.number):
        _filter.number = options.number
    
    account_info = _util.GetAccountInfo()
    server = WordPressAPI.WordPressClient(account_info['url'],account_info['user_name'],account_info['password'])
    results = server.getMediaLibrary(_filter)
    for item in results:
        print item['attachment_id'] + '\t'+item['link']

if __name__ == '__main__':
    main()