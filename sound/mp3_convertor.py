# -*- coding: utf-8 -*- 

import os	
from os import listdir

def MakeSound(filename):

	os.system("echo Y| ffmpeg -i ./original/" + filename + " -acodec libmp3lame -ac 1 -ab 128k ./result/" + filename[:-4] + '.mp3')

def init():
	print ('MakeSound Start!')

	filepath =os.getcwd() + "/original"

	for x in listdir(filepath):
		print(x)
		MakeSound(x)

	print ('Finish!')

init()