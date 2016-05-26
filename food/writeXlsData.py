# -*- coding: utf-8 -*-
from xlwt import Workbook, XFStyle, easyxf
from config import TITLE_KEY, CONTENT_KEY, TYPE_KEY, XL_CELL_DATE
import myLogging

style_date = easyxf(num_format_str='YY/MM/DD')


class WriteXlsData(object):

    """docstring for WriteXlsData"""

    def __init__(self, data):
        super(WriteXlsData, self).__init__()
        self.data = data

    # 写入
    def wirteDataToXlsFile(self, fileName):
        xlsData = Workbook()
        for sheetName, sheetData in self.data.items():
            # sheet
            xlsSheet = xlsData.add_sheet(sheetName)
            # title
            sheetTitle = sheetData[TITLE_KEY]
            # content
            sheetContent = sheetData[CONTENT_KEY]
            # type
            sheetTypes = sheetData[TYPE_KEY]

            self.initSheetTitle(xlsSheet, sheetTitle)
            self.initSheetContent(xlsSheet, sheetContent, sheetTypes)

        xlsData.save(fileName)
        myLogging.logging.info("Save xls file:" + fileName + " succeed.")

    def initSheetTitle(self, xlsSheet, sheetTitle):
        # 初始化每一个 sheet title 内容
        for col, value in enumerate(sheetTitle):
            xlsSheet.write(0, col, value)
        return xlsSheet

    def initSheetContent(self, xlsSheet, sheetContent, sheetTypes):
        # 第一行开始
        rows = len(sheetContent)
        for index in range(rows):
            row = index + 1
            rowValue = sheetContent[index]
            for col, value in enumerate(rowValue):
                #xlsSheet.write(row, col, value)
                if XL_CELL_DATE == sheetTypes[col]:
                    xlsSheet.write(row, col, value, style_date)
                else:
                    xlsSheet.write(row, col, value)
