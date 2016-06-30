# -*- coding: utf-8 -*-
from xlrd import open_workbook
from config import IGNORE_SHEETS
import myLogging
from dataInfo import getYamlConfig, changeXlsDateToStr


class ReadXlsInfo(object):

    def __init__(self, file_name):
        super(ReadXlsInfo, self).__init__()
        try:
            self.file_name = file_name
            self.xls_file = open_workbook(file_name)
            myLogging.logging.info(
                "Read xls file from: " + file_name + " succeed.")
        except IOError:
            # 日志输出:
            myLogging.logging.error("No such file or directory: " + file_name)
            exit()

    def getFileName(self):
        return self.file_name

    def getXlsSheetsName(self):
        names = self.xls_file.sheet_names()
        result = []
        for name in names:
            if name not in IGNORE_SHEETS:
                result.append(name)
        return result

    def getXlsSheetsTitle(self, name):
        sheet = self.xls_file.sheet_by_name(name)
        titles = sheet.row_values(0)  # 默认第一行是title
        return titles

    def getXlsSheetsValueType(self, name):
        sheet = self.xls_file.sheet_by_name(name)
        # print "getXlsSheetsValueType",name
        # print sheet.row_values(1)
        try:
            types = sheet.row_types(1)
        except IndexError:
            types = [0] * len(sheet.row_values(0))
        #types = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return types

    def getXlsSheetsContent(self, name):
        sheet = self.xls_file.sheet_by_name(name)
        line_contents = []

        # 第二行开始到末尾
        for line_num in range(1, sheet.nrows):
            line_content = sheet.row_values(line_num)
            line_contents.append(line_content)

        return line_contents

    def getXlsSheetsInfo(self):
        sheet_names = self.getXlsSheetsName()
        result = []
        for name in sheet_names:
            result.append((name, self.getXlsSheetsContent(name)))

        return result


class ReadXlsFormat(ReadXlsInfo):

    def __init__(self, file_name):
        super(ReadXlsFormat, self).__init__(file_name)
        self.xlsStrInfoDic = getYamlConfig('XLSTITLE')

    def formatContent(self, name):
        sheet = self.xls_file.sheet_by_name(name)
        titles = self.getXlsSheetsTitle(name)
        for line_num in range(1, sheet.nrows):
            line_content = sheet.row_values(line_num)
            self.resolutionContent(line_content, titles)
            # print line_content

    def resolutionContent(self, line_content, titles):
        sqlCont = []
        print '------------'
        for title in titles:

            infoData = self.xlsStrInfoDic[title]
            index = infoData['index']
            ctype = infoData['type']
            if index >= 0:
                value = line_content[index]
                if ctype == 'date':
                    value = changeXlsDateToStr(value)
                if value is '':
                    value = 1

                sqlCont.append(value)

        print tuple(sqlCont)
        print '------------'
