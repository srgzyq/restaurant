# -*- coding: utf-8 -*-

TITLE_KEY = 'title'
CONTENT_KEY = 'content'


class CombXlsData(object):

    """docstring for CombXlsData"""

    def __init__(self):
        super(CombXlsData, self).__init__()
        self.doMergeData = []
        self.result = {}

    def setXlsData(self, xlsData):
        assert xlsData is not None, "xls Data is None"
        self.doMergeData.append(xlsData)

    def getResultData(self):
        return self.result

    def mergeData(self):
        self.initTableInfo()
        self.initTableTitleInfo()
        self.mergeTableContent()
        return self.result

    def initTableInfo(self):
        result = self.result
        # 合并xls结构一致，取出第一个即可
        assert len(self.doMergeData) > 0, "doMergeData not have value"
        xlsData = self.doMergeData[0]
        for sheetKey in xlsData.getXlsSheetsName():
            if result.get(sheetKey) is None:
                result[sheetKey] = {TITLE_KEY: [], CONTENT_KEY: []}

    def initTableTitleInfo(self):
        result = self.result
        # 合并xls结构一致，取出第一个即可
        assert len(self.doMergeData) > 0, "doMergeData not have value"
        xlsData = self.doMergeData[0]
        for sheetKey, sheetInfo in result.items():
            sheetInfo[TITLE_KEY] = xlsData.getXlsSheetsTitle(sheetKey)

    def mergeTableContent(self):
        result = self.result
        for xlsData in self.doMergeData:
            sheetDatas = xlsData.getXlsSheetsInfo()
            for sheetName, sheetContents in sheetDatas:
                sheetCon = result[sheetName][CONTENT_KEY]
                for line in sheetContents:
                    sheetCon.append(line)
