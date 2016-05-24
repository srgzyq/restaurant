#-*- encoding: utf-8 -*-
'''
Created on 2016-05-23 15:54:21

@author: Srgzyq
'''

import unittest
from tool.saveBackup import BackUpByDropBox


class TestBackUpByDropBox(unittest.TestCase):
    dropBoxObj = BackUpByDropBox()

    def setUp(self):
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_initDropBoxInfo(self):
        pass

    def test_uploadFile(self):
        fileName = u"/Test/模板/模板.xlsx"
        isExit = self.dropBoxObj.isFileExist(fileName)
        if isExit:
            self.dropBoxObj.delFile(fileName)

        self.dropBoxObj.uploadFile(
            u"/Users/playcrab/工作/自我文档总结/极加/数据/模板/模板.xlsx", fileName)

        self.assertTrue(self.dropBoxObj.isFileExist(fileName))

    def test_isFileExist(self):
        isExit = self.dropBoxObj.isFileExist("Getting Started.pdf")
        self.assertTrue(isExit)
        isExit = self.dropBoxObj.isFileExist(u"/Test/2016.5.11.xlsx")
        self.assertTrue(not isExit)

    def test_delFile(self):
        pass


if __name__ == '__main__':
    unittest.main()
