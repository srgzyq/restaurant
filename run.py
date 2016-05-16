# -*- coding: utf-8 -*-

from food.readXlsInfo import ReadXlsInfo
from food.combXlsData import CombXlsData
from food.writeXlsData import WriteXlsData
from dataInfo import getDirFileNameList, getNumWeek
import os

DIR_PATH = "/Users/playcrab/工作/自我文档总结/极加/数据"
READ_PATH = "原数据"
WRITH_PATH = "汇总"
INPUT_FILE_LIST = []
OUTPUT_FILE = ""


if __name__ == '__main__':

    fileNames = getNumWeek(2016, 5, 3)

    read_xls_file = os.path.join(DIR_PATH, READ_PATH)
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
