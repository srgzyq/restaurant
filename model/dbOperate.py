#-*- encoding: utf-8 -*-
'''
Created on 2016-06-17 11:15:33

@author: Srgzyq
'''
import sqlite3


class DBOperate(object):

    def __init__(self, name, password=''):
        super(DBOperate, self).__init__()
        # 如果文件不存在, 会自动在当前目录创建:
        self.conn = sqlite3.connect(name)
        # 创建一个Cursor:
        self.cursor = self.conn.cursor()

    def createTable(self, tableName, keyConect):
        # "create table user (id varchar(20) primary key, name varchar(20))"
        sql = "create table " + tableName + "(" + keyConect + ")"
        self.executeSql(sql)

    def dropTable(self, tableName):
        sql = "DROP TABLE " + tableName
        self.executeSql(sql)

    def getAllData(self, sql):
        self.executeSql(sql)
        value = self.cursor.fetchall()
        return value

    def executeSql(self, sql):
        self.cursor.execute(sql)
        # 提交事务
        self.conn.commit()

    def executeManySql(self, sql, rows):
        self.cursor.executemany(sql, rows)
        self.conn.commit()

    def closeDbCon(self):
        # 关闭cursor
        self.cursor.close()
        # 关闭Connection:
        self.conn.close()


class ReTableOperate(DBOperate):

    def __init__(self, name, password=''):
        super(ReTableOperate, self).__init__(name, password)

    def initTables(self, tableNames, sqls):
        for index in range(len(tableNames)):
            self.createTable(tableNames[index], sqls[index])

    def insertDayBaseTables(self, sql, rows):
        self.executeManySql(sql, rows)
