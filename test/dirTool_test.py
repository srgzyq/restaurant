#-*- encoding: utf-8 -*-
'''
Created on 2016-05-22 17:52:54

@author: Srgzyq
'''

import unittest
from config import DIR_PATH


from tool.dirTool import getAbsFileNameList, oppositeFileNameList, isFileExist, getLocalAndDropBoxPath


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
        # print "DIR_PATH:" + DIR_PATH
        rs = getAbsFileNameList(DIR_PATH)
        # for filename in rs:
        #    print "xls:" + filename

    def test_getLocalAndDropBoxPath(self):
        getLocalAndDropBoxPath(DIR_PATH)

    def test_oppositeFileNameList(self):
        rs = oppositeFileNameList(DIR_PATH)
        # for v in rs:
        #    print v

if __name__ == '__main__':
    unittest.main()
