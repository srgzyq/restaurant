# -*- coding: utf-8 -*-
import xlwt
import xlrd
import readXlsFile
import os

from xlutils.copy import copy;


style_date = xlwt.easyxf(num_format_str='YY/MM/DD')

def mergeXlsData(from_file_name, to_file_name, sheet_num):
	# to_file_name 文件是否存在 sheet_num 是否存在
	
	if os.path.isfile(to_file_name):
		ready_sheet_num = readXlsFile.getXlsSheetNum(to_file_name)
		print "ready_sheet_num",ready_sheet_num,"sheet_num",sheet_num
		copyXlsDataByFile(from_file_name,to_file_name,sheet_num)
		#if (ready_sheet_num == sheet_num+1):
		#	copyXlsDataByFile(from_file_name,to_file_name,sheet_num)
		#else:
		#	writeXlsDataByFile(from_file_name,to_file_name,sheet_num)
	else:
		# 直接 copy
		writeXlsDataByFile(from_file_name,to_file_name,sheet_num)
		

def writeXlsDataByFile(read_file_name,write_file_name,sheet_num):
	# 生成一个xls对象
	write_file = xlwt.Workbook()
	# 初始化table
	sheet_name = readXlsFile.getXlsSheetNameByIndex(read_file_name,sheet_num)
	print sheet_name
	table = write_file.add_sheet(sheet_name)
	
	# 获取文件sheet 为sheet_num的 内容
	xls_titles,xls_data = readXlsFile.getXlsDataByFile(read_file_name,sheet_num)

	for col,title in enumerate(xls_titles):
		if xlrd.XL_CELL_TEXT == title[0]:
			table.write(0,col,title[1])

	# 插入剩余内容
	for row,contents in enumerate(xls_data):
		for col,content in enumerate(contents):
			if xlrd.XL_CELL_DATE == content[0]:
				table.write(row+1,col,content[1],style_date)
			else:
				table.write(row+1,col,content[1])

	write_file.save(write_file_name)

def copyXlsDataByFile(from_file_name,to_file_name,sheet_num):
	old_xls_file = readXlsFile.getXlsTableByFileAndSheet(to_file_name)
	
	# to do list
	old_rows,old_cols = readXlsFile.getXlsTableRowAndCol(to_file_name,0)

	new_xls_table = copy(old_xls_file)
	
	# to do list
	table = new_xls_table.get_sheet(0)

	# 获取文件sheet 为0的 内容
	xls_titles,xls_data = readXlsFile.getXlsDataByFile(from_file_name,sheet_num)

	# 插入剩余内容
	for row,contents in enumerate(xls_data):
		row = row+old_rows-1
		for col,content in enumerate(contents):
			if xlrd.XL_CELL_DATE == content[0]:
				table.write(row+1,col,content[1],style_date)
			else:
				table.write(row+1,col,content[1])

	new_xls_table.save(to_file_name);


def testWriteXlsDataByFile():
	writeXlsDataByFile("./data/2016.4.11.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.12.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.13.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.14.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.15.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.16.xlsx",u"./data/4月/1.xls",0)
	copyXlsDataByFile("./data/2016.4.17.xlsx",u"./data/4月/1.xls",0)

def testMergeXlsData():
	from_file_names = ["./data/2016.4.11.xlsx","./data/2016.4.12.xlsx","./data/2016.4.13.xlsx","./data/2016.4.14.xlsx","./data/2016.4.15.xlsx","./data/2016.4.16.xlsx","./data/2016.4.17.xlsx"]
	to_file_name = u"./data/4月/1.xls"
	for file_name in from_file_names:
		mergeXlsData(file_name,to_file_name,0)
		#mergeXlsData(file_name,to_file_name,1)

testMergeXlsData()
#testWriteXlsDataByFile()


	

