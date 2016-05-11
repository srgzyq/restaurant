# -*- coding: utf-8 -*-
import calendar

FILE_END = "xlsx"


def getFileNameList(start, step=7):
    datelist = start.split(".")
    year = int(datelist[0])
    month = int(datelist[1])
    day = int(datelist[2]) - 1
    monthRange = calendar.monthrange(year, month)
    result = []

    for num in range(step):
        day += 1
        if day > monthRange[1]:
            day = 1
            month += 1

        datestr = ".".join([str(year), str(month), str(day), FILE_END])
        result.append(datestr)
    return result


def getDirFileNameList(fileList, dirName):
    result = []
    for fileName in fileList:
        result.append(dirName + fileName)
    return result
