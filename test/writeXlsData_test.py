import unittest
import FakeData
# -*- coding: utf-8 -*-
#import sys
#sys.path.append("..")
from config import CONTENT_KEY
from food.writeXlsData import WriteXlsData
from food.readXlsInfo import ReadXlsInfo


class TestWriteXlsData(unittest.TestCase):

    def setUp(self):
        fileName = "./wirtexls.xls"
        self.data = WriteXlsData(FakeData.xlsNewOne)
        self.data.wirteDataToXlsFile(fileName)
        self.readData = ReadXlsInfo(fileName)

    def tearDown(self):
        pass

    def test_wirteDataToXlsFile(self):
        pass

    def test_initSheetTitle(self):
        self.assertEquals(
            len(self.readData.getXlsSheetsName()), len(FakeData.xlsNewOne))
        self.assertTrue("user" in (self.readData.getXlsSheetsName()))
        self.assertTrue("member" in (self.readData.getXlsSheetsName()))

    def test_initSheetContent(self):
        contents = self.readData.getXlsSheetsInfo()
        for key in FakeData.xlsNewOne:
            for content in contents:
                if content[0] == key:
                    self.assertEquals(len(content[1]), len(
                        FakeData.xlsNewOne[key][CONTENT_KEY]))


if __name__ == '__main__':
    unittest.main()
