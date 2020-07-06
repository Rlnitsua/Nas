#coding=utf-8

import os
import sys
import re

from shutil import move

sys.path.append('..')
from utils import Log
from utils import Utils
from utils import Files

DOUBAN_PATH = '/var/services/video/douban/'
REGEX = '^(\d{2,3})\s(.*)$'

tag = 'main'

def processDoubanFolder(doubanPath):
    Log.d(tag, 'processDoubanFolder')
    for root, dirs, files in os.walk(doubanPath, True):
        for dirItem in dirs:
            matchObj = re.match(REGEX, dirItem)
            if (matchObj):
                filmName = matchObj.group(2).replace("·", "")
                path = os.path.join(root, dirItem)
                processDoubanFilm(path, filmName)
        deleteDownloadingFiles(root, files)


def processDoubanFilm(path, filmName):
    for root, dirs, files in os.walk(path, True):
        if (len(files) == 1 and Utils.isVideoFile(files[0])):
            processOneFilm(root, files[0], filmName)
        elif (len(files) == 0):
            Log.d(tag, "delete -- " + path)
            os.rmdir(path)

def processOneFilm(root, realFileName, filmName):
    realFilmName = Utils.videoFileName(realFileName)
    filmExtension = Utils.videoExtension(realFileName)
    realFullName = os.path.join(root, realFilmName) + "." + filmExtension
    targetFullName = os.path.join(root, filmName) + "." + filmExtension
    # rename film
    if (realFilmName != filmName):
        os.rename(realFullName, targetFullName)
    # copy to dest
    Log.d(tag, "from : " + targetFullName)
    Log.d(tag, "to : " + os.path.join(DOUBAN_PATH, filmName) + "." + filmExtension)
    move(targetFullName, os.path.join(DOUBAN_PATH, filmName) + "." + filmExtension)

def deleteDownloadingFiles(root, files):
    for file in files:
        reg = "^.*downloading$"
        if (re.match(reg, file)):
            path = os.path.join(root, file)
            Log.d(tag, "remove : " + path)
            os.remove(path)

if __name__ == '__main__':
    processDoubanFolder(DOUBAN_PATH)