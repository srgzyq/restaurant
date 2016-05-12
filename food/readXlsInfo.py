# -*- coding: utf-8 -*-
from xlrd import open_workbook
from config import IGNORE_SHEETS
import myLogging


class ReadXlsInfo(object):

    def __init__(self, file_name):
        super(ReadXlsInfo, self).__init__()
        try:
            self.file_name = file_name
            self.xls_file = open_workbook(file_name)
            myLogging.logging.info("Read xls file from: " + file_name + " succeed.")
        except IOError:
            # 日志输出:
            myLogging.logging.error("No such file or directory: " + file_name)

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
