# -*- coding: utf-8 -*-
# import sys
# sys.path.append("..")
import os
import unittest
from dataInfo import *
from config import DIR_PATH, READ_PATH


class TestDataInfo(unittest.TestCase):

    def setUp(self):
        # print "setUp.."
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_getYamlConfig(self):
        getYamlConfig()

    def test_getWeekInfoList(self):
        # print "test_getWeekInfoList.."
        w = getWeekInfoList(2016, 5)
        # print w
        self.assertEquals(len(w[0]), 1)
        self.assertEquals(len(w[len(w) - 1]), 2)
        self.assertEquals(len(w), 6)
        w = getWeekInfoList(2015, 5)
        self.assertEquals(len(w[len(w) - 1]), 7)
        w = getWeekInfoList(2015, 6)
        self.assertEquals(len(w[0]), 7)
        # print w
        #

    def test_getAllWeekInfoList(self):
        r = getAllWeekInfoList(2016, 8)
        self.assertEquals(r[0], [1, 2, 3, 4, 5, 6, 7])
        r = getAllWeekInfoList(2016, 4)
        self.assertEquals(len(r), 5)
        self.assertEquals(r[len(r) - 1], [25, 26, 27, 28, 29, 30, 1])
        r = getAllWeekInfoList(2016, 12)
        self.assertEquals(len(r), 5)
        self.assertEquals(r[len(r) - 1], [26, 27, 28, 29, 30, 31, 1])
        r = getAllWeekInfoList(2015, 5)
        self.assertEquals(r[len(r) - 1], [25, 26, 27, 28, 29, 30, 31])
        # print r

    def test_getDirFileNameList(self):
        fileNames = getNumWeek(2016, 5, 6)
        read_xls_file = os.path.join(DIR_PATH, READ_PATH)
        dirFileNames = getDirFileNameList(fileNames, read_xls_file)
        self.assertTrue('6/2016.6.2.xlsx' in dirFileNames[3])
        self.assertTrue('6/2016.6.1.xlsx' in dirFileNames[2])

    def test_getFormatDate(self):
        r = getFormatDate(2016, 5)
        # for week in r:
        #    print week
        # print len(r)
        r = getFormatDate(2016, 4)
        self.assertEquals(len(r), 5)
        self.assertEquals(r[len(r) - 1], ['2016.4.25.xlsx', '2016.4.26.xlsx', '2016.4.27.xlsx',
                                          '2016.4.28.xlsx', '2016.4.29.xlsx', '2016.4.30.xlsx', '2016.5.1.xlsx'])
        r = getFormatDate(2015, 12)
        self.assertEquals(r[4], ['2015.12.28.xlsx', '2015.12.29.xlsx', '2015.12.30.xlsx',
                                 '2015.12.31.xlsx', '2016.1.1.xlsx', '2016.1.2.xlsx', '2016.1.3.xlsx'])

    def test_changeXlsDateToStr(self):
        strD = changeXlsDateToStr(42543)
        self.assertEquals(strD, '2016/06/22')
        strD = changeXlsDateToStr(42499.0)
        self.assertEquals(strD, '2016/05/09')

if __name__ == '__main__':
    unittest.main()
