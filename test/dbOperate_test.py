#-*- encoding: utf-8 -*-
'''
Created on 2016-06-17 11:29:50

@author: Srgzyq
'''

import unittest
from data.dbOperate import DBOperate, ReTableOperate
from data.sqlConfig import *
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
        #tname = tableName[0]
        #tsql = tableSql[0]
        #redb.createTable(tname, tsql)
        redb.closeDbCon()


if __name__ == '__main__':
    db_file = os.path.join(os.path.dirname(__file__), 'testBaseData.db')
    if os.path.isfile(db_file):
        os.remove(db_file)
    unittest.main()
