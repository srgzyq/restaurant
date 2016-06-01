import unittest
import FakeData

# -*- coding: utf-8 -*-
# import sys
# sys.path.append("..")

from food.combXlsData import CombXlsData


class TestCombXlsData(unittest.TestCase):
    def setUp(self):
        self.comb = CombXlsData()
        self.comb.setXlsData(FakeData.getXlsFileDataByName("./xlsOne.xls"))
        self.comb.setXlsData(FakeData.getXlsFileDataByName("./xlsTwo.xls"))
        self.comb.initTableInfo()
        self.comb.initTableTitleInfo()
        self.comb.mergeTableContent()
        self.result = self.comb.getResultData()

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_setXlsData(self):
        self.assertEquals(len(self.comb.doMergeData), 2)

    def test_initTableInfo(self):
        self.assertEquals(u'income' , self.result[0]['name'])
        self.assertEquals(u'member' , self.result[1]['name'])

    def test_initTableTitleInfo(self):
        self.assertTrue(self.result[0]['ctype'][0], 3) #income
        self.assertTrue(self.result[1]['ctype'][0], 3) #member
        self.assertTrue('title' in self.result[0])
        self.assertTrue('title' in self.result[1])
        self.assertTrue('company'in self.result[0][u'title'])
        self.assertTrue('num'in self.result[1][u'title'])

    def test_mergeTableContent(self):
        self.assertEquals(len(self.result[0]['content']), 14)
        self.assertEquals(len(self.result[1]['content']), 6)

if __name__ == '__main__':
    unittest.main()
