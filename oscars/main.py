#coding=utf-8

import os
import sys
import re

sys.path.append('..')
from utils import Log
from utils import Files

OSCARS_PATH = '/var/services/video/Oscars'
REGEX = '^(.*)-(.*)$'
TEST_PATH = os.getcwd()

tag = 'main'

def processCurrentFolder(path):
    for root, dirs, files in os.walk(path, True):
        for fileName in files:
            matchObj = re.match(REGEX, fileName)
            if (matchObj):
                targetFileName = matchObj.group(2)
                filePath = os.path.join(root, fileName)
                targetPath = os.path.join(root, targetFileName)
                Log.d(tag, 'rename ' + filePath + " to " + targetPath)
                Files.rename(filePath, targetPath)
        for dirItem in dirs:
            processCurrentFolder(dirItem)

def moveToTargetFolder(path):
    for root, dirs, files in os.walk(path, True):
        for fileName in files:
            if (root != path):
                filePath = os.path.join(root, fileName)
                targetPath = os.path.join(path, fileName)
                Log.d(tag, 'move file from ' + filePath + ' to ' + targetPath)
                Files.move(filePath, targetPath)
        for dirItem in dirs:
            moveToTargetFolder(dirItem)

if __name__ == '__main__':
    processCurrentFolder(OSCARS_PATH)
    moveToTargetFolder(OSCARS_PATH)