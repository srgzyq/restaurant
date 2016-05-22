import unittest


# -*- coding: utf-8 -*-
#import sys
# sys.path.append("..")

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
        self.dropBoxObj.uploadFile("./xlsOne.xls", "/JiJia/5/xlsOne.xls")


if __name__ == '__main__':
    unittest.main()
