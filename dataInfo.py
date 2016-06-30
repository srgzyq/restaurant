# -*- coding: utf-8 -*-
import calendar
import os

from config import *
from tool.dirTool import isFileExist
from datetime import datetime
from datetime import timedelta
import yaml


def changeXlsDateToStr(dateNum):
    baseDay = datetime(1899, 12, 30)
    changeDay = baseDay + timedelta(days=+dateNum)
    dayStr = changeDay.strftime("%Y/%m/%d")
    return dayStr


def getYamlConfig(key):
    confFile = open(XLSANDDB_YAML_CON)
    confData = yaml.load(confFile)
    return confData[key]


def getDirFileNameList(fileList, dirName):
    result = []
    for fileName in fileList:
        monthNum = getMonthNumber(fileName)
        pathName = os.path.join(dirName, monthNum)
        result.append(os.path.join(pathName, fileName))
    return result


def checkoutCombFileExist(year, month, weekNum):
    fileNames = getNumWeek(year, month, weekNum)
    read_xls_file = os.path.join(DIR_PATH, READ_PATH)
    dirFileNames = getDirFileNameList(fileNames, read_xls_file)
    isExist, eixtList = isFileExist(dirFileNames)
    return eixtList, isExist


def getMonthNumber(fileName):
    dateList = fileName.split('.')  # ['2016', '5', '30', 'xlsx']
    return dateList[1]  # month


def getWeekInfoList(year, month):
    weekday, lastday = calendar.monthrange(year, month)
    # 计算一周0~6 6-当前周几+1 第一个星期天
    # 一月天数lastday
    # _sundays 每周的日历
    _sundays = [x for x in range(6 - weekday + 1, lastday + 1, WEEK_DAY_NUM)]
    # print _sundays

    monthList = range(1, lastday + 1)
    weeks = []

    for index in range(len(_sundays) + 1):
        if index == 0:
            weeks.append(monthList[0:_sundays[index]])
        elif index == len(_sundays) and _sundays[index - 1] != lastday:
            weeks.append(monthList[_sundays[index - 1]:])
        elif index != len(_sundays):
            weeks.append(monthList[_sundays[index - 1]:_sundays[index]])

    return weeks


def getAllWeekInfoList(year, month):
    curMonth = getWeekInfoList(year, month)

    # print curMonth
    monthList = curMonth[:]
    # 完整的一周结尾
    if len(curMonth[len(curMonth) - 1]) != WEEK_DAY_NUM:
        nextMonthNum = month % LAST_MONTH_NUM + 1
        nextYear = year
        if month % LAST_MONTH_NUM == 0:
            nextYear += 1
        # 下个月的开头
        nextMonth = getWeekInfoList(nextYear, nextMonthNum)
        monthList = curMonth[:len(curMonth)]
        monthList[len(monthList) - 1] += nextMonth[0]
        #monthList.append(curMonth[len(curMonth) - 1] + nextMonth[0])

    # print monthList
    return monthList


def getFormatDate(year, month):
    monthList = getAllWeekInfoList(year, month)
    weekday, lastday = calendar.monthrange(year, month)
    isNextMonth = False
    isNextYear = (month % LAST_MONTH_NUM == 0)
    curMonth = month
    curYear = year
    result = []
    for weeks in monthList:
        weekList = []
        for day in weeks:
            # 跨年 # 跨月
            if isNextMonth and not isNextYear:
                curMonth = month + 1
            elif isNextMonth and isNextYear:
                curMonth = 1
                curYear = year + 1

            datestr = SEPARATE_SIGN.join(
                [str(curYear), str(curMonth), str(day), FILE_END])
            weekList.append(datestr)

            if day == lastday:
                isNextMonth = True

        result.append(weekList)

    return result


def getNumWeek(year, month, num):
    return getFormatDate(year, month)[num - 1]
