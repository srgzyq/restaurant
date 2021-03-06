#-*- encoding: utf-8 -*-
'''
Created on 2016-05-26 16:56:43

@author: Srgzyq
'''
import unittest
from food.readXlsInfo import ReadXlsInfo


class TestReadXlsInfo(unittest.TestCase):

    def setUp(self):
        # print "setUp.."
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_getXlsSheetsTitle(self):
        xlsInfoOne = ReadXlsInfo("./xlsOne.xls")
        title = xlsInfoOne.getXlsSheetsTitle('income')
        self.assertEquals(title, [u'date', u'people', u'income', u'company'])

    def test_getXlsSheetsValueType(self):
        xlsInfoOne = ReadXlsInfo("./xlsOne.xls")
        types = xlsInfoOne.getXlsSheetsValueType('member')
        print types


if __name__ == '__main__':
    unittest.main()
