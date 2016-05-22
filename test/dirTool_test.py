#-*- encoding: utf-8 -*-
'''
Created on 2016-05-22 17:52:54

@author: Srgzyq
'''

import unittest
from config import DIR_PATH


from tool.dirTool import getFileNamelist


class TestDirTool(unittest.TestCase):

    def setUp(self):
        # print "setUp.."
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_getFileNamelist(self):
        print "DIR_PATH:"+ DIR_PATH
        rs = getFileNamelist(DIR_PATH)
        for filename in rs:
            print "xls:" + filename


if __name__ == '__main__':
    unittest.main()
