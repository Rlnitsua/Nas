#coding=utf-8

import sys
import DSFilmNameProcessor

tag = 'main'

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		DSFilmNameProcessor.processCurrentFolder(sys.argv[1])
	elif (len(sys.argv) == 3):
		DSFilmNameProcessor.processCurrentFolder(sys.argv[1], sys.argv[2])