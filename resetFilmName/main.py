#coding=utf-8

import DSFilmNameProcessor
import Log
import Constant

tag = 'main'

if __name__ == '__main__':
	Log.d(tag, "main function invoke !")
	DSFilmNameProcessor.processCurrentFolder(Constant.FILM_PATH)