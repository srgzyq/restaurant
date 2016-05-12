# -*- coding: utf-8 -*-
import calendar

FILE_END = "xlsx"
WEEK_DAY_NUM = 7
LAST_MONTH_NUM = 12

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

# 周月按照周日划分日期


def getWeekInfoList(year, month):
    weekday, lastday = calendar.monthrange(year, month)
    # 计算一周0~6 6-当前周几+1 第一个星期天
    # 一月天数lastday
    # _sundays 每周的日历
    _sundays = [x for x in range(6 - weekday + 1, lastday + 1, WEEK_DAY_NUM)]
    #print _sundays

    monthlist = range(1, lastday + 1)
    weeks = []

    for index in range(len(_sundays) + 1):
        if index == 0:
            weeks.append(monthlist[0:_sundays[index]])
        elif index == len(_sundays) and _sundays[index - 1] != lastday:
            weeks.append(monthlist[_sundays[index - 1]:])
        elif index != len(_sundays):
            weeks.append(monthlist[_sundays[index - 1]:_sundays[index]])

    return weeks

def getAllWeekInfoList(year,month):
    curMonth = getWeekInfoList(year,month)
    #print curMonth
    monthList = curMonth[:]
    # 完整的一周结尾
    if len(curMonth[len(curMonth)-1]) != WEEK_DAY_NUM:
        nextMonthNum = month%LAST_MONTH_NUM+1
        nextYear = year
        if month%LAST_MONTH_NUM == 0:
            nextYear += 1
        nextMonth = getWeekInfoList(nextYear,nextMonthNum)
        monthList = curMonth[:len(curMonth)]
        monthList.append(curMonth[len(curMonth)-1]+nextMonth[0])

    # 格式化
    return monthList

def test_getWeekInfoList():
    w = getWeekInfoList(2016, 5)
    #print w
    assert len(w[0]) == 1 ,'first is one'
    assert len(w[len(w)-1]) == 2 ,'last is one'
    assert len(w) == 6 ,'last is one'
    w = getWeekInfoList(2015, 5)
    assert len(w[len(w)-1]) == 7, 'last is all week' 
    w = getWeekInfoList(2015,6)
    assert len(w[0]) == 7, 'first is all week'
    #print w

if __name__ == '__main__':
    #getAllWeekInfoList(2016,8)
    print getAllWeekInfoList(2016,4)
    #getAllWeekInfoList(2016,12)
    #getAllWeekInfoList(2015,5)
    #print getWeekInfoList(2015,6)
    #test_getWeekInfoList()
    
