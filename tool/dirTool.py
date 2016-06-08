#-*- coding: utf-8 -*-
import os
import myLogging
from config import DIR_PATH, DROPBOX_DIR_PATH
# 回调函数的写法


def getAllFileName(pathName, rs):
    for fileName in os.listdir(pathName):

        # abspathName = os.path.abspath(fileName)
        # print "fileName:"+fileName

        curFileName = os.path.join(pathName, fileName)
        # print os.path.dirname(curFileName)
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


def getAbsFileNameList(pathName):
    result = []
    getAllFileName(pathName, result)
    return result


def getAllFileNameList(pathName):
    pass


def oppositeFileNameList(pathName):
    result = getAbsFileNameList(pathName)
    resultOpp = []
    for fileName in result:
        splitDir = fileName.split(DIR_PATH)
        if len(splitDir) == 2:
            resultOpp.append(splitDir[1])
    return resultOpp


def getLocalAndDropBoxPath(pathName):
    result = []
    oppositeFileList = oppositeFileNameList(pathName)
    for fileName in oppositeFileList:
        localPath = DIR_PATH + fileName
        dropBoxPath = DROPBOX_DIR_PATH + fileName
        result.append((localPath, dropBoxPath))
    return result


def changeLocalToDropBox(localName):
    splitDir = localName.split(DIR_PATH)
    dropBoxPath = None
    if len(splitDir) == 2:
        dropBoxPath = DROPBOX_DIR_PATH + splitDir[1]
    return dropBoxPath
