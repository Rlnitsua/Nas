import re

reg = '^.*[mp4|rmvb|avi|mkv|3gp|wmv|divx|flv|f4v|mov|ogg]$'

def isVideoFile(fileName):
	matchObj = re.match(reg, fileName, re.I)
	if matchObj:
		return True
	else:
		return False