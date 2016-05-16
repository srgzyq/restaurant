# -*- coding: utf-8 -*-

from food.readXlsInfo import ReadXlsInfo
from food.combXlsData import CombXlsData
from food.writeXlsData import WriteXlsData
from dataInfo import getFileNameList, getDirFileNameList

DIR_PATH = "./data/"
INPUT_FILE_LIST = []
OUTPUT_FILE = ""


if __name__ == '__main__':

    fileNames = getFileNameList("2016.4.25",6)
    dirFileNames = getDirFileNameList(fileNames, DIR_PATH)
    print dirFileNames
    '''
    comb = CombXlsData()
    for xlsfileName in dirFileNames:
    	xlsFile = ReadXlsInfo(xlsfileName)
        comb.setXlsData(xlsFile)
  	
  	# 合并
    mergeData = comb.mergeData()

    # 写入文件
    fileName = DIR_PATH+"all.xls"
    writeXls = WriteXlsData(mergeData)
    writeXls.wirteDataToXlsFile(fileName)


    '''
