# -*- coding: utf-8 -*-

from food.readXlsInfo import ReadXlsInfo
from food.combXlsData import CombXlsData
from food.writeXlsData import WriteXlsData
from dataInfo import getFileNameList, getDirFileNameList

DIR_PATH = "/Users/playcrab/工作/自我文档总结/极加/数据/"   #"./data/"
INPUT_FILE_LIST = []
OUTPUT_FILE = ""


if __name__ == '__main__':

    fileNames = getFileNameList("2016.5.9",7)
    dirFileNames = getDirFileNameList(fileNames, DIR_PATH)
    #print dirFileNames
    
    comb = CombXlsData()
    for xlsfileName in dirFileNames:
    	xlsFile = ReadXlsInfo(xlsfileName)
        comb.setXlsData(xlsFile)
  	
  	# 合并
    mergeData = comb.mergeData()

    # 写入文件
    fileName = DIR_PATH+"汇总/"+"5_3_week.xls"
    writeXls = WriteXlsData(mergeData)
    writeXls.wirteDataToXlsFile(fileName)


    
