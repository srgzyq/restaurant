# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from food.readXlsInfo import ReadXlsInfo

xlsInfoOne = ReadXlsInfo("./xlsOne.xls")

xlsInfoTwo = ReadXlsInfo("./xlsTwo.xls")

xlsOne = {
    "user":
    {
        "title": ["date", "people", "income", "company"],
        "ctype": [3, 2, 2, 1],
        "content":
        [[42472, 4, 300, 'didi'], [42472, 2, 215, 'other'], [42473, 4, 300, 'yaxin']]
    },
    "member":
    {
        "title": ["date", "num", "income"],
        "ctype": [3, 2, 2],
        "content":
        [[42472, 1, 20], [42472, 2, 40], [42473, 2, 40]]
    }
}


xlsTow = {
    "user":
    {
        "title": ["date", "people", "income", "company"],
        "ctype": [3, 2, 2, 1],
        "content":
        [[42472, 1, 12], [42472, 8, 600], [42472, 2, 180]]
    },
    "member":
    {
        "title": ["date", "num", "income"],
        "ctype": [3, 2, 2],
        "content":
        [[42470, 4, 80]]
    }
}
