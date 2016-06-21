#-*- encoding: utf-8 -*-
'''
Created on 2016-06-17 11:29:50

@author: Srgzyq
'''

import unittest
from model.dbOperate import DBOperate, ReTableOperate
from model.sqlConfig import *
import os


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
        # db.dropTable(userTable)
        db.closeDbCon()


class TestReTableOperate(unittest.TestCase):

    def test_initTables(self):
        # print "test_initTables"
        dbName = "testBaseData.db"
        redb = ReTableOperate(dbName)
        redb.initTables(tableName, tableSql)
        redb.closeDbCon()

    def test_insertDayTables(self):
        rows = [('2016/5/1', 8, 3, 1, 0, 1, 170.0, 0, 0, '1,2', ''),
                ('2016/5/1', 8, 3, 1, 0, 1, 100.0, 0, 0, '1,2', ''),
                ('2016/5/2', 8, 3, 1, 0, 1, 170.0, 0, 0, '1,2', ''),
                ('2016/5/2', 8, 3, 1, 0, 1, 170.0, 0, 0, '1', '')]
        dbName = "testBaseData.db"
        redb = ReTableOperate(dbName)
        redb.insertDayBaseTables(insertDayBaseStr, rows)
        redb.closeDbCon()


if __name__ == '__main__':
    db_file = os.path.join(os.path.dirname(__file__), 'testBaseData.db')
    if os.path.isfile(db_file):
        os.remove(db_file)
    unittest.main()
