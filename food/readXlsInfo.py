# -*- coding: utf-8 -*-
from xlrd import open_workbook


class ReadXlsInfo(object):

    def __init__(self, file_name):
        super(ReadXlsInfo, self).__init__()
        self.xls_file = open_workbook(file_name)

    def getXlsSheetsName(self):
        return self.xls_file.sheet_names()

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
