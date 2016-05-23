# -*- coding: utf-8 -*-

import os
import re
from food.readXlsInfo import ReadXlsInfo
from food.combXlsData import CombXlsData
from food.writeXlsData import WriteXlsData
from dataInfo import getDirFileNameList, getNumWeek
from tool.dirTool import isFileExist, getLocalAndDropBoxPath
from tool.saveBackup import BackUpByDropBox
from time import sleep, strftime
from config import DIR_PATH, READ_PATH, WRITH_PATH, USER_FIRST_NAME, DATE_RE, FILE_XLS_END, SEPARATE_SIGN


def welcome():
    print "Welcome, " + USER_FIRST_NAME + "."
    print "Calendar starting..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Current time: " + strftime("%H:%M:%S")


def upDataToDropBox():
    dropBoxObj = BackUpByDropBox()
    rs = getLocalAndDropBoxPath(DIR_PATH)
    for localName, dropboxName in rs:
        dropBoxObj.uploadFile(localName, dropboxName)


def checkoutCombFileExist(year, month, weekNum):
    fileNames = getNumWeek(year, month, weekNum)
    read_xls_file = os.path.join(os.path.join(DIR_PATH, READ_PATH), str(month))
    dirFileNames = getDirFileNameList(fileNames, read_xls_file)
    isExist, eixtList = isFileExist(dirFileNames)
    return eixtList, isExist


def combMoreXleToOne(year, month, weekNum):
    dirFileNames, isExist = checkoutCombFileExist(year, month, weekNum)
    if not isExist:
        return

    comb = CombXlsData()
    for xlsfileName in dirFileNames:
        xlsFile = ReadXlsInfo(xlsfileName)
        comb.setXlsData(xlsFile)

    # 合并
    mergeData = comb.mergeData()

    # 写入文件
    outFileName = "_".join([str(month), str(weekNum), "week"]
                           ) + SEPARATE_SIGN + FILE_XLS_END
    fileName = os.path.join(os.path.join(DIR_PATH, WRITH_PATH), outFileName)
    # print fileName
    writeXls = WriteXlsData(mergeData)
    writeXls.wirteDataToXlsFile(fileName)


def startRestaurant():
    welcome()
    start = True
    while start:
        user_choice = raw_input("C to comb, B to Backup, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'C':
            yearInfo = raw_input("Enter year month weekNum (2016/5/3) :")
            if re.match(DATE_RE, yearInfo):
                year, month, weekNum = yearInfo.split("/")
                combMoreXleToOne(int(year), int(month), int(weekNum))
        elif user_choice == 'B':
            pass
        elif user_choice == 'X':
            start = False
        else:
            print "An invalid command was entered."
            start = False

if __name__ == '__main__':
    startRestaurant()
    #upDataToDropBox()
