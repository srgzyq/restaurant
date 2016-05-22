#-*- coding: utf-8 -*-
import os


DIR_PATH = "/Users/playcrab/工作/自我文档总结/极加/数据"

def getAllFileName(path,rs):
	for fileName in os.listdir(path):
	
		#abspathName = os.path.abspath(fileName)
		#print "fileName:"+fileName
		curFileName = os.path.join(path, fileName)
		#print curFileName
		#print abspathName
		#print "is right"+ str(os.path.exists(abspathName))
		#print "isdir:" + str(os.path.isdir(fileName))
		if os.path.isdir(curFileName):
			
			#print "abspath:" + curFileName
			getAllFileName(curFileName,rs)
		elif os.path.isfile(curFileName):
			# 返回后缀
			name,suffix = os.path.splitext(fileName)
			if suffix == '.xls' or suffix == '.xlsx':
				#print name
				#print suffix
				rs.append(curFileName)

def getFileNamelist(path):
	result = []
	getAllFileName(path,result)
	return result