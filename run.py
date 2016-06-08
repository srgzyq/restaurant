# -*- coding: utf-8 -*-

import os
import re
import myLogging
from food.readXlsInfo import ReadXlsInfo
from food.combXlsData import CombXlsData
from food.writeXlsData import WriteXlsData
from dataInfo import checkoutCombFileExist
from tool.dirTool import getLocalAndDropBoxPath
from tool.saveBackup import BackUpByDropBox
from time import sleep, strftime
from config import *
import subprocess


def welcome():
    print "Welcome, " + USER_FIRST_NAME + "."
    print "Calendar starting..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Current time: " + strftime("%H:%M:%S")


# def upDataToDropBox():
#     dropBoxObj = BackUpByDropBox()
#     rs = getLocalAndDropBoxPath(DIR_PATH)
#     for localName, dropboxName in rs:
#         isExist = dropBoxObj.isFileExist(dropboxName)
#         if isExist:
#             myLogging.logging.info(dropboxName + " is exits")
#         else:
#             dropBoxObj.uploadFile(localName, dropboxName)
#     myLogging.logging.info(DIR_PATH + " all files upload success!")


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

                # 执行:proxychains4 python
                yes_backup = raw_input('Is upload current file (yes or no)? ')
                if yes_backup.strip().lower() == 'yes':
                    cmd = "proxychains4 python upLoadFile.py " + yearInfo
                    subprocess.call([cmd], shell=True)

        elif user_choice == 'B':
            pass
        elif user_choice == 'X':
            start = False
        else:
            print "An invalid command was entered."
            start = False

if __name__ == '__main__':
    startRestaurant()
    # upDataToDropBox()
