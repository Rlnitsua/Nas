#coding=utf-8

import os
import sys
import re

sys.path.append('..')
from utils import Log
from utils import Files

regex = [
        '^\D*(\d+).*\.(.*)$', #0
        '^.*\.E(\d+).*\.(.*)$', #1
        '^\D*(\d+).*视\.(.*)$', #2
        '^.*S\d+E(\d+).*\.(.*)$', #3
        '^.*季(\d+).*\.(.*)$' #4
        ]

tag = 'main'

def processCurrentPath(path, index, handle = False):
    Log.d(tag, 'path : ' + path)
    Log.d(tag, 'regex : ' + regex[int(index)])
    for root, dirs, files in os.walk(path, True):
        for fileName in files:
            matchObj = re.match(regex[int(index)], fileName)
            if (matchObj):
                charpter = matchObj.group(1)
                if (len(charpter) == 1):
                    charpter = '0' + charpter
                extension = matchObj.group(2)
                rootArr = root.split('/')
                fileSuffix = rootArr[len(rootArr) - 1]
                filePath = os.path.join(root, fileName)
                targetPath = os.path.join(root, fileSuffix + '.E' + charpter + '.' + extension)
                Log.d(tag, 'rename ' + filePath + ' -> ' + targetPath)
                if (handle):
                    Files.rename(filePath, targetPath)
                    Log.d(tag, 'rename done')

if __name__ == '__main__':
    if (len(sys.argv) == 3):
        processCurrentPath(sys.argv[1], sys.argv[2])
    elif(len(sys.argv) == 4):
        processCurrentPath(sys.argv[1], sys.argv[2], sys.argv[3])