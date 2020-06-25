#coding=utf-8

FILM_PATH = '/var/services/video/电影'

PREFIX_LIST = ['电影天堂www.dygod.org', 
			'电影天堂www.dy2018.com', 
			'电影天堂www.dy2018.net', 
			'阳光电影-www.ygdy8.com',
			'电影天堂-wwwdy2018net',
			'阳光电影www.ygdy8.com', 
			'电影天堂wwwdy2018net',
			'6v电影www.dy131.com',
			'3E电影站www.eee4.com',
			'3E电影站www.eee4.com',
			'66影视www.66ys.cn',
			'66影视wwwdy131com',
			'小调网-www.xiaodiao.com',
			'更多电影请去www.6vdy.net',
			'电影天堂wwwdygodcom',
			'wwwdy131com']


SYMBOL_LIST = ['.', '[', ']', '【', '】']

QUALITY_LIST = ['BD', 'HD', 'DVD', '720p', '1080p', '1024', '1280',
	'1024x576', 'x576', 'x560', '1280x692', '高清', '分辨率', '无水印']

SOUND_TRACK_LIST = ['国英双语双字', '中文字幕', '国语配音', '国语修正', '中英双字幕',
		'中英字幕', '国语中字', '国粤双语', '国粤日三语', '国粤英三语', '英国粤三语', '国粤日三语',
		'国粤日3语', '英国粤台四音轨', '国语无字幕', '国语', '韩语', '日语', '国日', '粤语', 
		'中英双字', '中字', '双语', '无字幕版']

DEL_TAG = PREFIX_LIST + SYMBOL_LIST + QUALITY_LIST + SOUND_TRACK_LIST