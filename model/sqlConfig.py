#-*- encoding: utf-8 -*-
'''
Created on 2016-06-17 17:19:14

@author: Srgzyq
'''

tableName = ["DAYBASE", "MENUBASE", "COMPANYBASE", "PAYBASE"]

dayBaseStr = '''
ID INT PRIMARY KEY NOT NULL,
DATE TEXT NOT NULL,
DESKID INT ,
NUM INT ,
DINNER INT NOT NULL,
COMPANY_ID INT NOT NULL,
PAY_ID INT NOT NULL,
INCOME REAL NOT NULL,
DISCOUNT INT NOT NULL,
BILL INT NOT NULL,
MENU_IDS TEXT NOT NULL,
REMARKS TEXT
'''

menuBaseStr = '''
ID INT PRIMARY KEY NOT NULL,
NAME           TEXT NOT NULL
'''

companyBaseStr = '''
ID INT PRIMARY KEY  NOT NULL,
NAME           TEXT NOT NULL
'''

payBaseStr = '''
ID INT PRIMARY KEY NOT NULL,
NAME           TEXT NOT NULL
'''

tableSql = [dayBaseStr, menuBaseStr, companyBaseStr, payBaseStr]
