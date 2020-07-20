#coding=utf-8

import os
import sys
import re

sys.path.append('..')
from utils import Log
from utils import Files

REGEX = '\D*(\d+).*\.(.*)$'
REGEX_Pro = '.*\.\d*\.S(\d+).*\.(.*)$'

tag = 'main'

def processCurrentPath(path):
    for root, dirs, files in os.walk(path, True):
        for fileName in files:
            matchObj = re.match(REGEX, fileName)
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
                Files.rename(filePath, targetPath)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        processCurrentPath(sys.argv[1])