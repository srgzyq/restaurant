import unittest


# -*- coding: utf-8 -*-
#import sys
#sys.path.append("..")

from dataInfo import getWeekInfoList, getAllWeekInfoList, getFormatDate


class TestDataInfo(unittest.TestCase):

    def setUp(self):
        # print "setUp.."
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

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

    def test_getFormatDate(self):
        r = getFormatDate(2016, 4)
        #print r
        #print len(r)

if __name__ == '__main__':
    unittest.main()
