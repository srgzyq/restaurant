#-*- encoding: utf-8 -*-
'''
Created on 2016-06-17 11:29:50

@author: Srgzyq
'''

import unittest
from data.dbOperate import DBOperate


class TestDBOperate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        # print "tearDown.."
        pass

    def test_createTable(self):
        dbName = "testBaseData.db"
        userTable = 'user'
        userTableConect = 'id varchar(20) primary key, name varchar(20)'
        db = DBOperate(dbName)
        db.createTable(userTable, userTableConect)
        #tableSql = "select name from sqlite_master where type='table' order by name"
        #data = db.getAllData(tableSql)
        #[(u'COMPANYBASE',), (u'DAYBASE',), (u'MENUBASE',), (u'PAYBASE',), (u'user',)]
        db.dropTable(userTable)
        db.closeDbCon()

if __name__ == '__main__':
    unittest.main()
