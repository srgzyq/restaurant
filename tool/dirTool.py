#-*- coding: utf-8 -*-
import os

def getAllFileName(path):
	for fileName in os.listdir(path):
		if os.path.isdir(fileName):
			getAllFileName(fileName)
		else:
			print fileName
