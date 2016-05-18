# -*- coding: utf-8 -*-

from food.readXlsInfo import ReadXlsInfo
from food.combXlsData import CombXlsData
from food.writeXlsData import WriteXlsData
from dataInfo import getDirFileNameList, getNumWeek
import os
import re
from time import sleep, strftime

DIR_PATH = "/Users/playcrab/工作/自我文档总结/极加/数据"
READ_PATH = "原数据"
WRITH_PATH = "汇总"
INPUT_FILE_LIST = []
OUTPUT_FILE = ""
USER_FIRST_NAME = "srgzyq"
# 2016/5/3
DATE_RE = "^\d{4}/([0][1-9]|[1-9]|[1][0-2])/([1-9]|0[1-9]|[1-3][0-9])$"


def welcome():
    print "Welcome, " + USER_FIRST_NAME + "."
    print "Calendar starting..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "Current time: " + strftime("%H:%M:%S")


def combMoreXleToOne(year, month, weekNum):
    fileNames = getNumWeek(year, month, weekNum)
    read_xls_file = os.path.join(os.path.join(DIR_PATH, READ_PATH), str(month))
    dirFileNames = getDirFileNameList(fileNames, read_xls_file)

    comb = CombXlsData()
    for xlsfileName in dirFileNames:
        xlsFile = ReadXlsInfo(xlsfileName)
        comb.setXlsData(xlsFile)

    # 合并
    mergeData = comb.mergeData()

    # 写入文件
    # DIR_PATH + "汇总/" + "5_3_week.xls"
    fileName = os.path.join(os.path.join(DIR_PATH, WRITH_PATH), "5_3_week.xls")
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
    #combMoreXleToOne(2016, 5, 3)
