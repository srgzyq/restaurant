# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from food.readXlsInfo import ReadXlsInfo

xlsInfoOne = ReadXlsInfo("./xlsOne.xls")

xlsInfoTwo = ReadXlsInfo("./xlsTwo.xls")

xlsOne = {
    "user":
    {
        "title": ["date", "people", "income","company"],
        "content":
        [["2016/4/25", 4, 300,'didi'], ["2016/4/25", 2, 215,'other'], ["2016/4/25", 4, 300,'yaxin']]
    },
    "member":
    {
        "title": ["date", "num", "income"],
        "content":
        [["2016/4/25", 1, 20], ["2016/4/25", 2, 40],["2016/4/25", 2, 40]]
    }
}


xlsTow = {
    "user":
    {
        "title": ["date", "people", "income","company"],
        "content":
        [["2016/4/26", 1, 12], ["2016/4/26", 8, 600], ["2016/4/26", 2, 180]]
    },
    "member":
    {
        "title": ["date", "num", "income"],
        "content":
        [["2016/4/26", 4, 80]]
    }
}
