#coding=utf-8

import os
import sys
import re

sys.path.append('..')
from utils import Log

DOUBAN_PATH = '/var/services/video/douban'

tag = 'main'

def processDoubanFolder(doubanPath):
    Log.d(tag, 'processDoubanFolder')
    for root, dirs, files in os.walk(doubanPath, True):
        Log.d(tag, 'handle : ' + root)
        for dirItem in dirs:
            if (isDoubanParentFolder(dirItem)):
                processDoubanParentFolder(dirItem)

def isDoubanParentFolder(dirItem):
    # Log.d(tag, 'isDoubanParentFolder : ' + dirItem)
    regex = '^\d\d\d-\d\d\d$'
    return re.match(regex, dirItem)

def processDoubanParentFolder(dirItem):
    # Log.d(tag, 'processDoubanParentFolder' + dirItem)
    regex = '^(.*)\s(.*)$'
    matchObj = re.match(regex, dirItem)
    if (matchObj):
        filmName = matchObj.group(2)
    for root, dirs, files in os.walk(dirItem, True):
        if (len(files) == 1):
            Log.d(tag, files[0])

if __name__ == '__main__':
    processDoubanFolder(DOUBAN_PATH)