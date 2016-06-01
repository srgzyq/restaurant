# -*- coding: utf-8 -*-


from config import TITLE_KEY, CONTENT_KEY, TYPE_KEY
import myLogging


class CombXlsData(object):

    """docstring for CombXlsData"""

    def __init__(self):
        super(CombXlsData, self).__init__()
        self.doMergeData = []
        self.result = []  # {}

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
        # 合并xls结构一致，取出第一个即可
        assert len(self.doMergeData) > 0, "doMergeData not have value"
        xlsData = self.doMergeData[0]
        for sheetKey in xlsData.getXlsSheetsName():
            dicSheetInfo = {"name": sheetKey, TITLE_KEY: [],
                            CONTENT_KEY: [], TYPE_KEY: []}
            self.result.append(dicSheetInfo)

    def initTableTitleInfo(self):
        result = self.result
        # 合并xls结构一致，取出第一个即可
        assert len(self.doMergeData) > 0, "doMergeData not have value"
        xlsData = self.doMergeData[0]
        for sheetInfo in result:
            sheetKey = sheetInfo["name"]
            sheetInfo[TITLE_KEY] = xlsData.getXlsSheetsTitle(sheetKey)
            sheetInfo[TYPE_KEY] = xlsData.getXlsSheetsValueType(sheetKey)

    def getSheetContentList(self, sheetName, result):
        lines = []
        for sheetInfo in result:
            if sheetInfo["name"] == sheetName:
                lines = sheetInfo[CONTENT_KEY]
                break
        return lines

    def mergeTableContent(self):
        result = self.result
        assert len(result) != 0, "result is None"
        for xlsData in self.doMergeData:
            sheetDatas = xlsData.getXlsSheetsInfo()
            for sheetName, sheetContents in sheetDatas:
                try:
                    lines = self.getSheetContentList(sheetName, result)
                except KeyError:
                    myLogging.logging.error(
                        "fileName:" + xlsData.getFileName() + " sheetName is error: " + sheetName)

                for line in sheetContents:
                    lines.append(line)
            myLogging.logging.info(
                "Merge xls file in Dic:" + xlsData.getFileName() + " succeed.")
