#-*- encoding: utf-8 -*-
'''
Created on 2016-05-23 15:54:21

@author: Srgzyq
'''

import unittest
from tool.saveBackup import BackUpByDropBox


class TestBackUpByDropBox(unittest.TestCase):

    def setUp(self):
        # print "setUp.."
        self.dropBoxObj = BackUpByDropBox()

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_initDropBoxInfo(self):
        pass

    def test_uploadFile(self):
        pass
        self.dropBoxObj.uploadFile(
            u"/Users/playcrab/工作/自我文档总结/极加/数据/原数据/5/2016.5.10.xlsx", u"/Test/5/2016.5.10.xlsx")


if __name__ == '__main__':
    unittest.main()
