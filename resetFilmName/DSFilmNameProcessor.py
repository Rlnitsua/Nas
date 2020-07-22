#coding=utf-8

import os
import sys
import Constant

sys.path.append('..')
from utils import Log
from utils import Utils

tag = 'DSFilmNameProcessor'

def processCurrentFolder(path, handle = False):
	for root, dirs, files in os.walk(path, True):
		Log.d(tag, '---- handle current Path : ' + root + ' ---')
		Log.d(tag, 'dirs len : ' + str(len(dirs)) + ' files : ' + str(len(files)))
		for fileName in files:
			if (Utils.isVideoFile(fileName)) :
				Log.d(tag, 'handle file : ' + fileName)
				processOneFile(root, fileName, handle)
			else:
				Log.d(tag, '[' + fileName + ']' + ' is not video file !')
				continue

def processOneFile(root, fileName, handle):
	pointIndex = fileName.rfind('.')
	originFilmName = fileName[:pointIndex]
	extensionName = fileName[pointIndex + 1:]
	currentFileName = processFilmName(originFilmName) + '.' + extensionName
	if (fileName != currentFileName) :
		Log.d(tag, 'reset FileName to ---> [' + currentFileName + '] <---')
		if (handle):
			os.system('mv ' + os.path.join(root, fileName) + " " + os.path.join(root, currentFileName))

def processFilmName(originFilmName):
	for tag in Constant.DEL_TAG:
		if (originFilmName.find(tag) != -1) :
			newFilmName = originFilmName.replace(tag, '')
			return processFilmName(newFilmName)
	return originFilmName