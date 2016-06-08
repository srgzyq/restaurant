#-*- encoding: utf-8 -*-
'''
Created on 2016-06-08 14:24:04

@author: Srgzyq
'''
from tool.saveBackup import BackUpByDropBox
import myLogging
from config import *
from tool.dirTool import getLocalAndDropBoxPath, changeLocalToDropBox
import sys
from dataInfo import checkoutCombFileExist
import os


def upDataAllFillToDropBox():
    dropBoxObj = BackUpByDropBox()
    rs = getLocalAndDropBoxPath(DIR_PATH)
    for localName, dropboxName in rs:
        isExist = dropBoxObj.isFileExist(dropboxName)
        if isExist:
            myLogging.logging.info(dropboxName + " is exits")
        else:
            dropBoxObj.uploadFile(localName, dropboxName)
    myLogging.logging.info(DIR_PATH + " all files upload success!")


def getCurFileToDropBox(yearMonthWeekStr):
    dropBoxObj = BackUpByDropBox()
    year, month, weekNum = yearMonthWeekStr.split("/")
    print year, month, weekNum
    dirFileNames, isExist = checkoutCombFileExist(
        int(year), int(month), int(weekNum))

    # 导出文件
    outFileName = "_".join([month, weekNum, "week"]
                           ) + SEPARATE_SIGN + FILE_XLS_END
    fileName = os.path.join(os.path.join(DIR_PATH, WRITH_PATH), outFileName)
    dirFileNames.append(fileName)

    for localName in dirFileNames:
        dropboxName = changeLocalToDropBox(localName)
        isExist = dropBoxObj.isFileExist(dropboxName)
        if isExist:
            myLogging.logging.info(dropboxName + " is exits")
        else:
            #print "localName===", localName
            #print "dropboxName===", dropboxName
            dropBoxObj.uploadFile(localName, dropboxName)


if __name__ == '__main__':
    assert len(sys.argv) == 2, 'input arg is error'
    getCurFileToDropBox(sys.argv[1])
