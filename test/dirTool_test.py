#-*- encoding: utf-8 -*-
'''
Created on 2016-05-22 17:52:54

@author: Srgzyq
'''

import unittest
from config import DIR_PATH


from tool.dirTool import getAbsFileNameList, oppositeFileNameList, isFileExist


class TestDirTool(unittest.TestCase):

    def setUp(self):
        # print "setUp.."
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_isFileExist(self):
        a = ["a.py", "b.py"]
        self.assertEquals(isFileExist(a)[0], False)
        self.assertEquals(len(isFileExist(a)[1]), 0)

    def test_getAbsFileNameList(self):
        print "DIR_PATH:" + DIR_PATH
        rs = getAbsFileNameList(DIR_PATH)
        for filename in rs:
            print "xls:" + filename

        # b="/Users/playcrab/工作/自我文档总结/极加/数据/原数据/5/2016.5.10.xlsx"
        b = "/Users/playcrab/工作/自我文档总结/极加/数据/汇总/5_3_week.xls"
        c = b.split(DIR_PATH)

        for v in c:
            print v

    def test_oppositeFileNameList(self):
        rs = oppositeFileNameList(DIR_PATH)
        for v in rs:
            print v

if __name__ == '__main__':
    unittest.main()
