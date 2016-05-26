import unittest
import FakeData

# -*- coding: utf-8 -*-
# import sys
# sys.path.append("..")

from food.combXlsData import CombXlsData


class TestCombXlsData(unittest.TestCase):

    def setUp(self):
        self.comb = CombXlsData()
        self.comb.setXlsData(FakeData.xlsInfoOne)
        self.comb.setXlsData(FakeData.xlsInfoTwo)
        self.comb.initTableInfo()
        self.comb.initTableTitleInfo()
        self.comb.mergeTableContent()
        self.result = self.comb.getResultData()
        # print "setUp.."

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_setXlsData(self):
        self.assertEquals(len(self.comb.doMergeData), 2)

    def test_initTableInfo(self):
        self.assertTrue(u'income' in self.result)
        self.assertTrue(u'member' in self.result)

    def test_initTableTitleInfo(self):
        self.assertTrue(self.result[u'income']['ctype'][0], 3)
        self.assertTrue(self.result[u'member']['ctype'][0], 3)
        self.assertTrue('title' in self.result[u'income'])
        self.assertTrue('title' in self.result[u'member'])
        self.assertTrue('company'in self.result[u'income'][u'title'])
        self.assertTrue('num'in self.result[u'member'][u'title'])

    def test_mergeTableContent(self):
        self.assertEquals(len(self.result['income']['content']), 14)
        self.assertEquals(len(self.result['member']['content']), 6)

if __name__ == '__main__':
    unittest.main()
