#-*- coding: utf-8 -*-
import os
import myLogging
# 回调函数的写法

DIR_PATH = "/Users/playcrab/工作/自我文档总结/极加/数据"


def getAllFileName(path, rs):
    for fileName in os.listdir(path):

        # abspathName = os.path.abspath(fileName)
        # print "fileName:"+fileName

        curFileName = os.path.join(path, fileName)
        print os.path.dirname(curFileName)
        # print curFileName
        # print abspathName
        # print "is right"+ str(os.path.exists(abspathName))
        # print "isdir:" + str(os.path.isdir(fileName))
        if os.path.isdir(curFileName):

            # print "abspath:" + curFileName
            getAllFileName(curFileName, rs)
        elif os.path.isfile(curFileName):
            # 返回后缀
            name, suffix = os.path.splitext(fileName)
            if suffix == '.xls' or suffix == '.xlsx':
                # print name
                # print suffix
                rs.append(curFileName)

# 文件是否存在


def isFileExist(fileNameList):
    eixtList = []
    isExis = True
    for fileName in fileNameList:
        if not os.path.exists(fileName):
            myLogging.logging.info("fileName:" + fileName + " is not exist.")
            isExis = False
        else:
            eixtList.append(fileName)
    return isExis, eixtList


def getAbsFileNameList(path):
    result = []
    getAllFileName(path, result)
    return result


def getAllFileNameList(path):
    pass


def oppositeFileNameList(path):
    result = getAbsFileNameList(path)
    resultOpp = []
    for fileName in result:
        splitDir = fileName.split(DIR_PATH)
        if len(splitDir) == 2:
            resultOpp.append(splitDir[1])
    return resultOpp
